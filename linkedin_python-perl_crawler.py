import os
import time
import re
from multiprocessing.pool import Pool
import requests
import subprocess
import json

#pipe1 = subprocess.Popen(["perl","./perl_linkedin.pl","{0}".format(test_comb)],stdout=subprocess.PIPE)
#		pipe1 = pipe1.stdout.read()
#		pipe1 = str(pipe1)

def wget_cookie(url):
	data = os.popen('wget -qO- --no-cookies --header "Cookie: JSESSIONID="ajax:0605833331634091728"" %s'% url).read()
	print data

def wget_sepcial(url):
	pipe1 = subprocess.Popen(["perl","./perl_linkedin.pl","{0}".format(url)],stdout=subprocess.PIPE)
	pipe1 = pipe1.stdout.read()
	data = str(pipe1)
	return data

def urlLib(url):
	
	user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
	headers = {'User-Agent': user_agent}
	data = requests.get(url,headers = headers,verify=False)
	return data.text.encode('utf-8')

def curll(url):
	data = os.popen("curl --silent 'https://www.linkedin.com/uas/login-submit' -H 'origin: https://www.linkedin.com' -H 'accept-encoding: gzip, deflate' -H 'accept-language: en-US,en;q=0.8' -H 'x-requested-with: XMLHttpRequest' -H 'x-isajaxform: 1' -H 'cookie: bcookie='v=2&7f91dd6c-278b-4e93-87f1-622a57d97e92'; bscookie='v=1&20151013061554015e679e-4487-464f-86c2-c8c323a077c5AQHjFZgs79k5SZChmRdUk0XCgijrAAOV'; visit='v=1&M'; oz_props_fetch_size1_193758893=15; wutan=tvlszlZDlODMoh1G1rrLtWrcLwihO83BnAn6RDSdALo=; L1c=5896cb41; share_setting=PUBLIC; sdsc=1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D; L1e=203e6005; _ga=GA1.2.1232760116.1450865086; JSESSIONID='ajax:0748663782374868679'; _lipt=0_2YjFSU-XJh6E6IbH00m7WzVXq9GEUo6L3wYSIM9FUbACvmOmJgO1bGOSVt3_o1dh1pwmKBYoi_6sfv0TyNtmK98IQccPcuqowv0kpbFz2Zt4iCY8Z31xYpcoEN4glL6B9LWi1pxWj_ZXlBMghN5ZnLetMzlQtjx6vvIzA9nVpie_VpLjU0aXGqFPIcCB2p1HSjbxp0XtIQM-2GpgwGDa8dTvVgwLzPZWII-nYg1L4lFK4bBSAXJWMv2GdNIJ3cs9lJREomR_d_RANFA2GIPsEG1w_WDdnsb19pfXLZr064k9XFRRHcMOAWgCJdx2a9bMAeu_oAF8KPmy9UptWfJ8We3vR8UgHCW7Bq4WXtmX1d4AQdaHRyGS5OeGTKQcOIWsLYv7VDnh5BM7AxDv--_13rjljVvHySl7b3DECcjvCKDAyQgICLI3_-T2MpYSFaJCv-sOLq9nBkE27dEcmPH5-j; lidc='b=LGST05:g=7:u=1:i=1451834017:t=1451920417:s=AQFB_fF_pBs3ic9hrhrVHPjzr6VZC2bP'; RT=s=1451835604499&r=https%3A%2F%2Fwww.linkedin.com%2Fuas%2Flogin; leo_auth_token='GST:9OKeWcqZEwyJ-F1uakKe22eNip-vv5J5FiAsqpqZgyGv-FOFA5nFpV:1451835652:ed6a87368dc37f738eca21d52df3b3824322ed1a'; lang='v=2&lang=en-us' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded' -H 'accept: */*' -H 'referer: https://www.linkedin.com/uas/login' -H 'x-linkedin-tracedatacontext: X-LI-ORIGIN-UUID=FyDjKcr0JRSAyUpq+ioAAA==' --data 'isJsEnabled=true&source_app=&tryCount=&clickedSuggestion=false&session_key=moun_india%40yahoo.co.in&session_password=hanuman&signin=Sign%20In&session_redirect=&trk=&loginCsrfParam=7f91dd6c-278b-4e93-87f1-622a57d97e92&fromEmail=&csrfToken=ajax%3A0748663782374868679&sourceAlias=0_7r5yezRXCiA_H0CRD8sf6DhOjTKUNps5xGTqeX8EEoi&client_ts=1451835663189&client_r=moun_india%40yahoo.co.in%3A618389639%3A107166812%3A544493709&client_output=-745498753&client_n=618389639%3A107166812%3A544493709&client_v=1.0.1' 2>/dev/null")

def linkedinData(url):
	f3 = open('product_information_preety.txt','a')
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
	url = re.sub(r"[\n]*","",url)
	url = re.sub(r"\&","\&",url)
	data = wget_sepcial(url)
	data = str(data)
	f2 = open("data.html","w")
	f2.write(data)
	results_hash["url"] = url
	if re.search(r'locality\"\>\<a\shref\=\"[^\=]*\=(us)',data):
		if re.search(r'full\-name\"\sdir\=\"auto\"\>([^<]*)<',data):
			name = re.findall(r'full\-name\"\sdir\=\"auto\"\>([^<]*)<',data)[0]
			name = re.sub(r"<[^>]*>","",name)
			results_hash["name"] = name

		if re.search(r'<img\ssrc\=\'([^\']*)\'\swidth=\"2',data):
			images = re.findall(r'<img\ssrc\=\'([^\']*)\'\swidth=\"2',data)[0]
			images = re.sub(r"<[^>]*>","",images)
			results_hash["images"] = images

		if re.search(r'title\"\sdir\=\"ltr\"\>([^<]*)<',data):
			headline = re.findall(r'title\"\sdir\=\"ltr\"\>([^<]*)<',data)[0]
			headline = re.sub(r"<[^>]*>","",headline)
			results_hash["headline"] = headline

		if re.search(r'location\'\sti[^>]*>([^<]*)<',data):
			location = re.findall(r'location\'\sti[^>]*>([^<]*)<',data)[0]
			location = re.sub(r"<[^>]*>","",location)
			results_hash["location"] = location

		if re.search(r'description" dir="ltr">(.*?)<\/div><d',data):
			summary = re.findall(r'description" dir="ltr">(.*?)<\/div><d',data)[0]
			summary = re.sub(r"<[^>]*>","",summary)
			results_hash["summary"] = summary

		if re.search(r'<table summary="Overview[^>]*>(.*?)<\/table',data):
			iter_obj = re.findall(r'<table summary="Overview[^>]*>(.*?)<\/table',data)[0]
			iter_obj = re.findall(r'data\-trk[^>]*>([^<]*)<\/a>.*?<a\s[^>]*>(.*?)<\/ol>',iter_obj)

			for key in iter_obj:
				key1 = key[0]
				key1 = re.sub(r"<[^>]*>","",key1)
				#key1 = re.sub(r"\n","",key1)
				value = key[1]
						#value = re.sub(r"\s*","",value)
				value = re.sub(r"\n","",value)
				value = re.sub(r"<[^>]*>","",value)
				results_hash[key1] = value
	else:
		results_hash["error"] = "Might Not Be An USA Profile OR Some Error"

	print(products)
	f3.write(json.dumps(products,indent=4, sort_keys=True)+"\n")



f1 = ["https://www.linkedin.com/in/amanda-richeson-a7784345","https://www.linkedin.com/in/american-legion-aux-dept-of-alaska-05382771","https://www.linkedin.com/in/american-pressure-washing-26739273","https://www.linkedin.com/in/american-red-cross-health-safety-director-4135a834","https://www.linkedin.com/in/american-society-of-colon-and-rectal-surgeons-71754ba8","https://www.linkedin.com/in/american-solar-fund-63a5a310b","https://www.linkedin.com/in/americas-main-street-writers-50076979","https://www.linkedin.com/in/americasonlineautomall","https://www.linkedin.com/in/americashomerescue","https://www.linkedin.com/in/americasinstantsigns","https://www.linkedin.com/in/americans-for-fair-sentencing-02915670","https://www.linkedin.com/in/americare-physical-therapy-59161a48"]
for url in f1:
	linkedinData(url)