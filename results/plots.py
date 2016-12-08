import numpy as np
import matplotlib.pyplot as plt
import csv
import glob

c_i = {'taxi':0,'shovel':1,'powerdrill':2,'laptop':3,'toaster':4,'flamingo':5,'tarantula':6,'hammer':7,'hummingbird':8}
i_c = {}
for k,v in c_i.iteritems():
	i_c[v] = k

def scale_plot():
	x = np.arange(.1,1,.1).tolist()
	y_all = [[0 for j in range(9)] for i in range(9)]
	for file in glob.iglob('accuracy_all_all_scale*.csv'):
		with open(file, 'rb') as f:
			scale_index = int(file[-6:-4])-1
			reader = csv.reader(f)
			for row in reader:
				if row[0] == 'power drill': row[0] = 'powerdrill' 
				y_all[c_i[row[0]]][scale_index] = row[1]
	plt.figure()
	for i,y in enumerate(y_all):
		plt.plot(x,y, label = i_c[i], lw = 2)
	plt.xlabel('Foreground Scale')
	plt.ylabel('Classification Accuracy')
	plt.title('Image Scale and Classifaction Accuracy in AlexNet')
	plt.legend(loc = 'upper left', bbox_to_anchor=(1,1))

def combos_map():
	z = np.ones((9,9,3))*1;
	for file in glob.iglob('accuracy_2*.csv'):
		with open(file, 'rb') as f:
			reader = csv.reader(f)
			fg = {}
			for i,row in enumerate(reader):
				if row[0] == 'power drill': row[0] = 'powerdrill' 
				fg[c_i[row[0]]] = float(row[1])*15
			if len(fg):
				x = max(fg.keys())
				y = min(fg.keys())
				z[x,y,0] = fg[x]
				z[x,y,1] = 0
				z[x,y,2] = fg[y]
				# if z[x,y,1] == 1:
				# 	z[x,y,0] = fg[x]
				# 	z[x,y,1] = 0
				# 	z[x,y,2] = fg[y]
	plt.figure()
	# plt.xlabel('Foreground Class (Blue)')
	# plt.ylabel('Foreground Class (Red)')
	plt.title('Two Foreground Image Classification Trends')
	plt.imshow(z, interpolation='nearest')

def bg_clutter(filename):
	bg_acc = {}
	acc = []
	clut = []
	#bg_acc = {bg_filename:[# correct,# total,bg_clutter]}
	for file in glob.iglob('accuracy_bybg*[6-9].csv'):
		with open(file, 'rb') as f:
			reader = csv.reader(f)
			for i,row in enumerate(reader):
				key = str(row[0])
				key = key[:key.rindex('.')]
				if key in bg_acc:
					bg_acc[key] = [bg_acc[key][0]+float(row[2]),bg_acc[key][1]+float(row[3]),0]
				else:
					bg_acc[key] = [float(row[2]),float(row[3]),0]
	with open(filename,'rb') as f:
		reader = csv.reader(f)
		for i,row in enumerate(reader):
			key = str(row[0])
			key = key[31:key.rindex('.')]
			bg_acc[key][2] = float(row[1])
		for k,v in bg_acc.iteritems():
			acc.append(v[0]/v[1])
			clut.append(v[2])
	plt.figure()
	plt.title('How Background Clutter Affects AlexNet Accuracy')
	plt.xlabel('Background Clutter')
	plt.ylabel('Classification Accuracy')
	plt.scatter(clut,acc,s=25)



#32

bg_clutter('../backgroundclutters.csv')
#bg_clutter('../backgroundcluttersmax.csv')
combos_map()	
scale_plot()
plt.show()
