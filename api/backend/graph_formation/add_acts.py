from env import ENV
import act_section_parser

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
    per_page = 100
    for page in range(int(len(all_cases)/per_page)):
        j_new = j
        low = page*per_page
        high = (page+1)*per_page

        page_of_cases = all_cases[low:high]

        low = 0
        high = 100
        # for i, case in enumerate(CASE_ID_TO_FILE):
        for i, case in enumerate(page_of_cases):
            # if i> 10:
            #     continue
            # if case in CASE_ID_TO_FILE:
                # i += 1
            case_file = CASE_ID_TO_FILE[case]
            print("Running act-case mapper for case {}: {}".format(i+1, case_file))
            acts = act_section_parser.fetch_all_acts_in_a_case(case_file)
            # print(acts)
            for act in acts:
                if act in j_new:
                    j_new.add_edge(act, case)

        lkg_to_json(j_new, "lkg_page_{}.json".format(page))
    # return(j)