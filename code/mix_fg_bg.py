#!/bin/python

'''
Takes a directory of background images and a directory of forground images, and produces the
'image crossproduct' of the two directories. That is, for each background/foreground image
pair, it produces a new image that contains the foreground image placed on top of the background
image.

'''
from PIL import Image
import numpy as np
from scipy.ndimage.interpolation import zoom  as scipy_zoom
import argparse
import glob
import os
from copy import deepcopy


def make_output_fname(bg_fname, fg_fname):
    return ''

def main():
    #parse inputs, this requires 3 directories as input at least (bg, fg, and out)
    #general usage: python ./mix_fg_bg --bg_dir DIR --fg_dir DIR --out_dir DIR [--im_ex EX]
    parser = argparse.ArgumentParser()
    parser.add_argument("--bg_dir", type=str, help='background directory')
    parser.add_argument("--fg_dir", type=str, help='foreground directory')
    parser.add_argument("--out_dir", type=str, help='output directory. Must already exist.')
    parser.add_argument("--im_ex", type=str, help='extension of valid images, defaults to \'*.png\'.')
    args = parser.parse_args()
    
    #loop through background images
    for bg_fname in glob.glob(os.path.join(args.bg_dir,args.im_ex)):
        bg = Image.open(bg_fname)
        
        #loop through foreground files
        for fg_fname in glob.glob(os.path.join(args.fg_dir,args.im_ex)):
            
            out_image = deepcopy(bg)
            fg = Image.open(fg_fname)
            
            #make sure the foreground file has transparency
            if not fg.info.has_key('transparency') and not fg.mode == 'RGBA':
                import ipdb; ipdb.set_trace()
                print "Foreground file %s does not have a transparency value, foregoing this file" % fg_fname
                fg.close()
                continue
            

            #get the ratio between the foreground and background (used for rescaling)
            if fg.size[0] > fg.size[1]:
                resize_ratio = 1.0 * bg.size[0] / (2 * fg.size[0])
            else:
                resize_ratio = 1.0 * bg.size[1] / (2 * fg.size[1])

            #rescale
            fg_resized = fg.resize((int(fg.size[0] * resize_ratio), int(fg.size[1] * resize_ratio)))
            #convert to RGBA format (sometimes starts in 'P')
            fg_final = fg_resized.convert('RGBA')
            
            #overlay
            out_image.paste(fg_final,(bg.size[0] / 2 - fg_final.size[0] / 2, bg.size[1] / 2 - fg_final.size[1] / 2), fg_final)            

            fg.close()

            #write output
            out_fname = os.path.join(args.out_dir, fg_fname[fg_fname.rindex('/') + 1:fg_fname.rindex('.')] + '__' + bg_fname[bg_fname.rindex('/') + 1:])
            out_image.save(out_fname)
        bg.close()


if __name__ == '__main__':
    main()
