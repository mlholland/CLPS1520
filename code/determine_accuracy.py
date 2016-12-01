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
        reader = csv.reader(f)
        right = dd(int)
        total = dd(int)
        for line in reader:
            class = line[0].split('_')[0]
            if class == line[1]:
                right[class] += 1
            total[class] += 1
    with open(args.output, 'w') as f:
        for key in total.keys():
            f.writeline("%s, %f, %d, %d" % (key, 1.0 * right[class] / total[class], right[class], total[class]))





if __name__ == '__main__':
    main()
