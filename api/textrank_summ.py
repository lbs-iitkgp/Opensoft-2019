import os
from env import ENV

from summa import summarizer, keywords

MAX_WORDS=100

case_filenames = [f for f in os.listdir("{}/All_FT".format(ENV["DATASET_PATH"])) if not f.startswith(".") ]
for i,case_filename in enumerate(case_filenames[:10]):
    article_text = ""
    with open("{}/All_FT/{}".format(ENV["DATASET_PATH"], case_filename)) as f:
        for line in f.readlines():
            article_text += " "
            article_text += line.strip()
    article_text = article_text.strip()
    summ = summarizer.summarize(article_text, words=MAX_WORDS).strip()
    print("\n{}. Summary of {} with {} keywords and {} words : {}".format(i+1, case_filename, len(keywords.keywords(article_text)), len(summ.split(" ")), summ))
