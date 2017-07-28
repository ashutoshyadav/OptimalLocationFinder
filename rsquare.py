import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
import csv
import pickle

def Rsquare(model,x,y):
	den = []
	num = float(0)
	for i in xrange(len(y)):
		try:
			num+=(model.predict(y[i])-x[i])**2
			den.append(x[i])
		except:
			continue
	m = np.mean(np.array(den))
	d = float(0)
	for item in den:
		d+=(item-m)**2
	RSquare = 1 - (num/d)
	return RSquare[0]

def RMSE(model,x,y):
	temp = Rsquare(model,x,y)
	return 1-temp

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
	RSqaure = Rsquare(model,x,y)
	print "RSqaure: "+str(RSqaure)
	print "RMSE: "+str(RMSE(model,x,y))

if __name__=="__main__":
	main()