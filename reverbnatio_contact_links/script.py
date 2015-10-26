from nltk import word_tokenize
import glob
import os, sys
import re
from multiprocessing.pool import Pool 

def wget_sepcial(url):
    data = os.popen('wget  -qO- --header="Accept: text/html" --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"  %s'% url).read()
    return data

def train_data_sets():
	spam_nontkenized =[]

	for f1 in glob.glob('urls/*.txt'):
		fin = open(f1)
		for f in fin:
			f = re.sub(r'\n','',f)
			print f
			spam_nontkenized.append(f)


	#print len(spam_nontkenized)
	get_data(spam_nontkenized)

def get_data(spam_nontkenized):
	nprocs = 1000 # nprocs is the number of processes to run
	ParsePool = Pool(nprocs)
	#ParsePool.map(btl_test,url)
	ParsedURLS = ParsePool.map(crawl_fb_again,spam_nontkenized)

def crawl_fb_again(url):
		#f1 = open('facebook_crawled_urls','r+')
	f2 = open('facebook_crawled_again','a')
	f3 = open('crawled_email1','a')
	f4 = open('crawled_email_ugly','a')
	f5 = open('facebook-crawled_email_ids_report.json','a')
	if re.search(r'^\w',url):
		lin = re.sub(r"\s*","",url)
		#print (lin)
		try:
			#url_lin = re.sub(r'(.*?\/)',r"\1",lin)
			print (url_lin)
			data = wget_sepcial(lin)
			data = str(data)
			print (data)
				#print (data)

			if re.search(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data):
				email = re.findall(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data)
				for fb in email:
					url = re.sub(r'\?.*','',fb)
					if re.search(r'^htt',url):
						fb_cac = re.sub(r'\?.*','',fb)
						fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
						fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
						f2.write(fb_cac+"\n")
						print (fb_cac)
						if re.search(r'^\w',fb_cac):
							try:                                                                                             
								data = wget_sepcial(url)
								data = str(data)
									#print (data)
								

								if re.search(r'(?msi)<a\s*href\=\"([^\"]*\/contact.*?[^\"]*)\"',data):
									ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*\/contact.*?[^\"]*)\"',data)
									if re.search(r'(?ms)^\/',ear[0]):
										ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
										print (ear)
										link_again(ear)
									else:
										print (ear)
										link_again(ear[0])

								if re.search(r'(?msi)<a\s*href\=\"([^\"]*\/about.*?[^\"]*)\"',data):
									ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*\/about.*?[^\"]*)\"',data)
									if re.search(r'(?ms)^\/',ear[0]):
										ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
										print (ear)
										link_again(ear)
									else:
										print (ear[0])
										link_again(ear[0])

							except Exception: 
								pass    

									

			else: 
				print ("not found")
				f5.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")
		except Exception: 
			pass   

	if re.search(r'^\w',url):
		lin = re.sub(r"\s*","",url)
		print (lin)
		try:
			url_lin = re.sub(r'(.*?\/)',r"\1",lin)
			#print (url_lin)
			data = wget_sepcial(lin)
			data = str(data) 
				#print (data)

			if re.search(r'(?msi)<a\s*href\=\"([^\"]*\/contact.*?[^\"]*)\"',data):
				print ("yes")
				ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*\/contact.*?[^\"]*)\"',data)
				#print (ear)
				if re.search(r'(?ms)^\/',ear[0]):
					ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
					print (ear)
					link_again(ear)
				else:
					print (ear)
					link_again(ear[0])

			if re.search(r'(?msi)<a\s*href\=\"([^\"]*\/about.*?[^\"]*)\"',data):
				ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*\/about.*?[^\"]*)\"',data)
				if re.search(r'(?ms)^\/',ear[0]):
					ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
					print (ear)
					link_again(ear)
				else:
					print (ear)
					link_again(ear[0])

		except Exception: 
			pass  

def link_again(url):
	f2 = open('facebook_crawled_again','a')
	f3 = open('crawled_links_for_promolta','a')
	f4 = open('crawled_email_ugly','a')
	f5 = open('facebook-crawled_email_ids_report.json','a')

	if re.search(r'^\w',url):
		lin = re.sub(r"\s*","",url)
		print (lin)
		try:
			data = wget_sepcial(lin)
			data = str(data) 
			if re.search(r'(?mis)form.*?name.*?email.*?textarea',data):
				print "Yes - Found - Link - ********************************************************"+lin
				f3.write(lin+"\n")


		except Exception: 
			pass  



train_data_sets()