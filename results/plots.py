import numpy as np
import matplotlib.pyplot as plt
import csv
import glob

c_i = {'taxi':0,'shovel':1,'power drill':2,'laptop':3,'toaster':4,'flamingo':5,'tarantula':6,'hammer':7,'hummingbird':8}
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
				y_all[c_i[row[0]]][scale_index] = row[1]
	for i,y in enumerate(y_all):
		plt.plot(x,y, label = i_c[i])
	plt.xlabel('Foreground Scale')
	plt.ylabel('Classification Accuracy')
	plt.title('Image Scale and Classifaction Accuracy in AlexNet')
	plt.legend()
	plt.show()
scale_plot()


