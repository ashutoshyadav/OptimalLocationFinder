import csv
import math
from math import cos, asin, sqrt, log

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

def getNeighbours(data,foodCategories):
	lat = data[3]
	lon = data[4]
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


def createNeighbourProfile(neighbourProfile,data,categories,neighbours):
	for n in neighbours:
		for item in n[5:-1]:
			neighbourProfile[categories[item]] = 1

def other(data,neighbours):
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
	print 'Working. Please wait!'
	data = csv.reader(open('rawData.csv','r'))
	target = csv.writer(open('trainingData.csv','w'))
	categories = dict()
	foodCategories = set()
	getCategories(categories)
	getFoodCategories(foodCategories)
	for row in data:
		line = []
		myProfile = []
		for i in xrange(len(categories)):
			myProfile.append(0)
		createMyProfile(myProfile,row[5:],categories)
		neighbourProfile = []
		for i in xrange(len(categories)):
			neighbourProfile.append(0)
		neighbours,foodNeighbours = getNeighbours(row,foodCategories)
		createNeighbourProfile(neighbourProfile,row,categories,neighbours)
		totalCheckins = []
		avgCheckins = []
		foodTotalCheckins = []
		avgFoodCheckins = []
		totalCheckins,avgCheckins = other(row,neighbours)
		foodTotalCheckins,avgFoodCheckins = other(row,foodNeighbours)
		line.append(row[1])
		for item in myProfile:
			line.append(item)
		for item in neighbourProfile:
			line.append(item)
		for item in totalCheckins:
			line.append(item)
		for item in avgCheckins:
			line.append(item)
		for item in foodTotalCheckins:
			line.append(item)
		for item in avgFoodCheckins:
			line.append(item)
		target.writerow(line)
	print 'Completed Successfully!'

if __name__=='__main__':
	main()