#!/bin/bash

#Pulls the files listed in all the text files that exist
# in $1/txt/ and reads each line.
# each line is assumed to be a download link to an image
# of the same class as the text file filename
# saves each image to $1/images/classname_number.png

#hard code txt and class_images
txt_dir="/txt/"
image_dir="/images/"

mkdir "$1$image_dir"
ls "$1$txt_dir" | while read file
do
    echo "$1$txt_dir$file"
    class=`echo "$file" | sed -E "s/(.*)\..*/\1/g"`
    counter=0
    cat "$1$txt_dir$file" | while read line 
    do
	echo "$1$image_dir$class"_"$counter".png
	curl -0 ${line} > "$1$image_dir$class"_"$counter".png
	counter=$((counter+1))
    done
done
#cat $1 | while read line 
#do
#    echo $line
#    curl -0 ${line} > $1
#done
