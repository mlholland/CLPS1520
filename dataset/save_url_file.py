import urllib
import sys

import pdb





with open(sys.argv[1], 'r') as rfile:
	l = rfile.readline()

	count = 0;

	while l != "":

		img = urllib.urlretrieve(l, "img" + str(count) + ".png")
		count += 1

		l = file.readline()