#!/bin/python

'''
Given an input and output file, read the input as a CSV of (image filename, classification)
pairs, and record the accuracy into the output file. The correct class is assumed to be
the first substring of the image file when split by underscore. 

Usage example: python determine_accuracy.py --input ../dataset/classifications.csv --output ../dataset/accuracy.txt
'''

import argparse
import csv
from  collections import defaultdict as dd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help='Input csv file (should be output of classify_inputs.m) to get classification results from.') 
    parser.add_argument("--output", type=str, help='Output txt file to store accuracy in.')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        reader = csv.reader(f, quotechar='"')
        right = dd(int)
        total = dd(int)
        for line in reader:
            classification = line[0].split('_')[0]            
            if classification == '2':
                class_1 = line[0].split('_')[1]
                class_2 = line[0].split('_')[3]
                if class_1 in line[1]:  
                    right[class_1] += 1
                if class_2 in line[1]:
                    right[class_2] += 1
                total[class_1] += 1
                total[class_2] += 1
            else:
                if classification in line[1]:
                    right[classification] += 1
                total[classification] += 1
    with open(args.output, 'w') as f:
        for key in total.keys():
            f.write("%s, %f, %d, %d\n" % (key, 1.0 * right[key] / total[key], right[key], total[key]))





if __name__ == '__main__':
    main()
