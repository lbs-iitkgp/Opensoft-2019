'''
    This script generates a returns the corresponding date of a case given its Indlaw SC ID
    '''

import os
from env import ENV
CASE_FILE = os.listdir("{}/All_FT".format(ENV["DATASET_PATH"]))

CASE_FILE_TO_ID = dict()


def get_year_from_case(case):
    '''
        Extracts the file path first from the case ID and then gets the date from it
        '''
    with open("{}/{}".format(ENV["DATASET_PATH"], 'doc_path_ttl_id.txt')) as doc_file:
        for line in doc_file.readlines():
            line = line.strip()
            file_name, title, case_id = line.split('-->')
            if case_id == case:
                # Get the year from the file name and search for the date in the file  
                year = line[:4]
                path = file_name + '.txt'
                path = os.path.join('./All_FT', path)
                found = 0
                with open(path, 'r') as f:
                    for line2 in f.readlines():
                        if line2.find(year) != -1:
                            # Extracts the date of the case
                            if found == 0:
                                date = line2
                                found = 1
                                break
    return date
