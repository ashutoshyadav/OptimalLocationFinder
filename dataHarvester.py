import facebook as fb
import csv
import urllib2 as url
import json
import time

access_token = 'EAACEdEose0cBAAAmrjZBBeZBpkNz2kQ59KsMXI6OX9Mjd8ZCoHLnifUJr1LLl9WDggovGrsGcBlTDnevlfHRX0ytSRcxe9KGJu8TaUZA9a0MtLVLnOtAaqGx37230X2N5TQdqsqiRtKyzA0FwLJ99UAKRwSwFqwGYQjPr0o3ZAwZDZD'
graph = None
categories = ['Airport','Arts Entertainment','Attractions/Things to Do','Bank/Financial Service','Bar','Bookshop','Business Service','Cinema','Club','Community Government','Concert Venue','DIY','Doctor','Event Planner','Food Shop','Hospital/Clinic','Hotel','Landmark','Lawyer','Library','Licensed Financial Representative','Local Business','Medical Health','Middle School','Museum/Art Gallery','Outdoor Gear/Sporting Goods','Pet Services','Professional Service','Property','Public Places','Public Transport Stop','Religious Organisation','Restaurant/Cafe','School','Shopping/Retail','Spas/Beauty/Personal Care','Sports Recreation','Sports Venue Stadium','Tours Sightseeing','Train Station','Transport','University','Vehicles','Aerospace/Defence','Bank/Financial Institution','Biotechnology','Cargo Freight Company','Cars and Parts','Cause','Chemicals','Community Organisation','Company','Computers/Technology','Consulting/Business Service','Education','Energy','Engineering/Construction','Farming/Agriculture','Food/Beverages','Government Organisation','Health/Beauty','Health/Medical/Pharmaceuticals','Industrials','Insurance Company','Internet/Software','Legal/Law','Media/News/Publishing','Middle School','Mining/Materials','Non-governmental Organisation (NGO)','Non-profit Organisation','Organisation','Political Organisation','Political Party','Preschool','Primary School','Religious Organisation','Retail and Consumer Merchandise','School','Small Business','Telecommunication','Tobacco','Travel/Leisure','University','App Page','Appliances','Baby Goods/Kids Goods','Bags/Luggage','Board Game','Building Materials','Camera/Photo','Cars','Clothing','Commercial Equipment','Computers','Electronics','Food/Beverages','Furniture','Games/Toys','Health/Beauty','Home Decor','Household Supplies','Jewellery/Watches','Kitchen/Cooking','Medications','Office Supplies','Patio/Garden','Pet Supplies','Phone/Tablet','Product/Service','Software','Tools/Equipment','Video Game','Vitamins/Supplements','Website','Wine/Spirits','Actor/Director','Artist','Author','Blogger','Business Person','Chef','Coach','Comedian','Dancer','Designer','Entertainer','Entrepreneur','Fictional Character','Film Character','Government Official','Journalist','Musician/Band','News Personality','Pet','Photographer','Politician','Producer','Public Figure','Scientist','Sportsperson','Teacher','Writer','Album','Amateur Sports Team','Book','Book Series','Bookshop','Cinema','Concert Tour','Concert Venue','Fictional Character','Film','Film Television Studio','Film Character','Library','Magazine','Music Award','Music Chart','Music Video','Performance Art','Podcast','Radio Station','Record Label','School Sports Team','Song','Sports League','Sports Team','Sports Venue Stadium','Theatrical Play','TV Channel','TV Network','TV Programme','TV/Film Award']
sleepTime = 30

def performQuery(query,target):
	global graph
	global access_token
	global sleepTime
	f = csv.writer(open(target,'w'))
	data = graph.get_object(query)
	print ''
	print query	
	print ''
	for line in data['data']:
		row = []
		flag = True
		while flag:
			try:
				print 'fetching url'
				page = url.urlopen('https://graph.facebook.com/'+str(line['id'])+'?access_token='+access_token)
				page = page.read()
				flag = False
			except:
				print ''
				print 'Error in opening url'
				print 'Goint to sleep'
				time.sleep(sleepTime)
		try:
			print 'loading data'
			page = json.loads(page)
		except:
			continue
		try:
			print 'creating row'
			row.append(page['name'].encode())
			row.append(page['checkins'])
			row.append(page['likes'])
			row.append(page['location']['latitude'])
			row.append(page['location']['longitude'])
			row.append(page['category'].encode())
			for t in page['category_list']:
				row.append(t['name'].encode())
			print row
			f.writerow(row)	
		except:
			print 'Location parameter not available. Skipping!'
			continue				

def main():
	global access_token,graph
	graph = fb.GraphAPI(access_token)
	print 'Working. Please wait!'
	for i in xrange(127,len(categories)):
		target = 'bangalore'+str(i)+'.csv'
		i+=1
		query='/search?q=bangalore '+str(categories[i])+'&type=page'
		performQuery(query,target)
	

 
if __name__=='__main__':
	main()