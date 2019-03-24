import os
import spacy
import json

# for token in doc:
#     if token.pos_ not in tags.keys():
#         tags[token.pos_] = [token.text]
#     else:
#         tags[token.pos_].append(token.text)
#
# for key, val in tags.items():
#     print(key, ': ', val)
SIMILARITY_THRESHOLD = 0.6


def get_topic_clusters(keywords, nlp):

    # make a line out of these words
    keywords_line = " ".join(keywords)
    # for testing
    # keywords_line = " ".join(keywords[:100])

    # remove duplicate words and join them
    keywords_line = set(keywords_line.split())
    keywords_line = " ".join(keywords_line)

    doc = nlp(keywords_line)

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
            if word2.similarity(word) > SIMILARITY_THRESHOLD:
                cluster.append(word2.text)
                words.remove(word2)
        clusters.append(cluster)
        words.remove(word)

    return clusters


if __name__ == '__main__':

    nlp = spacy.load('en_core_web_md')

    file = open(os.path.join(os.getcwd(), 'api', 'base_class', 'catch.json'), 'r')

    catch_words = [item[0] for item in json.loads(file.read())]
    # Removes year from keywords
    catch_words = [item.lower() for item in catch_words if not item.isnumeric()]

    print(get_topic_clusters(catch_words, nlp))
