import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
import csv
import pickle
from math import cos, asin, sqrt, log
import warnings
warnings.filterwarnings('ignore')

RADIUS = 1.0

def getDistance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

def getCategories(categories):
	f = open('categories.txt','r')
	data = f.readlines()
	i = 0
	for line in data:
		categories[line[:-1]] = i
		i+=1

def getFoodCategories(foodCategories):
	f = open('foodCategories.txt','r')
	data = f.readlines()
	i = 0
	for line in data:
		foodCategories.add(line[:-1])

def createMyProfile(myProfile,data,categories):
	for item in data:
		myProfile[categories[item]] = 1

def getNeighbours(lat,lon,foodCategories):
	neighbours = []
	foodNeighbours = []
	places = csv.reader(open('rawData.csv','r'))
	for place in places:
		dist = getDistance(float(lat),float(lon),float(place[3]),float(place[4]))
		if dist<=RADIUS:
			place.append(dist)
			neighbours.append(place)
			for item in place[5:-1]:
				if item in foodCategories:
					foodNeighbours.append(place)
					break
	return neighbours,foodNeighbours

def createNeighbourProfile(neighbourProfile,categories,neighbours):
	for n in neighbours:
		for item in n[5:-1]:
			neighbourProfile[categories[item]] = 1

def other(neighbours):
	totalCheckins = []
	totalCount = []
	for i in xrange(20):
		totalCount.append(0)
		totalCheckins.append(0)
	for n in neighbours:
		temp = float(n[-1])/0.05
		temp = int(temp)
		for i in xrange(temp,20):
			totalCheckins[i]+=int(n[1])
			totalCount[i]+=1
	avgCheckins = []
	for i in xrange(20):
		if totalCount[i]==0:
			avgCheckins.append(0)
		else:
			avgCheckins.append(totalCheckins[i]/totalCount[i])
	for i in xrange(20):
		if totalCheckins[i]==0:
			totalCheckins[i] = 0
		else:
			totalCheckins[i] = log(totalCheckins[i])
		if avgCheckins[i]==0:
			avgCheckins[i] = 0
		else:
			avgCheckins[i] = log(avgCheckins[i])
	return totalCheckins,avgCheckins

def main():
	model = pickle.load(open('model.sav','rb'))
	lon,lat = map(float,raw_input('Enter longitude and latiude:').split())
	foodCategories = set()
	categories = dict()
	getCategories(categories)
	getFoodCategories(foodCategories)
	for i in xrange(len(list(foodCategories))):
		print(i+1),
		print(list(foodCategories)[i])
	temp = map(int,raw_input('Select Category:').split())
	for i in xrange(len(temp)):
		temp[i] = list(foodCategories)[i]
	myProfile = []
	for i in xrange(len(categories)):
		myProfile.append(0)
	createMyProfile(myProfile,temp,categories)
	neighbours,foodNeighbours = getNeighbours(lat,lon,foodCategories)
	neighbourProfile = []
	for i in xrange(len(categories)):
		neighbourProfile.append(0)
	createNeighbourProfile(neighbourProfile,categories,neighbours)
	totalCheckins,avgCheckins = other(neighbours)
	foodTotalCheckins,avgFoodCheckins = other(foodNeighbours)
	row = []
	for item in myProfile:
		row.append(item)
	for item in neighbourProfile:
		row.append(item)
	for item in totalCheckins:
		row.append(item)
	for item in avgCheckins:
		row.append(item)
	for item in foodTotalCheckins:
		row.append(item)
	for item in avgFoodCheckins:
		row.append(item)
	prediction = model.predict(row)
	if prediction<0:
		prediction = 0
	print '-----------------------------------------------------------'
	print 'Predicted Checkins: '+str(prediction)
	print '-----------------------------------------------------------'

if __name__=='__main__':
	main()