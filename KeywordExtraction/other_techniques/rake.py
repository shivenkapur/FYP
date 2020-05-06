import time
print(time.localtime())
import nltk
from rake_nltk import Metric, Rake
from gensim import corpora, similarities, models
from gensim.models.wrappers import LdaMallet
print(time.localtime())
r = Rake()

# r = Rake(ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO)
# r = Rake(ranking_metric=Metric.WORD_DEGREE)
# r = Rake(ranking_metric=Metric.WORD_FREQUENCY)

print(time.localtime())
r.extract_keywords_from_text("""
Coronavirus disease disease caused discovered coronavirus. people infected virus experience illness recover requiring treatment. people problems disease diabetes disease cancer develop illness. way prevent slow transmission. virus disease causes spreads. Protect infection washing hands alcohol based rub touching face. virus spreads droplets saliva discharge nose person coughs sneezes. practice etiquette example coughing elbow. time vaccines treatments COVID-19. trials evaluating treatments. continue provide updated information findings. Seek attention symptoms. visiting doctor health facility. People symptoms manage symptoms home. Vanshaj. takes days infected virus symptoms days.""")

print(r.get_ranked_phrases())
print(time.localtime())