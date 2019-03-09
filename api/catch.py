
CASE_FILE_TO_ID = dict()


def add_catch_subject(j):
    with open('doc_path_ttl_id.txt') as f:
        for line in f.readlines():
            line = line.strip()
        
            file_name, title, case_id = line.split("-->")
            CASE_FILE_TO_ID[file_name] = case_id

    with open('subject_keywords.txt') as sk:
        for line in sk.readlines():
            line = line.strip()
            if '-->' in line:
                file_Name2, title2, catch_words_subjs = line.split("-->")
                print(catch_words_subjs)
                if '$$$' in catch_words_subjs:
                    subjects, catch_words = catch_words_subjs.split("$$$")
                    print(subjects, catch_words)
                    subjects = subjects.split(";")
                    catch_words = catch_words.split(";")
                    case_id = CASE_FILE_TO_ID[file_Name2]
                    for subject in subjects:
                        j.add_key_word_to_case(subject.strip(), case_id)
                    for catch_word in catch_words:
                        j.add_catch_to_case(case_id, catch_word.strip())
    return(j)

if __name__ == "__main__":
    from legal_graph import LegalKnowledgeGraph
    j = LegalKnowledgeGraph()
    j= add_catch_subject(j)
    print(len(j.nodes()))
    print(j['Civil Procedure'])
