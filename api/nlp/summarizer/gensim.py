import os
from env import ENV
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


def fetch_summary_from_case(case_filename):
    with open("{}/All_FT/{}".format(ENV["DATASET_PATH"], case_filename)) as f:
        article_text = f.read().strip()
    summary = summarize(article_text, word_count=100).replace("\n", " ").strip()
    return(summary)    

def main():
    case_filenames = [f for f in os.listdir("{}/All_FT".format(ENV["DATASET_PATH"])) if not f.startswith(".") ]
    for i,case_filename in enumerate(case_filenames):
        summary = fetch_summary_from_case(case_filename)
        print("\n{}. Summary of {} with and {} words : {}".format(i+1, case_filename, len(summary.split(" ")), summary))

if __name__ == "__main__":
    main()