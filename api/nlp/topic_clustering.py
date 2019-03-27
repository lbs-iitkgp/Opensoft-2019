import os
import spacy
import json
from string_matching import find_score

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
    # keywords_line = " ".join(keywords)
    # for testing
    keywords_line = " ".join(keywords[:500])

    # remove duplicate words and join them
    keywords_line = set(keywords_line.split())
    keywords_line = [item for item in keywords_line if not item.isnumeric()]
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
    words_used = []
    for token in words:
        if token.text in words_used:
            continue
        words_used.append(token.text)
        cluster = [token.text]
        for token2 in words:
            if token2.text in words_used:
                continue
            if token2.similarity(token) >= SIMILARITY_THRESHOLD:
                cluster.append(token2.text)
                words_used.append(token2.text)
        clusters.append(cluster)

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
    keywords_line = " ".join(dict_keys[:500])

    # remove duplicate words and join them
    keywords_line = set(keywords_line.split())
    keywords_line = [item for item in keywords_line if not item.isnumeric()]
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
    words_used = []
    for token in words:
        if token.text in words_used:
            continue
        words_used.append(token.text)
        # add word and its occurrences to the cluster
        cluster = [(token.text, get_count(token.text, keywords))]
        for token2 in words:
            if token2.text in words_used:
                continue
            if token2.similarity(token) >= SIMILARITY_THRESHOLD:
                # add words and its respective occurrencces to the cluster
                cluster.append((token2.text, get_count(token2.text, keywords)))
                words_used.append(token2.text)
        cluster_count = 0
        for word, count in cluster:
            cluster_count += count
        # remove all word occurrences from the cluster
        cluster = [item[0] for item in cluster]

        # add cluster and its cumulative occurrences to the list
        clusters.append((cluster, cluster_count))

    return clusters


def process(text):
    """
    Removes numbers from strings
    """
    return " ".join([word for word in text.split() if not word.isnumeric()])


def is_sentence_similar(doc1, doc2, text1, text2):
    """
    Checks if two sentences are similar using a hybrid algorithm
    """

    # if no. of words is only one, then only check for semantic similarity
    if len(text1.split()) < 2 or len(text2.split()) < 2:
        return doc1.similarity(doc2) > 0.7
    return 0.9 * doc1.similarity(doc2) + 0.2 * find_score(text1, text2) / 100 > 0.8


def find_match_score(text1, text2):
    return find_score(text1.replace(' act', ' '), text2.replace(' act', ' '))


def get_sentence_clusters(keywords, nlp):
    """
    clusters a list of sentences according to their semantic similarity
    :param keywords: the list of sentences to be clustered
    :param nlp: the nlp vocab of spacy
    :return: the clusters of sentences (as a list of lists)
    """
    # make a line out of these words
    keywords = [item for item in keywords if not item.isnumeric()]

    # keywords_line = " ".join(keywords)
    # for testing
    # keywords_line = " ".join(keywords[:100])

    words_used = []
    # make clusters with formed tokens
    clusters = []
    for text in keywords:
        if text in words_used:
            continue
        doc1 = nlp(process(text))
        cluster = [text]
        for text2 in keywords:
            if text2 == text or text2 in words_used:
                continue
            doc2 = nlp(process(text2))
            if is_sentence_similar(doc1, doc2, text, text2):
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

    # catch_words = [item[0].lower() for item in json.loads(file.read())]
    # clusters = get_topic_clusters(catch_words, nlp)
    # clusters.sort(key=lambda x: len(x), reverse=True)
    # catch_words = {item[0].lower(): item[1] for item in json.loads(file.read()) if not item[0].isnumeric()}
    # clusters = get_topic_clusters_with_count(catch_words, nlp)
    # clusters.sort(key=lambda x: len(x[0]), reverse=True)

    catch_words = [item[0].lower() for item in json.loads(file.read())][:500]
    clusters = get_sentence_clusters(catch_words, nlp)
    clusters.sort(key=lambda x: len(x), reverse=True)

    for cluster in clusters:
        print(cluster)
    print(len(clusters))

    # word1 = input("Enter first word : ")
    # word2 = input("Enter second word : ")
    #
    # print(is_similar(word1, word2, clusters))


