import urllib.request
import os
import re

class LibAccess(object):
	#Retrive Seed URL to crawl(Either spidering or content extraction) via constructor method
	#def __init__(self,url):
		#self.url = url
		#self.wget_data = os.popen('wget -qO- %s'% url).read()

	#Downloading webpage content via wget
	def wget(self,url):
		self.wget_data = os.popen('wget -qO- %s'% url).read()
		return self.wget_data

    #Downloading webpage content via curl
	def curl(self):
		url = self.url
		self.curl_data = os.popen('curl -I %s'% url).read()
		return self.curl_data

	#Downlaoding page content using python3 default library urllib
	#To execute this use python3 as branch(python3 jabong_crawler.py)
	def url_lib(self):
		self.urllib_data = urllib.request.urlopen(self.url).read()
		return self.urllib_data

#To retrive all the urls from site(Spidering)
class Spidering(LibAccess):
	def category1(self):
		f1 = open('exampleFile.txt','w')
		spider = self.wget_data
		#print (spider)
		#f1.write(spider)
		if re.search(r'<a href\=\"[^\"]*\"\sid\=\"qa\-main',spider):
		    main_url = re.findall(r'<a href\=\"([^\"]*)\"\sid\=\"qa\-main',spider)
		    for url in main_url:
		    	#pass
			    print (url)
			    f1.write(url+"\n")
		else:
			print ("Match Not Found")
		f1.close()



#To extract the content from product pages with the extracted category urls
#class ContetExtraction(object):		
		

#Creating objects via class
scrap = Spidering()
#Give seed url as parameter as it is compulsary to crawl the webpage
scrap.wget("http://jabong.com")
scrap.category1()
