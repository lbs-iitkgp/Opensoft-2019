"""This module contains the function to
        add 'key_word(or subject) to case_id' edges
            and 'catchy_words to case_id' edges in our LKG graph"""

from env import ENV
CASE_FILE_TO_ID = dict()

def add_catch_subject(j):
    """adds 'key_word(or subject) to case_id' edges
        and 'catchy_words to case_id' edges in the graph"""

    with open("{}/doc_path_ttl_id.txt".format(ENV["DATASET_PATH"])) as doc_file:
        for line in doc_file.readlines():
            line = line.strip()

            file_name, title, case_id = line.split("-->")
            CASE_FILE_TO_ID[file_name] = case_id

    with open("{}/subject_keywords.txt".format(ENV["DATASET_PATH"])) as key_word_file:
        for line in key_word_file.readlines():
            line = line.strip()
            if '-->' in line:
                file_name2, title, catch_words_subjs = line.split("-->")
                # print(catch_words_subjs)
                if '$$$' in catch_words_subjs:
                    subjects, catch_words = catch_words_subjs.split("$$$")
                    # print(subjects, catch_words)
                    subjects = subjects.split(";")
                    catch_words = catch_words.split(",")
                    case_id = CASE_FILE_TO_ID[file_name2]
                    for subject in subjects:
                        j.add_key_word_to_case(subject.strip(), case_id)
                    for catch_word in catch_words:
                        j.add_catch_to_case(case_id, catch_word.strip())
    return j


if __name__ == "__main__":
    from backend.graph_formation.base.legal_knowledge_graph import LegalKnowledgeGraph
    LKG = LegalKnowledgeGraph()
    LKG = add_catch_subject(LKG)
    print(len(LKG.nodes()))
    print(LKG['Civil Procedure'])
