import webCrawlingSpider as wcs
import pubSub
import threading
import json

def callbackURLQueue(message):
	wcs.main(message)

def callbackRelevance(message):
	json_data = json.loads(message['data'])
	# Publish related URLs and extracted text to Document Data
	print(type(json_data['classify']))
	if(bool(json_data['classify']) == True):
		print("HELLOOOOOOOOOOO")
		pubSub.publish('documentData', json.dumps(
				{'url': json_data['url'], 'linkedTo': json_data['linkedTo'], 'document': json_data['document'], 'similarity': json_data['similarity'], 'query': json_data['query']}))

# def relevanceSubscribe():
# 	pubSub.subscribe('classificationResult', callbackRelevance)

# def urlQueueSubscribe():
# 	pubSub.subscribe('urlQueue', callbackURLQueue)

if __name__ == '__main__':	

	pubSub.subscribe1('classificationResult', callbackRelevance)
	pubSub.subscribe2('urlQueue', callbackURLQueue)

	# t = threading.Thread(target = urlQueueSubscribe)
	# t.start()
	# # Subscribe the crawler to Classifier for return of relevance result
	# t = threading.Thread(target = relevanceSubscribe)
	# t.start()
	print("Subscribed to URL Queue and Classifier")
