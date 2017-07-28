import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
import csv
import pickle

def main():
	print 'Working! Please Wait.'
	data = csv.reader(open('trainingData.csv','r'))
	x = []
	y = []
	for line in data:
		if(len(line)==0):
			continue
		x.append(float(line[0]))
	plt.plot(x)
	plt.show()

if __name__=="__main__":
	main()