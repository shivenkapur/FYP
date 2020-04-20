# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import requests 

class WebCrawler(scrapy.Spider):
	
	name = 'webCrawler'
	start_urls=[]
	allowed_domains=[]

	def parse(self, response):
		
		if(response.status == 200):
	 		# Extract the hrefs from initial google results
			soup = BeautifulSoup(response.text, 'html.parser')
			
			# Feed them into the URL Queue
			hyperlinks = []

			for link in soup.find_all('a'):
				if(link.get('href') is not None):
					if(link.get('href').startswith('http')):
						hyperlinks.append(link.get('href'))

			print(hyperlinks)

			# Extract the normal text and put it into the Document Storage database
			pageText = soup.get_text()

			print(pageText)

			# Creation of new spiders for a url from URL queue through script
			for url in hyperlinks:
				yield scrapy.Request(url, self.parse)

			# Lacks stopping condition


# Running WebCrawler spider from the script instead of the terminal

response = requests.get('http://www.google.com/search?q=amazon+strengths/')

soup = BeautifulSoup(response.text, 'html.parser')
initialGoogleLinks = []

for link in soup.find_all('a'):
	temp = link.get('href')
	if(temp.startswith('/url?q=')):
		stop = temp.find('&')
		initialGoogleLinks.append(temp[7:stop])

process = CrawlerProcess()		# For multiple spiders

for link in initialGoogleLinks:
	process.crawl(WebCrawler, start_urls = [link])

process.start()

