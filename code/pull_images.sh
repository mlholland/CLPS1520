#!/bin/bash

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