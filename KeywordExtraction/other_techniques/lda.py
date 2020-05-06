from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import os
from gensim.models.wrappers import LdaMallet
from gensim.test.utils import common_corpus, common_dictionary
import time
from gensim import corpora, similarities, models

print(time.localtime())


print(time.localtime())


def createCorpus():
    corpusdir = 'textfiles/'  # Directory of corpus.
    newcorpus = PlaintextCorpusReader(corpusdir, '.*')
    return newcorpus


# You should update this path as per the path of Mallet directory on your system.

# You should update this path as per the path of Mallet directory on your system.

tokenize = []
with open('./textfiles/COVID-sample.txt', 'r') as f:
    for line in f:
        for word in line.split():
            tokenize.append(word)
final_text = [
    tokenize
]

mallet_path = "/Users/anujkapur/Downloads/mallet-2.0.8/bin/mallet"
print(final_text)

print(time.localtime())
dictionary = corpora.Dictionary(final_text)
corpus = [dictionary.doc2bow(text) for text in final_text]

model = LdaMallet(mallet_path, corpus=corpus,
                  num_topics=5, id2word=dictionary)
print(time.localtime())
print(model)
