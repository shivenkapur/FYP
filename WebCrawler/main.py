import webCrawlingSpider as wcs
import pubSub
import threading
import json

def callbackURLQueue(message):
	wcs.main(message)

if __name__ == '__main__':	

	pubSub.subscribe('urlQueue', callbackURLQueue)
	print("Subscribed to URL Queue")
