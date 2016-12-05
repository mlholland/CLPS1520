#!/bin/bash

#Pulls the files listed in all the text files that exist
# in $1/txt/ and reads each line.
# each line is assumed to be a download link to an image
# of the same class as the text file filename
# saves each image to $1/images/classname_number.png

#hard code txt and class_images
txt_dir="/txt/"
image_dir="/images/"
all_dir="/all/"


mkdir "$1$image_dir"
mkdir "$1$image_dir$all_dir"
ls "$1$txt_dir" | while read file
do
    echo "$1$txt_dir$file"
    class=`echo "$file" | sed -E "s/(.*)\..*/\1/g"`
    counter=0
    mkdir "$1$image_dir$class"/
    cat "$1$txt_dir$file" | while read line 
    do
	echo "$1$image_dir$class"/"$class"_"$counter".png
	curl -0 ${line} > "$1$image_dir$class"/"$class"_"$counter".png
	ln "$1$image_dir$class"/"$class"_"$counter".png "$1$image_dir$all_dir$class"_"$counter".png 
	counter=$((counter+1))
    done
done
#cat $1 | while read line 
#do
#    echo $line
#    curl -0 ${line} > $1
#done
