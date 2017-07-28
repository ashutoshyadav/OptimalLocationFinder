import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
import csv
import pickle
import rsquare
import mae

models = ['DecisionTreeUsingEntropy.sav','DecisionTreeUsingGini.sav','GradientBoosting.sav','KNNNeighbours.sav','LinearRegression.sav','LogisticRegression.sav','RandomForest.sav']

def compare(x,y):
	print 'Working Please Wait!'
	print 'Model\tMAE\tRMSE\tR^2'
	for m in models:
		model = pickle.load(open(m,'rb'))
		print str(m)+'\t'+str(mae.MAE(model,x,y))+'\t'+str(rsquare.RMSE(model,x,y))+'\t'+str(rsquare.Rsquare(model,x,y))


def main():
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
	compare(x,y)

if __name__=='__main__':
	main()