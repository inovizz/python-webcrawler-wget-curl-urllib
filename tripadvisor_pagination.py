import urllib.request
import os
import re
import time
import json

pagination_urls = ["http://www.tripadvisor.in/Hotel_Review-g60898-d86238-Reviews-or10-Sheraton_Atlanta_Hotel-Atlanta_Georgia.html#REVIEWS"]


def wget(url):
	data = os.popen('wget -qO- %s'% url).read()
	if re.search(r'(?ms)<span\sclass\="pageNum\scurrent[^>]*>[^>]*>\s*<a href\=\"[^\"]*\"',data):
		print (re.findall(r'(?ms)<span\sclass\="pageNum\scurrent[^>]*>[^>]*>\s*<a href\=\"([^\"]*)\"',data)[0])
		match = re.findall(r'(?ms)<span\sclass\="pageNum\scurrent[^>]*>[^>]*>\s*<a href\=\"([^\"]*)\"',data)[0]
		match1 = re.sub(r"^","http://www.tripadvisor.com",match)
		data1.append(match1)
	return data


data1 = []
data2 = wget(pagination_urls[0])
if re.search(r'<span class\=\"separator\">\&hellip\;',data2):
	print("hi")	
	print (data1[0])
if re.search(r'<span class\=\"separator\">\&hellip\;',data2):
	for urls in data1:
		wget(urls)
		


