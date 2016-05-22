import urllib.request
import os
import re
import time
import json

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
		self.url = url
		#curl --silent '$_' -H 'User-Agent: Mozilla/5.0 (Macintosh; In grep OS X 10.9; rv:24.0) Gecko/20100101 Firefox/24.0' 2>/dev/null
		self.curl_data = os.popen('curl --silent %s -H User-Agent: Mozilla/5.0 (Macintosh; In grep OS X 10.9; rv:24.0) Gecko/20100101 Firefox/24.0 2>/dev/null'% url).read()
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
class ContentExtraction(Spidering):
	
	def product_infomation(self,sleep):
		f1 = open('product_urls.txt','r')
		f2 = open('product_information.txt','a')
		f3 = open('product_information_preety.txt','a')
		
		#xproducts['results']['images'] = [results_hash["images"]]
		#products["results"]["images"] = images_hash
		for producturls in f1:
			products = {}
			results_hash = {}
			results_array = []
			results_array = results_hash
			offers_hash = {}
			results_array = offers_hash
			features_hash = {}
			features_array = {}
			features_hash = features_array
			results_array = features_hash
			variations_hash = {}
			variations_hash["size"] = []
		#results_array = images_hash
			products["results"] = results_hash
			products["results"]["offers"] = offers_hash
			products["results"]["features"] = features_hash
			products["results"]["images"] = []
			products["results"]["variations"] = variations_hash
			ajaxURL = producturls
			scrap.wget(ajaxURL)
			spider = self.wget_data
			if re.search(r'itemprop\=\"name\">',spider):
				if re.search(r'itemprop="name">\s*[^<]*\s*<\/span',spider):
					results_hash["name"] = re.findall(r'itemprop="name">\s*([^<]*)\s*<\/span',spider)[0]
				if re.search(r'itemprop="brand">\s*[^<]*\s*<\/span',spider):
					results_hash["brand"] = re.findall(r'itemprop="brand">\s*([^<]*)\s*<\/span',spider)[0]
				if re.search(r'og\:description\"\scontent\=\"[^\"]*\"',spider):
					results_hash["description"] = re.findall(r'og\:description\"\scontent\=\"([^\"]*)\"',spider)[0]
				if re.search(r'(?ms)ratingCount">[^<]*<',spider):
					results_hash["reviews_number"] = re.findall(r'(?ms)ratingCount">([^<]*)<',spider)[0]
				if re.search(r'(?ms)ratingValue">[^<]*<',spider):
					results_hash["siterating"] = re.findall(r'(?ms)ratingValue">([^<]*)<',spider)[0]
					results_hash["siterating_scale"] = "5"
				if re.search(r'striked\-price[^>]*>[\w\.]*\s*[\d\.]+',spider):
					results_hash["list_price"] = re.findall(r'striked\-price[^>]*>[\w\.]*\s*([\d\.]+)',spider)[0]
					results_hash["listprice_currency"] = "MRP"
				if re.search(r'itemprop="price">\s*[^<]*<',spider):
					offers_hash["price"] = re.findall(r'itemprop="price">\s*([^<]*)<',spider)[0]
					offers_hash["currency"] = "MRP" 
				if re.search(r'availability"\shref\=\"[^\.]*\.org\/[^\"]*\"',spider):
					offers_hash["availability"] = re.findall(r'availability"\shref\=\"[^\.]*\.org\/([^\"]*)\"',spider)[0]
				offers_hash["seller"] = "Jabong"
				if re.search(r'(?ms)breadcrumbs\smb8\"\>.*?<\/div',spider):
					crumb = re.findall(r'(?ms)breadcrumbs\smb8\"\>(.*?)<\/div',spider)[0]
					crumb = re.sub(r"<a [^>]*>","",crumb)
					crumb = re.sub(r"<span [^>]*>","",crumb)
					crumb = re.sub(r"<[^>]*>","",crumb)
					crumb = re.sub(r"\n*","",crumb)
					crumb = re.sub(r"\s*","",crumb)
					results_hash["crumb"] = crumb
				results_hash["url"] = ajaxURL
				if re.search(r'(?s)c999 fs12 mt10 f-bold">.*?<\/table',spider):
					features = re.findall(r'(?s)c999 fs12 mt10 f-bold">(.*?)<\/table',spider)[0]
					features = re.findall(r'<td[^>]*>([^<]*)<\/td>\s*<td[^>]*>([^<]*)<\/td',features)
					for key in features:
						key1 = key[0]
						#key1 = re.sub(r"\s*","",key1)
						key1 = re.sub(r"\n","",key1)
						value = key[1]
						#value = re.sub(r"\s*","",value)
						value = re.sub(r"\n","",value)
						features_hash[key1] = value
				if re.search(r'(?ms)<ul id="listProductSizes.*?<\/ul',spider):
					variations = re.findall(r'(?ms)<ul id="listProductSizes(.*?)<\/ul',spider)[0]
					variations_hash["size"] = re.findall(r'(?ms)sizeAvailable\'\,\s\'([^\']*)\'',variations)
					#for key in variations:
					#	if len(key) > 0:
					#		key = ''.join(key)
					#		variations_hash["size"].append(('size',key))
					#	else:
					#		key = ''.join(key)
					#		variations_hash["size"].append(('size',"NONE"))

					#loop = variations_hash["si"]
					#for l in loop:
					#	key = l[0]
					#	value = l[1]
					#	variations_hash[key] = value
				if re.search(r'data\-image\-big\=\"([^\"]*)\"',spider):
					images = re.findall(r'data\-image\-big\=\"([^\"]*)\"',spider)
					for image in images:
						products['results']['images'].append(image)
					print(products)
					f2.write(json.dumps(products)+"\n")
					f3.write(json.dumps(products,indent=4, sort_keys=True)+"\n")
					
			else:
				print ("Match Not Found")
			time.sleep(sleep)


#sleep time
sleep = 3
#Creating objects via class
scrap = ContentExtraction()
#Give seed url as parameter as it is compulsary to crawl the webpage
scrap.wget("http://jabong.com")
scrap.category1(sleep)
scrap.ajaxCategories(sleep)
scrap.product(sleep)
scrap.product_infomation(sleep)
