import os
from env import ENV

from summa import summarizer, keywords

def fetch_summary_from_case(case_filename):
    MAX_WORDS=100

    article_text = ""
    with open("{}/All_FT/{}".format(ENV["DATASET_PATH"], case_filename)) as f:
        for line in f.readlines():
            article_text += " "
            article_text += line.strip()
    article_text = article_text.strip()
    summary = summarizer.summarize(article_text, words=MAX_WORDS).strip()
    return(summary, article_text)

def main():
    case_filenames = [f for f in os.listdir("{}/All_FT".format(ENV["DATASET_PATH"])) if not f.startswith(".") ]
    for i, case_filename in enumerate(case_filenames):
        summary, article_text = fetch_summary_from_case(case_filename)
        print("\n{}. Summary of {} with {} keywords and {} words : {}".format(i+1, case_filename, len(keywords.keywords(article_text)), len(summary.split(" ")), summary))

if __name__ == "__main__":
    main()
