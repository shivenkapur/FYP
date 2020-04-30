import redis

def publish(channel, message):
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    redis_client.publish(channel, message)


def subscribe(channel, callback):
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    pubsub = redis_client.pubsub()
    pubsub.subscribe(**{channel: callback})
    pubsub.run_in_thread(sleep_time=.01)


