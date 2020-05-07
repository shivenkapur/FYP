from universalSentenceEncoder import universalSentenceEncoder
import json
import pubSub


def callbackURLQueue(message):
    print(message)
    json_data = json.loads(message["data"])
    sentences = [json_data["query"], json_data["document"]]

    similarity = universalSentenceEncoder(sentences)

    passed = False

    print("Similarity: " + str(similarity))
    if similarity > 0.2:
        passed = True

    pubSub.publish('classificationResult', json.dumps(
        {
            "url": json_data["url"],
            "document": json_data["document"],
            "linkedTo": json_data["linkedTo"],
            "classify": passed,
            "similarity": str(similarity),
            "query": json_data["query"]
        }
    ))
    print(json_data["url"], passed)


if __name__ == '__main__':

    pubSub.subscribe('classifyDocument', callbackURLQueue)
    print("Subscribed to Classify Document")

    # pubSub.publish('classifyDocument', json.dumps(
    #     {
    #         "query": "Node.js",
    #         "document": "As an asynchronous event-driven JavaScript runtime,",
    #         "url": "asdasd"
    #     }
    # ))

    # pubSub.publish('classifyDocument', json.dumps(
    #     {
    #         "query": "Corona",
    #         "document": "As an asynchronous event-driven JavaScript runtime,",
    #         "url": "asdasd"
    #     }
    # ))
