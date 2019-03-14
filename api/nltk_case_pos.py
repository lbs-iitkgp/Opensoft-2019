import os
import bs4 as bs
import urllib.request  
import re
import nltk
from knapsack import knapsack
import heapq  
from env import ENV


case_filenames = [f for f in os.listdir("{}/All_FT".format(ENV["DATASET_PATH"])) if not f.startswith(".") ]
for i, case_filename in enumerate(case_filenames[:10]):
    case_text = ""

    with open("{}/All_FT/{}".format(ENV["DATASET_PATH"], case_filename)) as f:
        for line in f.readlines():
            case_text += line.strip()
    print("\n{}. POS-tagger of {}:".format(i+1, case_filename))
    print(nltk.pos_tag(nltk.word_tokenize(" ".join(case_text.split(" ")))))
