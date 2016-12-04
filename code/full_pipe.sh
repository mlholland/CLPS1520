#!/bin/bash

#does the full pipe of making images, classifying them
#and getting tho accuracy from those classifications.
#Requires 3 inputs, the background and foreground 
#directories, as well as a suffix to append to
#the output files.

#can either be run normally, or as an sbatch job using
#sbatch ./full_pipe arguments


#SBATCH --time=00:40:00
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --mem=1G
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1

bg_dir=$1
fg_dir=$2
mix_dir='../dataset/mixed_images_'$3'/'
class='../results/classifications_'$3'.csv'
accuracy='../results/accuracy_'$3'.csv'

mkdir $mix_dir
echo 'making images...'
python mix_fg_bg.py --bg_dir $bg_dir --fg_dir $fg_dir --out_dir $mix_dir
echo 'classifying images...'
./auto_categorize.sh $mix_dir $class
echo 'calculating accuracies...'
python determine_accuracy.py --input $class --output $accuracy
rm -rf $mix_dir


