import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
import csv
import pickle

def MAE(model,x,y):
	den = []
	num = float(0)
	for i in xrange(len(y)):
		try:
			num+=abs(model.predict(y[i])-x[i])
			den.append(x[i])
		except:
			continue
	m = np.mean(np.array(den))
	mae = num/(len(den)*m)
	return mae[0]

def main():
	print 'Working. Please wait!'
	model = pickle.load(open('LinearRegression.sav','rb'))
	data = csv.reader(open('trainingData.csv','r'))
	x = []
	y = []
	for line in data:
		if len(line)==0:
			continue
		x.append(float(line[0]))
		y.append([float(item) for item in line[1:]])
	x = np.array(x)
	y = np.array(y)
	mae = MAE(model,x,y)
	print "Mean Absolute Error: "+str(mae)

if __name__=="__main__":
	main()