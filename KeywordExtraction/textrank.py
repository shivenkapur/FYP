from spacy.lang.en.stop_words import STOP_WORDS
import spacy
import numpy as np
from collections import OrderedDict
import time

print(time.localtime())

nlp = spacy.load('en_core_web_sm')


class TextRank4Keyword():
    """Extract keywords from text"""

    def __init__(self):
        self.d = 0.85  # damping coefficient, usually is .85
        self.min_diff = 1e-5  # convergence threshold
        self.steps = 3  # iteration steps
        self.node_weight = None  # save keywords and its weight

    def set_stopwords(self, stopwords):
        """Set stop words"""
        for word in STOP_WORDS.union(set(stopwords)):
            lexeme = nlp.vocab[word]
            lexeme.is_stop = True

    def sentence_segment(self, doc, candidate_pos, lower):
        """Store those words only in cadidate_pos"""
        sentences = []
        for sent in doc.sents:
            selected_words = []
            for token in sent:
                # Store words only with cadidate POS tag
                if token.pos_ in candidate_pos and token.is_stop is False:
                    if lower is True:
                        selected_words.append(token.text.lower())
                    else:
                        selected_words.append(token.text)
            sentences.append(selected_words)
        return sentences

    def get_vocab(self, sentences):
        """Get all tokens"""
        vocab = OrderedDict()
        i = 0
        for sentence in sentences:
            for word in sentence:
                if word not in vocab:
                    vocab[word] = i
                    i += 1
        return vocab

    def get_token_pairs(self, window_size, sentences):
        """Build token_pairs from windows in sentences"""
        token_pairs = list()
        for sentence in sentences:
            for i, word in enumerate(sentence):
                for j in range(i+1, i+window_size):
                    if j >= len(sentence):
                        break
                    pair = (word, sentence[j])
                    if pair not in token_pairs:
                        token_pairs.append(pair)
        return token_pairs

    def symmetrize(self, a):
        return a + a.T - np.diag(a.diagonal())

    def get_matrix(self, vocab, token_pairs):
        """Get normalized matrix"""
        # Build matrix
        vocab_size = len(vocab)
        g = np.zeros((vocab_size, vocab_size), dtype='float')
        for word1, word2 in token_pairs:
            i, j = vocab[word1], vocab[word2]
            g[i][j] = 1

        # Get Symmeric matrix
        g = self.symmetrize(g)

        # Normalize matrix by column
        norm = np.sum(g, axis=0)
        # this is ignore the 0 element in norm
        g_norm = np.divide(g, norm, where=norm != 0)

        return g_norm

    def get_keywords(self, number=10):
        """Print top number keywords"""
        node_weight = OrderedDict(
            sorted(self.node_weight.items(), key=lambda t: t[1], reverse=True))
        for i, (key, value) in enumerate(node_weight.items()):
            print(key + ' - ' + str(value))
            if i > number:
                break

    def analyze(self, text,
                candidate_pos=['NOUN', 'PROPN'],
                window_size=4, lower=False, stopwords=list()):
        """Main function to analyze text"""

        # Set stop words
        self.set_stopwords(stopwords)

        # Pare text by spaCy
        doc = nlp(text)

        # Filter sentences
        sentences = self.sentence_segment(
            doc, candidate_pos, lower)  # list of list of words

        # Build vocabulary
        vocab = self.get_vocab(sentences)

        # Get token_pairs from windows
        token_pairs = self.get_token_pairs(window_size, sentences)

        # Get normalized matrix
        g = self.get_matrix(vocab, token_pairs)

        # Initionlization for weight(pagerank value)
        pr = np.array([1] * len(vocab))

        # Iteration
        previous_pr = 0
        for epoch in range(self.steps):
            pr = (1-self.d) + self.d * np.dot(g, pr)
            if abs(previous_pr - sum(pr)) < self.min_diff:
                break
            else:
                previous_pr = sum(pr)

        # Get weight for each node
        node_weight = dict()
        for word, index in vocab.items():
            node_weight[word] = pr[index]

        self.node_weight = node_weight


text = '''
We’ve all heard of co-working, but new to the Hong Kong scene is co-living. Adopting the same principles as the popular shared workspaces, co-living aims to offer young professionals an alternative to traditional renting. Not only do the spaces strive to bring a more affordable option to our city’s pricey property market, but co-living is also a much more flexible way of living that’s perfect for our transient city. Whether you’re in Hong Kong long or short term, co-living promises a community feel. Many of the options available have stylish open-plan shared spaces, complete with all the amenities you’ll need to feel at home and well looked after. Keen to try it out? We’ve rounded up the best co-living spaces in Hong Kong.
With locations in Prince Edward and Hung Hom, Weave Co-Living offers value-for-money urban accommodation (with prices for Premium En-Suite Bedrooms starting at just $10,480 per month, all-inclusive) and a lively community for young professionals and millennials. Featuring a minimalist modern design aesthetic, the bright and airy properties combine private bedrooms with extensive shared spaces and social amenities. There’s even a rooftop (sundowners anyone?), along with hotel-like concierge services to ensure your co-living experience is as easy and hassle-free as they come.

Sassy Perk: Book a Premium En-Suite Bedroom for six months or more and receive an additional $1,000 food and beverage voucher for Fong Waa Parlour, located at Weave on Boundary (while stocks last).

Weave on Boundary, 36 Boundary Street, Prince Edward, Kowloon, Hong Kong, 2155 1400

Weave on Baker, 61 Winslow Street, Hung Hom, Kowloon, Hong Kong, 2155 1400,
YOOF
Affordability meets convenience in YOOF’s newest co-living space, YoofHill. Located in stylish Sai Wan, YoofHill encapsulates the spirit of collaborative economy with its thoughtfully-designed shared-living options. Balancing privacy with community, the co-living space features individual rooms alongside communal spaces (including bathrooms, a large living and dining room, and a fully-equipped kitchen). If that wasn’t enough, regular events and activities (alongside shared rooftop, gym and self-laundry facilities), provide plenty of opportunities for like-minded neighbours to connect – a must for modern city living! Prices start from HK$7,100 per person.

Sassy Perk: Sign up with a friend and book two rooms by Tuesday, 31 March to enjoy up to 5% off (or up to $3,800 discount).

YoofHill, 71 – 77 Hill Road, Sai Wan, Hong Kong, 5228 5445, 5311 3545, info@yoofhk.com, www.yoofhk.com/yoofhill

Slash
Found in the heart of Causeway Bay, Slash offers multi-functional housing that combines living, sharing and community for young professionals and students. It strives to create a space that connects individuals in a multitude of ways, as well as build trust and present opportunities for collaboration. The Slash common area features a reading and games areas, a fully-equipped pantry, a balcony area and more. Both private and shared rooms are available, complete with 24-hour CCTV, regular cleaning, high speed wifi and more. 

Slash, 54-56 Percival Street, Causeway Bay, Hong Kong, www.slash-living.com

Hmlet
Offering co-living spaces in Singapore, Tokyo, Hong Kong and Sydney, Hmlet strives to bring communities together across the globe. With multiple spaces available across Hong Kong, you can narrow down your search by area, home type, length of stay and price to find your perfect home. Spaces vary from rooms in shared houses, to single occupancy studios, but all-inclusive membership plans include a fully-furnished home, utilities, unlimited wifi, weekly cleaning, maintenance, access to community events and the assistance of Community Managers.
Oootopia
With two locations in Kowloon and one on Hong Kong Island, Oootopia is a serviced residence that aims to blend the comfort of a serviced apartment with the community elements of co-living. Oootopia provides flexible term rentals with well-designed rooms and living spaces to tick all the boxes for the modern working individual.

Oootopia, 8 Anchor Street, Tai Kok Tsui, Kowloon, Hong Kong

Oootopia, 18 Sung Wong Toi Road, Kowloon, Hong Kong

Oootopia, 10 Yat Fu Lane, HKU, Hong Kong, www.oootopia.com

The Nate
Offering the best of both worlds, The Nate offers a range of fully-furnished studio apartments, complete with a communal lounge for socialising. What’s more, all residents have access to a fully equipped kitchen, self-service laundromat and rooftop. Conveniently located in the heart of Tsim Sha Tsui, The Nate offers both short and long-term rentals, with studios sized between 125 sq ft and 160 sq ft.

The Nate, 176 Nathan Road, Tsim Sha Tsui, Kowloon, Hong Kong, www.livethenate.com

Featured image courtesy of The Nate via Instagram, image 1 courtesy of Weave Co-Living, image 2 courtesy of YOOF, image 3 courtesy of Oootopia via Facebook.
'''

print(time.localtime())
tr4w = TextRank4Keyword()
tr4w.analyze(text, candidate_pos=['NOUN', 'PROPN'], window_size=1, lower=False)
tr4w.get_keywords(10)

print(time.localtime())

tr4w.analyze(text, candidate_pos=['NOUN', 'PROPN'], window_size=2, lower=False)
tr4w.get_keywords(5)
print(time.localtime())
