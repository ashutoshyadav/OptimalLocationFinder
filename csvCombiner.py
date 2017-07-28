import csv

target = csv.writer(open('rawData.csv','w'))
for i in xrange(180):
	source = 'bangalore'+str(i)+'.csv'
	source = csv.reader(open(source,'r'))
	for line in source:
		target.writerow(line)