import webCrawlingSpider as wcs
import pubSub


def callbackURLQueue(message):
    wcs.main(message)


# def callbackRelevance(message):

if __name__ == '__main__':	

	pubSub.subscribe('urlQueue', callbackURLQueue)
	# pubSub.subscribe('relevanceOfData', callbackRelevance)
	# pubSub.publish('urlQueue', 'Published to UrlQueue')
	print("Subscribed to URL Queue")
	# pubSub.publish('urlQueue', 'Hello')
