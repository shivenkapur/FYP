from textrank import TextRank4Keyword
import json
import pubSub


def callbackURLQueue(message):
    tr4w = TextRank4Keyword()
    json_data = json.loads(message['data'])

    tr4w.analyze(json_data['document'], candidate_pos=[
                 'NOUN', 'PROPN'], window_size=1, lower=False)
    keywords = tr4w.get_keywords(5)

    pubSub.publish('urlKeywords', json.dumps(
        {
            'url': json_data['url'],
            'keywords': keywords
        }
    ))
    print(keywords, json_data['url'])


if __name__ == '__main__':

    pubSub.subscribe('documentData', callbackURLQueue)

    print("Subscribed to documentData")
