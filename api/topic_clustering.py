import os
import spacy
import json

nlp = spacy.load('en_core_web_md')

file = open(os.path.join(os.getcwd(), 'base_class', 'catch.json'), 'r')

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
