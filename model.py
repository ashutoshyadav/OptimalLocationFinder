import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import datasets
from sklearn import linear_model
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
import csv
import pickle

print 'Working. Please wait!'
data = csv.reader(open('trainingData.csv','r'))
x = []
y = []
for line in data:
	if len(line)==0:
		continue
	x.append(float(line[0]))
	y.append([float(item) for item in line[1:]])
xTrain = []
yTrain = []
for i in xrange(len(y)):
	if(len(y[i])==1460):
		xTrain.append(x[i])
		yTrain.append(y[i])
xTrain = np.array(xTrain)
yTrain = np.array(yTrain)
print 'Model fitting'

# Linear Regression
# legr = linear_model.LinearRegression()
# legr.fit(yTrain,xTrain)
# pickle.dump(legr,open('LinearRegression.sav','wb'))


# Logistic Regression
# logr = linear_model.LogisticRegression()
# logr.fit(yTrain,xTrain)
# pickle.dump(logr,open('LogisticRegression.sav','wb'))	 


# Decision Tree
# dtree = tree.DecisionTreeClassifier(criterion='gini')
# dtree.fit(yTrain,xTrain)
# pickle.dump(dtree,open('DecisionTreeUsingGini.sav','wb'))

# dtree = tree.DecisionTreeClassifier(criterion='entropy')
# dtree.fit(yTrain,xTrain)
# pickle.dump(dtree,open('DecisionTreeUsingEntropy.sav','wb'))


# KNN Neighbours
# model = KNeighborsClassifier(n_neighbors=6)
# model.fit(yTrain,xTrain)
# pickle.dump(model,open('KNNNeighbours.sav','wb'))


# Random Forest
# model= RandomForestClassifier()
# model.fit(yTrain,xTrain)
# pickle.dump(model,open('RandomForest.sav','wb'))


# Gradient Boosting
# params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,
#           'learning_rate': 0.05, 'loss': 'ls'}
# clf = ensemble.GradientBoostingRegressor(**params)
# clf.fit(yTrain, xTrain)
# pickle.dump(clf,open('GradientBoosting.sav','wb'))

# Neural Network
model = MLPRegressor(hidden_layer_sizes=(1460,))
model.fit(yTrain,xTrain);
pickle.dump(model,open('NeuralNetwork.sav','wb'))

print 'Completed Successfully!'