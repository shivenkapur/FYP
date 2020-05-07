import webCrawlingSpider as wcs
import pubSub


def callbackURLQueue(message):
    wcs.main(message)


def callbackRelevance(message):
	json_data = json.loads(message['data'])
	# Publish related URLs and extracted text to Document Data
	if(json_data['classify']):
		pubSub.publish('documentData', json.dumps(
				{'url': message['url'], 'linkedTo': json_data['linkedTo'], 'document': json_data['document'], 'similarity': json_data['similarity'], 'query': json_data['query']}))

if __name__ == '__main__':	

	pubSub.subscribe('urlQueue', callbackURLQueue)
	# Subscribe the crawler to Classifier for return of relevance result
	pubSub.subscribe('classificationResult', callbackRelevance)
	print("Subscribed to URL Queue and Classifier")
