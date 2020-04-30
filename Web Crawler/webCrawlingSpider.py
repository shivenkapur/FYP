# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.crawler import CrawlerRunner
from bs4 import BeautifulSoup
import requests
import threading
from twisted.internet import reactor
import json


class WebCrawler(scrapy.Spider):

    name = 'webCrawler'
    start_urls = []
    allowed_domains = []
    number_of_pages_scraped = 0

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

            # print(hyperlinks)

            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.decompose()    # rip it out

            # Extract the normal text and put it into the Document Storage database
            pageText = soup.get_text()

            # Publish extracted text

            print(pageText)

            if(self.number_of_pages_scraped > 100):		# Stopping condition
                raise CloseSpider('Sufficient pages scraped')

            # Creation of new spiders for a url from URL queue through script
            for url in hyperlinks:
                self.number_of_pages_scraped += 1
                yield scrapy.Request(url, self.parse)


def main(message):

	print(message)

	json_data = json.loads(message['data'])

	initialGoogleLinks = []

	for link in json_data:
		link_url = link['url']
		if(link_url.startswith('/url?q=')):
			stop = link_url.find('&')					# Extracting appropriate URLs
			initialGoogleLinks.append(link_url[7:stop])

	# # Running WebCrawler spider from the script instead of the terminal
	# response = requests.get('http://www.google.com/search?q=amazon+strengths/')

	# for link in soup.find_all('a'):
	# 	temp = link.get('href')
	# 	if(temp.startswith('/url?q=')):
	# 		stop = temp.find('&')					# Extracting appropriate URLs
	# 		initialGoogleLinks.append(temp[7:stop])

	runner = CrawlerRunner()

    for link in initialGoogleLinks:
        runner.crawl(WebCrawler, start_urls=[link])

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
