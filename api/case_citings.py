"""maps Case-IDs of cases cited in a Case
     to Case-ID of case citing them"""

import os
from legal_graph import LegalKnowledgeGraph


LKG = LegalKnowledgeGraph()

ALL_FILES = os.listdir("./All_FT")
ALL_CASES = [filename for filename in ALL_FILES if filename[-4:] == ".txt"]


CASE_FILE_TO_ID = dict()


def compute_mapping():
    """prepares a dictonary of case_file_name as key
        with corresponding case_id as value for
            all given cases"""

    with open('doc_path_ttl_id.txt') as path_title_id:
        for line in path_title_id.readlines():
            line = line.strip()

            file_name, title, case_id = line.split("-->")
            CASE_FILE_TO_ID[file_name] = case_id


def citing(knowledge_graph):
    """adds edges from cases cited to case citing these cases
        in the given graph"""

    compute_mapping()

    for case in ALL_CASES:
        with open("./All_FT/"+case) as case_file:
            if case[:-4] in CASE_FILE_TO_ID:
                curr_case_id = CASE_FILE_TO_ID[case[:-4]]
                for line in case_file.readlines():
                    line = line.strip()
                    i = line.find("Indlaw")
                    if i != -1:
                        code = line[i+10: i+16]
                        while not code[-1].isdigit():
                            code = code[:-1]
                        year = line[line.find(
                            "Indlaw")-5: line.find("Indlaw")-1]
                        cite_id = year + " Indlaw SC " + code
                        knowledge_graph.add_citings(curr_case_id, cite_id)
    return knowledge_graph
