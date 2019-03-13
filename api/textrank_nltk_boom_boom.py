import os
from env import ENV

from summa import summarizer, keywords

MAX_WORDS=100

import re
import nltk
from knapsack import knapsack
import heapq  


def provide_summary(article_text):
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
    article_text = re.sub(r'\s+', ' ', article_text)
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    sentence_list = nltk.sent_tokenize(article_text)

    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}  
    for word in nltk.word_tokenize(formatted_article_text):  
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    sentence_scores = {}  
    stopped_sentences = []
    for sent in sentence_list:
        stopped_sent_words = []
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
                    stopped_sent_words.append(word)
        stopped_sentences.append(" ".join(stopped_sent_words))
    # summary_sentences = heapq.nlargest(MAX_LINES, sentence_scores, key=sentence_scores.get)
    summary_sentences = heapq.nlargest(20, sentence_scores, key=sentence_scores.get)

    # for i,s in enumerate(summary_sentences):
    #     print(i, s, sentence_scores[s], len(s.split(" ")))

    # size = [len(s.split(" ")) for s in summary_sentences]
    size = [len(stopped_sentences[sentence_list.index(s)].split(" ")) for s in summary_sentences]
    weights = [sentence_scores[s] for s in summary_sentences]
    # print(size, weights)
    sol = knapsack(size, weights).solve(MAX_WORDS)
    # print(sol)
    max_weight, selected_sizes = sol

    summary = " ".join(summary_sentences[s] for s in selected_sizes)
    words_in_summary = len(summary.split(" "))
    print("\n{}. Summary of {} with {} words, {} sentences and {} score is : {}".format(i+1, case_filename, words_in_summary, len(selected_sizes), max_weight, summary))

    return(summary)


case_filenames = [f for f in os.listdir("{}/All_FT".format(ENV["DATASET_PATH"])) if not f.startswith(".") ]
for i,case_filename in enumerate(case_filenames[:10]):
    article_text = ""
    with open("{}/All_FT/{}".format(ENV["DATASET_PATH"], case_filename)) as f:
        for line in f.readlines():
            article_text += " "
            article_text += line.strip()
    article_text = article_text.strip()
    textrank_summ = summarizer.summarize(article_text)
    nltk_textrank_summ = provide_summary(textrank_summ)
    # print("{}. Summary of {} with {} keywords and {} words : {}".format(i+1, case_filename, len(keywords.keywords(article_text)), len(summ.split(" ")), summ))
