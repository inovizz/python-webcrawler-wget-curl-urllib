import urllib.request
import os

class LibAccess(object):
	#Retrive Seed URL to crawl(Either spidering or content extraction) via constructor method
	def __init__(self,url):
		self.url = url

    #Downloading webpage content via wget
	def wget(self):
		url = self.url
		self.wget_data = os.popen('wget -qO- %s'% url).read()
		return self.wget_data

    #Downlaoding page content using python3 default library urllib
    #To execute this use python3 as branch(python3 jabong_crawler.py)
	def url_lib(self):
		self.urllib_data = urllib.request.urlopen(self.url).read()
		return self.urllib_data
		

#Creating objects via class
scrap = LibAccess("http://jabong.com")#Give seed url as parameter as it is compulsary to crawl the webpage
print(scrap.wget())
