import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
from sklearn import neural_network
import csv
import pickle

def train(x,y):
	model = neural_network.MLPRegressor(hidden_layer_sizes=(1460,),activation='logistic')


def main():
	print 'Working! Please Wait.'
	data = csv.reader(open('trainingData.csv','r'))
	x = []
	y = []
	for line in data:
		if(len(line)==0):
			continue
		x.append(float(line[0]))
		y.append([float(item) for item in line[1:]])
	x = np.array(x)
	y = np.array(y)
	for i in xrange(len(y)):
	if(len(y[i])==1460):
		xTrain.append(x[i])
		yTrain.append(y[i])
	


if __name__=="__main__":
	main()