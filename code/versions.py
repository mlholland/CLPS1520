import numpy as np  

'''

NOTE: for ./full_pipe compatability, make sure for version_XYZ that
params['out_dir'] = '../dataset/mixed_images_XYZ/'


NOTE: change scratch to be your scratch space (your name)
'''

scratch = '/gpfs/scratch/guest123/matlab1520/mixed_images_'

def version_0(params):
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/all/'
    params['out_dir'] = '../dataset/mixed_images_0'
    params['data'] = '../dataset/data.json'
    params['im_ex'] = '*.*g'
    params['x_dim'] = 227
    params['y_dim'] = 227
    params['two_fg'] = False
    params['bg_color'] = None
    params['grid_pos_x'] = [.5]
    params['grid_pos_y'] = [.5]
    params['grid_scale'] = [.5]
    params['grid_occlusion'] = [0]
    params['grid_opacity'] = [1]
    params['bg_only'] = False

    return params

def version_preston(params):
    #params = version_0
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['out_dir'] = '../results/'
    return params
#MILES!!!!!
def version_control(params):
    params = version_0(params)
    params['bg_color'] = .5
    params['grid_scale'] = .9
    return params

def version_background(params):
    params = version_0(params)
    params['bg_only'] = True
    return params

#MILESSSSS
#gray with two foregrounds:
def version_1(params):
    params = version_0(params)
    params['fg2_dir'] = '../dataset/foregrounds/images/all/;'
    params['bg_color'] = .5
    params['two_fg'] = True
    return params

#backrgound images with two foregrounds:
def version_2(params):
    params = version_0(params)
    params['fg2_dir'] = '../dataset/foregrounds/images/all;'
    params['two_fg'] = True
    return params

#single foreground black backrgound grid pos_x and size
def version_3(params):
    params = version_0(params)
    params['bg_color'] = 0.0
    params['grid_pos_x'] = np.arange(.25,1,.5).tolist()
    params['grid_scale'] = np.arange(.25,1,.5).tolist()
    return params

#single foreground backrgound image grid pos_x opacity
def version_4(params):
    params = version_0(params)
    #params['grid_pos_x'] = np.arange(.25,1,.5).tolist()
    params['grid_opacity'] = np.arange(.2,1.2,.2).tolist()
    return params

#helper version for phil running locally, feel free to make your own with proper directories, pass into version_fix argument
def version_phil(params):
    params['bg_dir'] = '../phil_images/b1/'
    params['fg_dir'] = '../phil_images/f1/'
    params['fg2_dir'] = '../phil_images/f2/'
    params['out_dir'] = '../phil_images/o1/'
    params['data'] = '../phil_images/data.json'
    return params

def version_miles_test(params):
    params = version_0(params)
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['out_dir'] = scratch + 'miles_test/'
    return params

def version_all_all_scale_01(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/all/'
    params['out_dir'] = scratch + 'all_all_scale_01/'
    params['grid_scale'] = [0.1]
    return params

def version_all_all_scale_02(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/all/'
    params['out_dir'] = scratch + 'all_all_scale_02/'
    params['grid_scale'] = [0.2]
    return params

def version_all_all_scale_03(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/all/'
    params['out_dir'] = scratch + 'all_all_scale_03/'
    params['grid_scale'] = [0.3]
    return params

def version_all_all_scale_04(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/all/'
    params['out_dir'] = scratch + 'all_all_scale_04/'
    params['grid_scale'] = [0.4]
    return params

def version_all_all_scale_05(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/all/'
    params['out_dir'] = scratch + 'all_all_scale_05/'
    params['grid_scale'] = [0.5]
    return params

def version_all_all_scale_06(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/all/'
    params['out_dir'] = scratch + 'all_all_scale_06/'
    params['grid_scale'] = [0.6]
    return params

def version_all_all_scale_07(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/all/'
    params['out_dir'] = scratch + 'all_all_scale_07/'
    params['grid_scale'] = [0.7]
    return params

def version_all_all_scale_08(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/all/'
    params['out_dir'] = scratch + 'all_all_scale_08/'
    params['grid_scale'] = [0.8]
    return params

def version_all_all_scale_09(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/all/'
    params['out_dir'] = scratch + 'all_all_scale_09/'
    params['grid_scale'] = [0.9]
    return params

####toaster cross##################

def version_2_broccoli_toaster_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/broccoli/'
    params['fg2_dir'] = '../dataset/foregrounds/images/toaster/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_broccoli_toaster_all/'
    return params

def version_2_flamingo_toaster_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['fg2_dir'] = '../dataset/foregrounds/images/toaster/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_flamingo_toaster_all/'
    return params

def version_2_hammer_toaster_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/hammer/'
    params['fg2_dir'] = '../dataset/foregrounds/images/toaster/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_hammer_toaster_all/'
    return params

def version_2_hummingbird_toaster_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['fg2_dir'] = '../dataset/foregrounds/images/toaster/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_hummingbird_toaster_all/'
    return params

def version_2_laptop_toaster_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/laptop/'
    params['fg2_dir'] = '../dataset/foregrounds/images/toaster/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_laptop_toaster_all/'
    return params

def version_2_powerdrill_toaster_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['fg2_dir'] = '../dataset/foregrounds/images/toaster/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_powerdrill_toaster_all/'
    return params

def version_2_shovel_toaster_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/shovel/'
    params['fg2_dir'] = '../dataset/foregrounds/images/toaster/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_shovel_toaster_all/'
    return params

def version_2_tarantula_toaster_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['fg2_dir'] = '../dataset/foregrounds/images/toaster/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_tarantula_toaster_all/'
    return params

def version_2_taxi_toaster_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['fg2_dir'] = '../dataset/foregrounds/images/toaster/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_taxi_toaster_all/'
    return params

#########flamingo crosss

def version_2_toaster_flamingo_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/toaster/'
    params['fg2_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_toaster_flamingo_all/'
    return params

def version_2_hammer_flamingo_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/hammer/'
    params['fg2_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_hammer_flamingo_all/'
    return params

def version_2_hummingbird_flamingo_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['fg2_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_hummingbird_flamingo_all/'
    return params

def version_2_laptop_flamingo_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/laptop/'
    params['fg2_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_laptop_flamingo_all/'
    return params

def version_2_powerdrill_flamingo_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['fg2_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_powerdrill_flamingo_all/'
    return params

def version_2_shovel_flamingo_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/shovel/'
    params['fg2_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_shovel_flamingo_all/'
    return params

def version_2_tarantula_flamingo_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['fg2_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_tarantula_flamingo_all/'
    return params

def version_2_taxi_flamingo_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['fg2_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_taxi_flamingo_all/'
    return params

#########hammer crosss

def version_2_toaster_hammer_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/toaster/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hammer/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_toaster_hammer_all/'
    return params

def version_2_flamingo_hammer_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hammer/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_flamingo_hammer_all/'
    return params

def version_2_hummingbird_hammer_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hammer/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_hummingbird_hammer_all/'
    return params

def version_2_laptop_hammer_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/laptop/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hammer/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_laptop_hammer_all/'
    return params

def version_2_powerdrill_hammer_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hammer/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_powerdrill_hammer_all/'
    return params

def version_2_shovel_hammer_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/shovel/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hammer/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_shovel_hammer_all/'
    return params

def version_2_tarantula_hammer_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hammer/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_tarantula_hammer_all/'
    return params

def version_2_taxi_hammer_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hammer/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_taxi_hammer_all/'
    return params

#########hummingbird crosss

def version_2_toaster_hummingbird_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/toaster/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_toaster_hummingbird_all/'
    return params

def version_2_flamingo_hummingbird_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_flamingo_hummingbird_all/'
    return params

def version_2_hammer_hummingbird_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_hummingbird_hummingbird_all/'
    return params

def version_2_laptop_hummingbird_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/laptop/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_laptop_hummingbird_all/'
    return params

def version_2_powerdrill_hummingbird_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_powerdrill_hummingbird_all/'
    return params

def version_2_shovel_hummingbird_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/shovel/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_shovel_hummingbird_all/'
    return params

def version_2_tarantula_hummingbird_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_tarantula_hummingbird_all/'
    return params

def version_2_taxi_hummingbird_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['fg2_dir'] = '../dataset/foregrounds/images/hummingbird/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_taxi_hummingbird_all/'
    return params

#########laptop crosss

def version_2_toaster_laptop_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/toaster/'
    params['fg2_dir'] = '../dataset/foregrounds/images/laptop/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_toaster_laptop_all/'
    return params

def version_2_flamingo_laptop_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['fg2_dir'] = '../dataset/foregrounds/images/laptop/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_flamingo_laptop_all/'
    return params

def version_2_hammer_laptop_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/laptop/'
    params['fg2_dir'] = '../dataset/foregrounds/images/laptop/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_laptop_laptop_all/'
    return params

def version_2_hummingbird_laptop_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/laptop/'
    params['fg2_dir'] = '../dataset/foregrounds/images/laptop/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_laptop_laptop_all/'
    return params

def version_2_powerdrill_laptop_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['fg2_dir'] = '../dataset/foregrounds/images/laptop/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_powerdrill_laptop_all/'
    return params

def version_2_shovel_laptop_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/shovel/'
    params['fg2_dir'] = '../dataset/foregrounds/images/laptop/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_shovel_laptop_all/'
    return params

def version_2_tarantula_laptop_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['fg2_dir'] = '../dataset/foregrounds/images/laptop/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_tarantula_laptop_all/'
    return params

def version_2_taxi_laptop_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['fg2_dir'] = '../dataset/foregrounds/images/laptop/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_taxi_laptop_all/'
    return params

#########powerdrill crosss

def version_2_toaster_powerdrill_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/toaster/'
    params['fg2_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_toaster_powerdrill_all/'
    return params

def version_2_flamingo_powerdrill_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['fg2_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_flamingo_powerdrill_all/'
    return params

def version_2_hammer_powerdrill_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['fg2_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_powerdrill_powerdrill_all/'
    return params

def version_2_laptop_powerdrill_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/laptop/'
    params['fg2_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_laptop_powerdrill_all/'
    return params

def version_2_hummingbird_powerdrill_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['fg2_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_powerdrill_powerdrill_all/'
    return params

def version_2_shovel_powerdrill_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/shovel/'
    params['fg2_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_shovel_powerdrill_all/'
    return params

def version_2_tarantula_powerdrill_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['fg2_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_tarantula_powerdrill_all/'
    return params

def version_2_taxi_powerdrill_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['fg2_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_taxi_powerdrill_all/'
    return params

#########shovel crosss

def version_2_toaster_shovel_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/toaster/'
    params['fg2_dir'] = '../dataset/foregrounds/images/shovel/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_toaster_shovel_all/'
    return params

def version_2_flamingo_shovel_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['fg2_dir'] = '../dataset/foregrounds/images/shovel/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_flamingo_shovel_all/'
    return params

def version_2_hammer_shovel_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/shovel/'
    params['fg2_dir'] = '../dataset/foregrounds/images/shovel/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_shovel_shovel_all/'
    return params

def version_2_laptop_shovel_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/laptop/'
    params['fg2_dir'] = '../dataset/foregrounds/images/shovel/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_laptop_shovel_all/'
    return params

def version_2_powerdrill_shovel_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['fg2_dir'] = '../dataset/foregrounds/images/shovel/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_powerdrill_shovel_all/'
    return params

def version_2_hummingbird_shovel_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/shovel/'
    params['fg2_dir'] = '../dataset/foregrounds/images/shovel/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_shovel_shovel_all/'
    return params

def version_2_tarantula_shovel_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['fg2_dir'] = '../dataset/foregrounds/images/shovel/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_tarantula_shovel_all/'
    return params

def version_2_taxi_shovel_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['fg2_dir'] = '../dataset/foregrounds/images/shovel/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_taxi_shovel_all/'
    return params

#########tarantula crosss

def version_2_toaster_tarantula_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/toaster/'
    params['fg2_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_toaster_tarantula_all/'
    return params

def version_2_flamingo_tarantula_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['fg2_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_flamingo_tarantula_all/'
    return params

def version_2_hammer_tarantula_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['fg2_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_tarantula_tarantula_all/'
    return params

def version_2_laptop_tarantula_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/laptop/'
    params['fg2_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_laptop_tarantula_all/'
    return params

def version_2_powerdrill_tarantula_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['fg2_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_powerdrill_tarantula_all/'
    return params

def version_2_hummingbird_tarantula_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['fg2_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_tarantula_tarantula_all/'
    return params

def version_2_shovel_tarantula_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['fg2_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_tarantula_tarantula_all/'
    return params

def version_2_taxi_tarantula_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['fg2_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_taxi_tarantula_all/'
    return params

#########taxi crosss

def version_2_toaster_taxi_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/toaster/'
    params['fg2_dir'] = '../dataset/foregrounds/images/taxi/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_toaster_taxi_all/'
    return params

def version_2_flamingo_taxi_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/flamingo/'
    params['fg2_dir'] = '../dataset/foregrounds/images/taxi/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_flamingo_taxi_all/'
    return params

def version_2_hammer_taxi_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['fg2_dir'] = '../dataset/foregrounds/images/taxi/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_taxi_taxi_all/'
    return params

def version_2_laptop_taxi_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/laptop/'
    params['fg2_dir'] = '../dataset/foregrounds/images/taxi/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_laptop_taxi_all/'
    return params

def version_2_powerdrill_taxi_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/powerdrill/'
    params['fg2_dir'] = '../dataset/foregrounds/images/taxi/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_powerdrill_taxi_all/'
    return params

def version_2_hummingbird_taxi_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['fg2_dir'] = '../dataset/foregrounds/images/taxi/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_taxi_taxi_all/'
    return params

def version_2_tarantula_taxi_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/tarantula/'
    params['fg2_dir'] = '../dataset/foregrounds/images/taxi/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_tarantula_taxi_all/'
    return params

def version_2_shovel_taxi_all(params):
    params = version_0(params)
    params['bg_dir'] = '../dataset/backgrounds/images/all/'
    params['fg_dir'] = '../dataset/foregrounds/images/taxi/'
    params['fg2_dir'] = '../dataset/foregrounds/images/taxi/'
    params['two_fg'] = True
    params['out_dir'] = scratch + '2_taxi_taxi_all/'
    return params
