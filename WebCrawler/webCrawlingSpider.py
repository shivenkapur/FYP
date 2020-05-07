import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.crawler import CrawlerRunner
from bs4 import BeautifulSoup
import requests
import threading
from twisted.internet import reactor
import json
import pubSub
from universalSentenceEncoder import universalSentenceEncoder


class WebCrawler(scrapy.Spider):

    name = 'webCrawler'
    start_urls = []
    allowed_domains = []
    number_of_pages_scraped = 0

    # def callbackRelevance(message):
    #     json_data = json.loads(message['data'])
    #     # Publish related URLs and extracted text to Document Data
    #     print(type(json_data['classify']))
    #     if(bool(json_data['classify']) == True):
    #         print("HELLOOOOOOOOOOO")
    #         pubSub.publish('documentData', json.dumps(
    #                 {'url': json_data['url'], 'linkedTo': json_data['linkedTo'], 'document': json_data['document'], 'similarity': json_data['similarity'], 'query': json_data['query']}))

    def similarityCheck(self, query, document):
        similarity = universalSentenceEncoder([query, document])
        print("Similarity: " + str(similarity))
        return similarity

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
            print(response.url)

            similarity = self.similarityCheck('The University of Hong Kong', pageText)
            if(similarity > 0.1):
                pubSub.publish('documentData', json.dumps(
                            {'url': response.url, 'linkedTo': hyperlinks, 'document': pageText, 'similarity': str(similarity), 'query': 'The University of Hong Kong'}))
                for url in hyperlinks:
                    self.number_of_pages_scraped += 1
                    if(self.number_of_pages_scraped > 20):		# Stopping condition
                        raise CloseSpider('Sufficient pages scraped')
                    else:
                        yield scrapy.Request(url, self.parse)
            else:
                raise CloseSpider('Page not relevant')



def main(message):

    # print(message)
    json_data = json.loads(message['data'])
    print(message)

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
    # Send a stopping signal for the subscription of Web Crawler
    pubSub.publish('startClustering', "")
