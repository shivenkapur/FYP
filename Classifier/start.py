from textrank import TextRank4Keyword
import textrank

tr4w = TextRank4Keyword()

data = '''Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.

Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.

The best way to prevent and slow down transmission is be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face. 

The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).

At this time, there are no specific vaccines or treatments for COVID-19. However, there are many ongoing clinical trials evaluating potential treatments. WHO will continue to provide updated information as soon as clinical findings become available.

Seek immediate medical attention if you have serious symptoms.  Always call before visiting your doctor or health facility. 

People with mild symptoms who are otherwise healthy should manage their symptoms at home. 

Vanshaj is my name.

On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.'''

tr4w.analyze(data, candidate_pos=[
                 'NOUN', 'PROPN'], window_size=1, lower=False)
keywords = tr4w.get_keywords(5)

query = "Coronavirus symptoms"
query = query.split(' ')
query_terms = []
for term in query:
    query_terms.append(textrank.nlp(term))

docs = []
for word in keywords:
    doc = textrank.nlp(word)
    docs.append(doc)

temp = []
for j in query_terms:
    for i in range(0, len(docs)):
        print(str(j) + "--" + str(docs[i]))
        print(j.similarity(docs[i]))
        temp.append(j.similarity(docs[i]))

print(temp)
