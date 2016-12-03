    # parser = argparse.ArgumentParser()
    # parser.add_argument("--bg_dir", type=str, help='background directory') 
    # parser.add_argument("--fg_dir", type=str, help='foreground directory')
    # parser.add_argument("--fg2_dir", type=str, help='second foreground directory, optional', default=None)
    # parser.add_argument("--x_dim", type=int, help='size of output image, note: will stretch background', default=None)
    # parser.add_argument("--y_dim", type=int, help='size of output image, note: will stretch background', default=None)
    # parser.add_argument("--bg_color", type=float, help='background color, black = 0, white = 1', default=None)
    # #TODO: parser.add_argument("--grid_pos", type=int, help='number of steps to grid fg position by', default=None)
    # #TODO: parser.add_argument("--grid_size", type=int, help='number of steps to grid fg size by', default=None)
    # parser.add_argument("--out_dir", type=str, help='output directory. Must already exist.')
    # parser.add_argument("--im_ex", type=str, help='extension of valid images, defaults to \'*.png\'.', default="*.*g")

def version_0(params):
    params['bg_dir'] = '../dataset/backgrounds/images/'
    params['fg_dir'] = '../dataset/foregrounds/images/'
    params['out_dir'] = '../dataset/images/'


