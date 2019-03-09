import os
from env import ENV

CHARS_TO_REMOVE = list('''.()"',-:;''')
CORPUS = dict()


def sanitize_line(line):
    for char_to_remove in CHARS_TO_REMOVE:
        line = line.replace(char_to_remove, ' ')
    return(line)


def fetch_corpus_from_file(filename):
    if filename.endswith(".txt"):
        with open("{}/CaseDocuments/All_FT/{}".format(ENV["DATASET_PATH"], case_filename)) as f:
            for line in f.readlines():
                line = sanitize_line(line)
                words = line.lower().split()
                for word in words:
                    word = word.strip()
                    if len(word) > 3:
                        if word in CORPUS:
                            CORPUS[word] += 1
                        else:
                            CORPUS[word] = 1


def fetch_corpus():
    for filename in os.listdir("{}/CaseDocuments/All_FT".format(ENV["DATASET_PATH"])):
        fetch_corpus_from_file(filename)


if __name__ == "__main__":
    fetch_corpus()
    for (word, count) in sorted(CORPUS.items(), key=lambda k: k[1], reverse=True):
        print(word, count)
    print(len(CORPUS))
