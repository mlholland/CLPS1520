#!/bin/python

'''
Takes a directory of background images and a directory of forground images, and produces the
'image crossproduct' of the two directories. That is, for each background/foreground image
pair, it produces a new image that contains the foreground image placed on top of the background
image.

'''
from PIL import Image, ImageDraw
import numpy as np
from scipy.ndimage.interpolation import zoom  as scipy_zoom
import argparse
import glob
import os
from copy import deepcopy


def make_output_fname(bg_fname, fg_fname):
    return ''

def resize_img(img, bg, scale=.5):
    scale = 1/scale
    if img.size[0] > img.size[1]:
        resize_ratio = 1.0 * bg.size[0] / (scale * img.size[0])
    else:
        resize_ratio = 1.0 * bg.size[1] / (scale * img.size[1])
    img = img.resize((int(img.size[0] * resize_ratio), int(img.size[1] * resize_ratio)))
    return img.convert('RGBA')

def paste_img(fg, bg, pos_x=.5, pos_y=.5):
    pos_x = 1/pos_x
    pos_y = 1/pos_y
    bg.paste(fg,(int(bg.size[0] / pos_x - fg.size[0] / 2), int(bg.size[1] / pos_y - fg.size[1] / 2)), fg) 
    return bg

def compose_img(args, bg, bg_fname):
    for fg_fname in glob.glob(os.path.join(args.fg_dir,args.im_ex)):
        out_image = bg.copy()

        fg = Image.open(fg_fname)
        if not fg.info.has_key('transparency') and not fg.mode == 'RGBA':
            import ipdb; ipdb.set_trace()
            print "Foreground file %s does not have a transparency value, foregoing this file" % fg_fname
            fg.close()
            continue
        
        fg_final = resize_img(fg, bg)

        if args.fg2_dir:
            for fg2_fname in glob.glob(os.path.join(args.fg2_dir,args.im_ex)):
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
                out_fname = os.path.join(args.out_dir, fg_fname[fg_fname.rindex('/') + 1:fg_fname.rindex('.')] + '_' +  \
                                        fg2_fname[fg2_fname.rindex('/') + 1:fg2_fname.rindex('.')] + '_' + bg_fname[bg_fname.rindex('/') + 1:])
                out_image.save(out_fname)
                fg2.close()
        else:
        #out_data = mix_images(bg, fg)
            out_image = paste_img(fg_final, out_image, .5, .5)           

            #write output
            out_fname = os.path.join(args.out_dir, fg_fname[fg_fname.rindex('/') + 1:fg_fname.rindex('.')] + '_' + bg_fname[bg_fname.rindex('/') + 1:])
            out_image.save(out_fname)
        fg.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bg_dir", type=str, help='background directory') 
    parser.add_argument("--fg_dir", type=str, help='foreground directory')
    parser.add_argument("--fg2_dir", type=str, help='second foreground directory, optional', default=None)
    parser.add_argument("--x_dim", type=int, help='size of output image, note: will stretch background', default=None)
    parser.add_argument("--y_dim", type=int, help='size of output image, note: will stretch background', default=None)
    parser.add_argument("--bg_color", type=float, help='background color, black = 0, white = 1', default=None)
    #TODO: parser.add_argument("--grid_pos", type=int, help='number of steps to grid fg position by', default=None)
    #TODO: parser.add_argument("--grid_size", type=int, help='number of steps to grid fg size by', default=None)
    parser.add_argument("--out_dir", type=str, help='output directory. Must already exist.')
    parser.add_argument("--im_ex", type=str, help='extension of valid images, defaults to \'*.png\'.', default="*.png")
    args = parser.parse_args()
    
    if args.bg_color and args.x_dim and args.y_dim:
        bg = Image.new('F', (args.x_dim,args.y_dim), args.bg_color*255).convert("RGB")
        bg_fname = "/color.jpg"
        compose_img(args, bg, bg_fname)
        bg.close()
    else:
        for bg_fname in glob.glob(os.path.join(args.bg_dir,args.im_ex)):
            bg = Image.open(bg_fname)
            if args.x_dim and args.y_dim:
                bg = bg.resize((args.x_dim,args.y_dim))
            compose_img(args, bg, bg_fname)
            bg.close()


if __name__ == '__main__':
    main()
