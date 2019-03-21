'''
    This script constructs the case's judgements corresponding to their Case Id's
    '''
import os

CASE_FILE = os.listdir('./All_FT')

OPTIMAL = []


def get_all_judgements(case):
    '''
        Extracts the file path first from the case ID and then gets the date from it
        '''
    with open('doc_path_ttl_id.txt') as doc_file:
        for line in doc_file.readlines():
            line = line.strip()
            file_name, title, case_id = line.split('-->')
            if case_id == case:  # Found required case
                path = file_name + '.txt'
                path = os.path.join('./All_FT', path)

                with open(path, 'r') as f:
                    line2 = f.readlines()
                    # '''Extracts the judgement of the case'''
                    if len(line2[-1]) <= 50:
                        l = line2[-1][:-4]
                        res = line2[-1].strip()
                    else:
                        l = line2[-1].split('.')
                        # Finds all sentences with word `appeal`
                        # and takes the one with minimum of them
                        for ll in l[::-1]:
                            if 'appeal' in ll:
                                OPTIMAL.append(ll)
                        res = min(OPTIMAL, key=lambda s: len(s))
                    break
    return res
