#!/bin/bash

#usage:./auto_categorize.sh input_dir output_file
#runs our categorization function (in matlab) on a directory of inputted images
#saves results to inputed result filename
#also loads modules first


module load matlab/R2015b
module load matconvnet
matlab -nodesktop -r "vl_setupnn; classify_inputs('$1','$2'); quit;"
