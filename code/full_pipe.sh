#!/bin/bash

#does the full pipe of making images, classifying them
#and getting tho accuracy from those classifications.
#Requires 3 inputs, the background and foreground 
#directories, as well as a suffix to append to
#the output files.

#CRITICAL NOTE: Before running, make sure
## that the run_name variable matches a mix_fg_bg version
## that params['out_dir'] = mix_dir (the mix_dir below, that is)
## that you set time properly (takes about 6 min for 650 images, scale that)

#can either be run normally, or as an sbatch job using
#sbatch ./full_pipe arguments


#SBATCH --time=00:40:00
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --mem=1G
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1

run_name=$1
mix_dir='../dataset/mixed_images_'$run_name'/'
class='../results/classifications_'$run_name'.csv'
accuracy='../results/accuracy_'$run_name'.csv'

mkdir $mix_dir
echo 'making images...'
python mix_fg_bg.py -v $run_name
echo 'classifying images...'
./auto_categorize.sh $mix_dir $class
echo 'calculating accuracies...'
python determine_accuracy.py --input $class --output $accuracy
rm -rf $mix_dir


