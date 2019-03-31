from env import ENV
import act_section_parser
from backend.graph_io import lkg_to_json

CASE_ID_TO_FILE = dict()
def compute_mapping():
    with open("{}/doc_path_ttl_id.txt".format(ENV["DATASET_PATH"])) as f:
        for line in f.readlines():
            line = line.strip()
        
            file_name, title, case_id = line.split("-->")
            CASE_ID_TO_FILE[case_id] = file_name+".txt"

def map_acts_with_cases(j):
    compute_mapping()
    # i = 0

    all_cases = list(CASE_ID_TO_FILE.keys())
    for i, case in enumerate(page_of_cases):
        case_file = CASE_ID_TO_FILE[case]
        print("Running act-case mapper for case {}: {}".format(i+1, case_file))
        acts = act_section_parser.fetch_all_acts_in_a_case(case_file)
        # print(acts)
        for act in acts:
            if act in j_new:
                j_new.add_edge(act, case)

    return(j)