# from nltk.corpus import stopwords
# from nltk.stem.wordnet import WordNetLemmatizer
# import string
# import gensim
# from gensim import corpora
# import os
#
# import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')
#
# stop = set(stopwords.words('english'))
# exclude = set(string.punctuation)
# lemma = WordNetLemmatizer()
#
# file = open(os.path.join(os.getcwd(), 'api', 'All_FT', '1953_A_7.txt'))
# doc_complete = [line for line in file.readlines()]
#
#
# def clean(doc):
#     stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
#     punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
#     normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
#     return normalized
#
#
# doc_clean = [clean(doc).split() for doc in doc_complete]
#
#
# # Creating the term dictionary of our corpus, where every unique term is assigned an index.
# dictionary = corpora.Dictionary(doc_clean)
#
# # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
# doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
#
# # Creating the object for LDA model using gensim library
# Lda = gensim.models.ldamodel.LdaModel
#
# # Running and Training LDA model on the document term matrix.
# ldamodel = Lda(doc_term_matrix, num_topics=3, id2word=dictionary, passes=50)
#
# print(ldamodel.print_topics(num_topics=3, num_words=10))

import os
import spacy
import json

nlp = spacy.load('en_core_web_md')

file = open(os.path.join(os.getcwd(), 'base_class', 'catch.json'), 'r')
#
# word = input("Enter word : ")
#
# catch_words = []
#
# word_token = nlp(word)[0]
# print(word_token)
#
# for line in file.readlines():
#     doc = nlp(line)
#     for token in doc:
#         if token.similarity(word_token) > 0.7:
#             catch_words.append(token)
#
# print(catch_words)

# Removes year from keywords
catch_words = [item[0].lower() for item in json.loads(file.read()) if not item[0].isnumeric()]

# make a line out of these words
catch_words_line = " ".join(catch_words[:100])

# remove duplicate words and join them
catch_words_line = set(catch_words_line.split())
catch_words_line = " ".join(catch_words_line)

doc = nlp(catch_words_line)

# for token in doc:
#     if token.pos_ not in tags.keys():
#         tags[token.pos_] = [token.text]
#     else:
#         tags[token.pos_].append(token.text)
#
# for key, val in tags.items():
#     print(key, ': ', val)

# form token only of nouns and adjectives
tags = ['NOUN', 'ADJ']
words = []
for token in doc:
    if token.pos_ in tags:
        words.append(token)

# make clusters with formed tokens
clusters = []
for word in words:
    cluster = [word]
    for word2 in words:
        if word2.text == word.text:
            continue
        if word2.similarity(word) > 0.6:
            cluster.append(word2.text)
            words.remove(word2)
    clusters.append(cluster)
    words.remove(word)

print(clusters)
