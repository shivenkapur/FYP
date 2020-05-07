import tensorflow as tf

import tensorflow_hub as hub
import numpy as np
#import pandas as pd
import seaborn as sns

# @param ["https://tfhub.dev/google/universal-sentence-encoder/4", "https://tfhub.dev/google/universal-sentence-encoder-large/5"]
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(module_url)
print("module %s loaded" % module_url)


def embed(input):
    return model(input)


def universalSentenceEncoder(messages_):
    message_embeddings_ = embed(messages_)
    corr = np.inner(message_embeddings_, message_embeddings_)
    return corr[0][1]

