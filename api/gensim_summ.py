import os
from env import ENV

# from gensim import summarization

# MAX_WORDS=100

# case_filenames = [f for f in os.listdir("{}/All_FT".format(ENV["DATASET_PATH"])) if not f.startswith(".") ]
# for i,case_filename in enumerate(case_filenames[:10]):
#     article_lines = []
#     with open("{}/All_FT/{}".format(ENV["DATASET_PATH"], case_filename)) as f:
#         for line in f.readlines():
#             article_lines.append(line.strip())

#     summ = summarization.summarize(article_lines)
#     print("\n{}. Summary of {} with and {} words : {}".format(i+1, case_filename, len(summ.split(" ")), summ))


from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

case_filenames = [f for f in os.listdir("{}/All_FT".format(ENV["DATASET_PATH"])) if not f.startswith(".") ]
for i,case_filename in enumerate(case_filenames[:500]):
    with open("{}/All_FT/{}".format(ENV["DATASET_PATH"], case_filename)) as f:
        article_text = f.read().strip()
    summ = summarize(article_text, word_count=100).replace("\n", " ").strip()
    print("\n{}. Summary of {} with and {} words : {}".format(i+1, case_filename, len(summ.split(" ")), summ))
