import os
from backend.graph_formation.base.legal_knowledge_graph import LegalKnowledgeGraph
from env import ENV

all_files = os.listdir("{}/All_FT".format(ENV["DATASET_PATH"]))
all_cases = filter(lambda x: x[-4:] == ".txt" and x[0]!=".", all_files)

CASE_FILE_TO_ID = dict()


def compute_mapping():
    with open("{}/doc_path_ttl_id.txt".format(ENV["DATASET_PATH"])) as f:
        for line in f.readlines():
            line = line.strip()
        
            file_name, title, case_id = line.split("-->")
            CASE_FILE_TO_ID[file_name] = case_id

def citing(j):
    compute_mapping()

    for case in all_cases:
        with open("{}/All_FT/{}".format(ENV["DATASET_PATH"], case))  as f:
            if case[:-4] in CASE_FILE_TO_ID: 
                curr_case_id = CASE_FILE_TO_ID[case[:-4]]
                for line in f.readlines():
                    line = line.strip()
                    i = line.find("Indlaw")
                    if i != -1:
                        code = line[i+10 : i+16]
                        while(not code[-1].isdigit()):
                            code= code[:-1]
                        year = line[line.find("Indlaw")-5 : line.find("Indlaw")-1]
                        cite_id = year + " Indlaw SC " + code
                        j.add_citings(curr_case_id, cite_id)
    return(j)

