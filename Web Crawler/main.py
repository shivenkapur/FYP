import webCrawlingSpider as wcs
import pubSub

def callbackURLQueue(message):
	wcs.main(message)

if __name__ == '__main__':	

	pubSub.subscribe('urlQueue', callbackURLQueue)
	#pubSub.publish('urlQueue', 'Published to UrlQueue')
	print("Subscribe 2:")
	# pubSub.publish('urlQueue', 'Hello')