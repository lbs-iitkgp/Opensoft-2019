import os
from env import ENV


import bs4 as bs
import urllib.request  
import re
import nltk
from knapsack import knapsack
import heapq  


MAX_WORDS=100

def fetch_summary_for_case(case_filename):
    paragraphs = []
    article_text = ""
    l = 0

    with open("{}/All_FT/{}".format(ENV["DATASET_PATH"], case_filename + '.txt')) as f:
        for line in f.readlines():
            paragraphs.append(line)
            l += 1

    for p in paragraphs:  
        article_text += p

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

    sani_sent_list = []

    new_sent = sentence_list[0]
    for j in range(len(sentence_list)-1):
        last_word = new_sent.split(" ")[-1]
        if last_word[-1] != ".":
            new_sent += "."
        last_word = last_word[:-1]
        if len(last_word) < 4 or "." in last_word or "/" in last_word:
            new_sent += (" " + sentence_list[j+1])
        else:
            sani_sent_list.append(new_sent)
            new_sent = sentence_list[j+1]

    if new_sent.split(" ")[-1][-1] != ".":
        new_sent += "."
    sani_sent_list.append(new_sent)
    for sent in sani_sent_list:
        stopped_sent_words = []
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < MAX_WORDS/3:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
                    stopped_sent_words.append(word)
        stopped_sentences.append(" ".join(stopped_sent_words))
    summary_sentences = heapq.nlargest(20, sentence_scores, key=sentence_scores.get)

    size = [len(s.split(" ")) for s in summary_sentences]
    weights = [sentence_scores[s]/len(s.split(" ")) for s in summary_sentences]
    sol = knapsack(size, weights).solve(MAX_WORDS)
    max_weight, selected_sizes = sol
    summary = " ".join(summary_sentences[s] for s in selected_sizes)
    return(summary, max_weight, selected_sizes)

def main():
    case_filenames = [f for f in os.listdir("{}/All_FT".format(ENV["DATASET_PATH"])) if not f.startswith(".") ]
    for i, case_filename in enumerate(case_filenames):
        summary, max_weight, selected_sizes = fetch_summary_for_case(case_filename)
        words_in_summary = len(summary.split(" "))
        print("\n{}. Summary of {} with {} words, {} sentences and {} score is : {}".format(i+1, case_filename, words_in_summary, len(selected_sizes), max_weight, summary))

if __name__ == "__main__":
    main()