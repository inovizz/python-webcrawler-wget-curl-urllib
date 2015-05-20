# python-webcrawler-wget-curl-urllib
Developing python web crawlers(spidering and conent extraction) with Regular Expression

This crawler will visit the home page of ecommerce website and it will extract category and pagination links then it will visit both category and pagination pages and it will extract product links.

Then it will visit the product links which is extracted and it will extract information like Name,Description,Price,Images,Brand,Model,MPN,Availability,Sellers from ecommerce website.

I use wget,curl and urllib to download the page content and from there i use python regex(re) to extract the content and the results will be update to mongo db
