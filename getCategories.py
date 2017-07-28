import csv

categories = set()
data = csv.reader(open('rawData.csv','r'))
for line in data:
	for item in line[5:]:
		categories.add(item)

target = open('categories.txt','w')
for item in categories:
	target.write(item)
	target.write('\n')