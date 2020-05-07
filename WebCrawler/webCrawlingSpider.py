# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.crawler import CrawlerRunner
from bs4 import BeautifulSoup
import requests
import threading
from twisted.internet import reactor
import json
import pubSub


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

            # Kill all script and style elements
            for script in soup(["script", "style"]):
                script.decompose()    # Rip it out

            # Extract the normal text and put it into the Document Storage database
            pageText = soup.get_text()
            # print(pageText)

            # Publish extracted text to Classifier in order to check its relevance TO DO

            # Subscribe the crawler to Classifier for return of relevance result
            #TO DO

            # Publish related URLs and extracted text to Document Data
            pubSub.publish('documentData', json.dumps(
                {'url': response.url, 'linkedTo': hyperlinks, 'pageText': pageText}))

            print(response.url)
            # Publish the extracted hyperlinks to URL queue

            # Subscribe the crawler to Classifier for new keywords

            # Publish to Google Search the new keywords

            if(self.number_of_pages_scraped > 10):		# Stopping condition
                raise CloseSpider('Sufficient pages scraped')

            # Creation of new spiders for a url from URL queue through script
            for url in hyperlinks:
                self.number_of_pages_scraped += 1
                yield scrapy.Request(url, self.parse)


def main(message):

    json_data = json.loads(message['data'])
    initialGoogleLinks = []

    for link in json_data:
        link_url = link['url']
        if(link_url.startswith('/url?q=')):
            stop = link_url.find('&')					# Extracting appropriate URLs
            initialGoogleLinks.append(link_url[7:stop])

    runner = CrawlerRunner()

    for link in initialGoogleLinks:
        runner.crawl(WebCrawler, start_urls=[link])

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
