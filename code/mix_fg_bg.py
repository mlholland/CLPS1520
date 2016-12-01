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
    parser = argparse.ArgumentParser()
    parser.add_argument("--bg_dir", type=str, help='background directory')
    parser.add_argument("--fg_dir", type=str, help='foreground directory')
    parser.add_argument("--fg_dir_2", type=str, help='second foreground directory, optional', default=None)
    parser.add_argument("--rand_pos", type=bool, help='randomize forground image position')
    parser.add_argument("--out_dir", type=str, help='output directory. Must already exist.')
    parser.add_argument("--im_ex", type=str, help='extension of valid images, defaults to \'*.png\'.', default=".png")
    args = parser.parse_args()
    
    for bg_fname in glob.glob(os.path.join(args.bg_dir,args.im_ex)):
        bg = Image.open(bg_fname)
        for fg_fname in glob.glob(os.path.join(args.fg_dir,args.im_ex)):

            out_image = deepcopy(bg)
            fg = Image.open(fg_fname)
            if not fg.info.has_key('transparency') and not fg.mode == 'RGBA':
                import ipdb; ipdb.set_trace()
                print "Foreground file %s does not have a transparency value, foregoing this file" % fg_fname
                fg.close()
                continue
            
            #out_data = mix_images(bg, fg)

            if fg.size[0] > fg.size[1]:
                resize_ratio = 1.0 * bg.size[0] / (2 * fg.size[0])
            else:
                resize_ratio = 1.0 * bg.size[1] / (2 * fg.size[1])

            fg_resized = fg.resize((int(fg.size[0] * resize_ratio), int(fg.size[1] * resize_ratio)))
            fg_final = fg_resized.convert('RGBA')
            out_image.paste(fg_final,(bg.size[0] / 2 - fg_final.size[0] / 2, bg.size[1] / 2 - fg_final.size[1] / 2), fg_final)            
            fg.close()

            #write output
            out_fname = os.path.join(args.out_dir, fg_fname[fg_fname.rindex('/') + 1:fg_fname.rindex('.')] + '__' + bg_fname[bg_fname.rindex('/') + 1:])
            out_image.save(out_fname)
        bg.close()


if __name__ == '__main__':
    main()
