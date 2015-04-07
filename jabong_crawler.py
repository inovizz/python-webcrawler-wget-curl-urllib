import urllib.request
import os
import re
import time

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
	def category1(self,sleep):
		f1 = open('category_urls.txt','w')
		spider = self.wget_data
		if re.search(r'<a href\=\"[^\"]*\"\sid\=\"qa\-main',spider):
			main_url = re.findall(r'<a href\=\"([^\"]*)\"\sid\=\"qa\-main',spider)
			for url in main_url:
				#pass
				print (url)
				f1.write(url+"\n")
		else:
			print ("Match Not Found")
		time.sleep(sleep)
		f1.close()

	#Jabong has all category urls via AJAX call this function will extract all category urls
	def ajaxCategories(self,sleep):
		f1 = open('category_urls.txt','a')
		ajaxURL = "http://www.jabong.com/index/topnav/?e_100"
		scrap.wget(ajaxURL)
		spider = self.wget_data
		if re.search(r'topnav\-title\\"\><a href\=\\\"[^\"]*\"',spider):
			main_url = re.findall(r'topnav\-title\\"\><a href\=\\\"([^\"]*)\"',spider)
			main_url = re.findall(r'<a href\=\\\"([^\"]*)\"\>',spider)
			#re.sub(r"\\","",main_url)
			for url in main_url:
				#pass
				#url = "r%s"%url
				url = re.sub(r"\\","",url)
				if url in "^http":
					f1.write(url+"\n")
				else:
					url = re.sub(r"^","http://www.jabong.com",url)
					f1.write(url+"\n")
				#url = re.sub(r"^","http://www.jabong.com",url)
				print (url)
		else:
			print ("Match Not Found")
		time.sleep(sleep)
		f1.close()

	def pagination(self,sleep):
		f1 = open('pagination_urls.txt','w')
		ajaxURL = "http://www.jabong.com/index/topnav/?e_100"
		scrap.wget(ajaxURL)
		spider = self.wget_data
		if re.search(r'topnav\-title\\"\><a href\=\\\"[^\"]*\"',spider):
			main_url = re.findall(r'topnav\-title\\"\><a href\=\\\"([^\"]*)\"',spider)
			main_url = re.findall(r'<a href\=\\\"([^\"]*)\"\>',spider)
			#re.sub(r"\\","",main_url)
		for url in main_url:
			#pass
			#url = "r%s"%url
			url = re.sub(r"\\","",url)
			if re.search(r'^http',url):
				f1.write(url+"\n")
			else:
				url = re.sub(r"^","http://www.jabong.com",url)
				f1.write(url+"\n")
				#url = re.sub(r"^","http://www.jabong.com",url)
			print (url)
		else:
			print ("Match Not Found")
		time.sleep(sleep)
		f1.close()

	def product(self,sleep):
		f1 = open('category_urls.txt','r')
		f2 = open('product_urls.txt','a')
		for categoryurls in f1:
			ajaxURL = categoryurls
			scrap.wget(ajaxURL)
			spider = self.wget_data
			if re.search(r'unbxdparam\_sku\=\"[^\"]+\"\s*href\=\"[^\"]*\"',spider):
				main_url = re.findall(r'unbxdparam\_sku\=\"[^\"]+\"\s*href\=\"([^\"]*)\"',spider)
				#re.sub(r"\\","",main_url)
				for url in main_url:
					#pass
					#url = "r%s"%url
					url = re.sub(r"\\","",url)
					if re.search(r'^http',url):
						f2.write(url+"\n")
					else:
						url = re.sub(r"^","http://www.jabong.com",url)
						f2.write(url+"\n")
					#url = re.sub(r"^","http://www.jabong.com",url)
					print (url)
			else:
				print ("Match Not Found")
			time.sleep(sleep)


#To extract the content from product pages with the extracted category urls
#class ContetExtraction(object):		
		

#sleep time
sleep = 10
#Creating objects via class
scrap = Spidering()
#Give seed url as parameter as it is compulsary to crawl the webpage
scrap.wget("http://jabong.com")
scrap.category1(sleep)
scrap.ajaxCategories(sleep)
scrap.product(sleep)
