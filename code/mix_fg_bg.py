#!/bin/python

'''
Takes a directory of background images and a directory of forground images, and produces the
'image crossproduct' of the two directories. That is, for each background/foreground image
pair, it produces a new image that contains the foreground image placed on top of the background
image.

'''
from PIL import Image, ImageDraw, ImageMath
import numpy as np
from scipy.ndimage.interpolation import zoom  as scipy_zoom
import argparse
import glob
import os
from copy import deepcopy
import versions
import json

# uniformly scales img, scaled so its largest dimension
# is scale multiplied by the corresponding background image
# ex: img dims = 300 x 600
#     bg dims = 100 x 100
#     scale = .5
# output img dims = 25 x 50
def resize_img(img, bg, scale=.5):
    scale = 1/scale
    if img.size[0] > img.size[1]:
        resize_ratio = 1.0 * bg.size[0] / (scale * img.size[0])
    else:
        resize_ratio = 1.0 * bg.size[1] / (scale * img.size[1])
    img = img.resize((int(img.size[0] * resize_ratio), int(img.size[1] * resize_ratio)))
    return img.convert('RGBA')


def center_crop_img(img, x, y):
    if img.size[0] < img.size[1]:
        img = img.resize((x,int(x*img.size[1]/img.size[0])))
    else:
        img = img.resize((int(y*img.size[0]/img.size[1]),y))
    x_int = 0
    y_int = 0
    half_the_width = img.size[0] // 2
    half_the_height = img.size[1] // 2
    if x%2:
        x_int = 1
    if y%2:
        y_int = 1
    img = img.crop(
    (
        half_the_width - x//2,
        half_the_height - y//2,
        half_the_width + x//2 + x_int,
        half_the_height + y//2 + y_int
    ))
    return img

# places a foreground image on a background so the 
# foreground center is positioned at pos_x,pos_y on the 
# background, where pos_x = 0 would be the far left, and 
# pos_x = 1 would be far right of the background
def paste_img(fg, bg, pos_x=.5, pos_y=.5, opacity=1):
    pos_x = 1/pos_x
    pos_y = 1/pos_y
    old_bg = bg.copy()
    bg.paste(fg,(int(bg.size[0] / pos_x - fg.size[0] / 2), int(bg.size[1] / pos_y - fg.size[1] / 2)), fg) 
    bg = Image.blend(old_bg, bg, opacity)
    return bg

def compose_img(params, bg, bg_fname, data):
    #loop through first set of fg images
    for fg_fname in glob.glob(os.path.join(params['fg_dir'],params['im_ex'])):

        fg = Image.open(fg_fname)
        if not fg.info.has_key('transparency') and not fg.mode == 'RGBA':
            import ipdb; ipdb.set_trace()
            print "Foreground file %s does not have a transparency value, foregoing this file" % fg_fname
            fg.close()
            continue
        
        fg_final = resize_img(fg, bg)

        #if a second foreground directory is specified, iterate through that too
        if params['two_fg'] and params['fg2_dir']:
            for fg2_fname in glob.glob(os.path.join(params['fg2_dir'],params['im_ex'])):
                out_image = bg.copy()
                fg2 = Image.open(fg2_fname)
                if not fg2.info.has_key('transparency') and not fg2.mode == 'RGBA':
                    import ipdb; ipdb.set_trace()
                    print "Second foreground file %s does not have a transparency value, foregoing this file" % fg2_fname
                    fg2.close()
                    continue
                
                fg2_final = resize_img(fg2, bg)
                out_image = paste_img(fg_final, out_image, .25, .5)   
                out_image = paste_img(fg2_final, out_image, .75, .5)          

                #write output
                out_fname = os.path.join(params['out_dir'], '2_' + fg_fname[fg_fname.rindex('/') + 1:fg_fname.rindex('.')] + '_' +  \
                                        fg2_fname[fg2_fname.rindex('/') + 1:fg2_fname.rindex('.')] + '_'  + bg_fname[bg_fname.rindex('/') + 1:])
                out_image.save(out_fname)
                fg2.close()
                data[out_fname] = params
        else:
            for x in params['grid_pos_x']:
                for y in params['grid_pos_y']:
                    for s in params['grid_scale']:
                        for oc in params['grid_occlusion']:
                            for op in params['grid_opacity']:
                                out_image = bg.copy()
                                fg_final = resize_img(fg, bg, s)
                                out_image = paste_img(fg_final, out_image, x, y, op)
                                #write output
                                f = map(str, [x,y,s,oc,op])
                                f = "_".join(f)
                                out_fname = os.path.join(params['out_dir'], fg_fname[fg_fname.rindex('/') + 1:fg_fname.rindex('.')] + '_' + f + '_' + bg_fname[bg_fname.rindex('/') + 1:])
                                out_image.save(out_fname)
                                params['f_pos_x'] = x
                                params['f_pos_y'] = y
                                params['f_scale'] = s
                                params['occlusion'] = oc
                                params['f_opacity'] = op
                                params['fg_fname'] = fg_fname
                                params['bg_fname'] = bg_fname
                                data[out_fname] = params
        
        fg.close()
    return data

def main():
    #parse inputs, this requires 3 directories as input at least (bg, fg, and out)
    #general usage: python ./mix_fg_bg --bg_dir DIR --fg_dir DIR --out_dir DIR [--im_ex EX]
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", type=str, help='version from versions.py', default="0") 
    parser.add_argument("-w", "--version_fix", type=str, help='helper version from versions.py, use for updating filepaths', default=None) 
    args = parser.parse_args()
    params = {'version': args.version}

    fn = getattr(versions, 'version_%s' % args.version)
    params = fn(params)
    if args.version_fix:
        fn = getattr(versions, 'version_%s' % args.version_fix)
        params = fn(params)

    try:
        with open(params['data'],'r') as data_json:
            try:
                data = json.load(data_json)
            except ValueError:
                print "No JSON data found, creating new one."
                data = {}
    except IOError:
        print "No JSON data found, creating new one."
        data = {}


    if params['bg_color'] != None and params['x_dim'] and params['y_dim']:
        bg = Image.new('F', (params['x_dim'],params['y_dim']), params['bg_color']*255).convert("RGB")
        bg_fname = "/color.jpg"
        data = compose_img(params, bg, bg_fname, data)
        bg.close()
    else:
        for bg_fname in glob.glob(os.path.join(params['bg_dir'],params['im_ex'])):
            bg = Image.open(bg_fname)
            if params['x_dim'] and params['y_dim']:
                bg = center_crop_img(bg, params['x_dim'], params['y_dim'])
                if params['bg_only']:
                    out_fname = os.path.join(params['out_dir'], params['x_dim'] + '_' + params['y_dim'] + '_' + bg_fname[bg_fname.rindex('/') + 1:])
                    out_image.save(out_fname)
                    continue
            data = compose_img(params, bg, bg_fname, data)
            bg.close()
    if not params['bg_only']:
        with open(params['data'],'w') as data_json:
            json.dump(data, data_json)

if __name__ == '__main__':
    main()
