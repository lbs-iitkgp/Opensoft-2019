import os
import spacy
import json


# The threshold limit for two words to consider as similar
SIMILARITY_THRESHOLD = 0.65


def get_topic_clusters(keywords, nlp):
    """
    Returns clusters of topics (list of lists) from a given list of keywords
    :param keywords: list of keywords to be clustered
    :param nlp: the nlp vocab by spacy
    :return: clusters of topic (list of lists)
    """
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
        cluster = [word.text]
        for word2 in words:
            if word2.text == word.text:
                continue
            if word2.similarity(word) >= SIMILARITY_THRESHOLD:
                cluster.append(word2.text)
                words.remove(word2)
        clusters.append(cluster)
        words.remove(word)

    return clusters


def get_count(word, dictionary):
    """
    Find the occurrences of the word in the dictionary
    """
    sum = 0
    for key, val in dictionary.items():
        if word in key:
            sum += val

    return sum


def get_topic_clusters_with_count(keywords, nlp):
    """
        Returns clusters of topics and their occurences in the list (list of lists) from a given list of keywords
        :param keywords: list of keywords to be clustered
        :param nlp: the nlp vocab by spacy
        :return: clusters of topic (list of lists)
    """

    dict_keys = list(keywords.keys())
    # make a line out of these words
    keywords_line = " ".join(dict_keys)
    # for testing
    # keywords_line = " ".join(dict_keys[:100])

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
    for token in words:
        # add word and its occurrences to the cluster
        cluster = [(token.text, get_count(token.text, keywords))]
        for word2 in words:
            if word2.text == token.text:
                continue
            if word2.similarity(token) >= SIMILARITY_THRESHOLD:
                # add words and its respective occurrencces to the cluster
                cluster.append((word2.text, get_count(word2.text, keywords)))
                words.remove(word2)
        cluster_count = 0
        for word, count in cluster:
            cluster_count += count
        # remove all word occurrences from the cluster
        cluster = [item[0] for item in cluster]

        # add cluster and its cumulative occurrences to the list
        clusters.append((cluster, cluster_count))
        words.remove(token)

    return clusters


def process(text):
    return " ".join([word for word in text.split() if not word.isnumeric()])


def get_sentence_clusters(keywords, nlp):
    # make a line out of these words
    keywords = [item for item in keywords if not item.isnumeric()]

    # keywords_line = " ".join(keywords)
    # for testing
    # keywords_line = " ".join(keywords[:100])

    # remove duplicate words and join them
    keywords_line = keywords

    words_used = []
    # make clusters with formed tokens
    clusters = []
    for text in keywords_line:
        if text in words_used:
            continue
        doc1 = nlp(process(text))
        cluster = [text]
        for text2 in keywords_line:
            if text2 == text or text2 in words_used:
                continue
            doc2 = nlp(process(text2))
            if doc1.similarity(doc2) > 0.7:
                cluster.append(text2)
                words_used.append(text2)
        clusters.append(cluster)
        words_used.append(text)

    return clusters


def is_similar(word1, word2, clusters):
    """
    Checks if two strings belong to the cluster
    """
    if isinstance(clusters[0], tuple):
        for cluster, count in clusters:
            if word1 in cluster and word2 in cluster:
                return True
        return False
    else:
        for cluster in clusters:
            if word1 in cluster and word2 in cluster:
                return True
        return False


if __name__ == '__main__':

    nlp = spacy.load('en_core_web_md')

    file = open(os.path.join(os.getcwd(), 'api', 'base_class', 'catch.json'), 'r')

    catch_words = [item[0].lower() for item in json.loads(file.read())]
    # catch_words.append("criminal")
    # catch_words.append("crime")
    # catch_words.append("killing")

    # Removes year from keywords
    # catch_words = [item.lower() for item in catch_words if not item.isnumeric()]

    clusters = get_sentence_clusters(catch_words, nlp)

    # catch_words = {item[0].lower(): item[1] for item in json.loads(file.read()) if not item[0].isnumeric()}
    #
    # clusters = get_topic_clusters_with_count(catch_words, nlp)

    print(len(clusters))

    # word1 = input("Enter first word : ")
    # word2 = input("Enter second word : ")
    #
    # print(is_similar(word1, word2, clusters))



