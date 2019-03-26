# import os

# ALL_FILES = os.listdir("{}/{}".format(ENV["DATASET_PATH"], "All_FT"))
# ALL_CASES = [filename for filename in ALL_FILES if filename[-4:] == ".txt"]

CASE_FILE_TO_ID = dict()
CASE_SERIAL_TO_CASE_KA_DATA = dict()
OPTIMAL = []
serial_id = 0

def compute_mapping():
    """prepares a dictonary of case_file_name as key
        with corresponding case_id as value for
            all given cases"""

    with open('{}/{}'.format(ENV["DATASET_PATH"], "doc_path_ttl_id.txt")) as path_title_id:
    #with open('./{}'.format("doc_path_ttl_id.txt")) as path_title_id:
        for line in path_title_id.readlines():
            line = line.strip()

            file_name, title, case_id = line.split("-->")
            CASE_FILE_TO_ID[file_name] = [file_name, case_id, title] 


def citing(case):
    """adds edges from cases cited to case citing these cases
        in the given graph"""
    # compute_mapping()
        
    with open("{}/CaseDocuments/All_FT/{}".format(ENV["DATASET_PATH"],case)) as case_file:
        if case[:-4] in CASE_FILE_TO_ID:
            curr_case_id = CASE_FILE_TO_ID[case[:-4]][1]
            all_lines = case_file.readlines()
            
            if len(all_lines[-1]) <= 50:
                l = all_lines[-1][:-4]
                judgement = all_lines[-1].strip()
            else:
                l = all_lines[-1].split('.')
                # Finds all sentences with word `appeal`
                # and takes the one with minimum of them
                for ll in l[::-1]:
                    if 'appeal' in ll:
                        OPTIMAL.append(ll)
                judgement = min(OPTIMAL, key=lambda s: len(s))
            
            date = all_lines[3]
            date = date.strip()
            CASE_FILE_TO_ID[case[:-4]].append(date)
            CASE_FILE_TO_ID[case[:-4]].append(judgement)
            CASE_FILE_TO_ID[case[:-4]].append("Page rank score")
            return CASE_FILE_TO_ID[case[:-4]]
 