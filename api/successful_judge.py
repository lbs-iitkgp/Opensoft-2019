'''
    This module returns the graph having JUDGES and cases as nodes
            with judge nodes pointing to their respective case nodes
    '''

import os
import re
import nltk
from env import ENV
# import json
CASE_FILE = os.listdir("{}/CaseDocuments/All_FT".format(ENV["DATASET_PATH"]))

JUDGES = []

# List of Honorary title present commonly in a Judge's name
#   and are removed for easy-handling of names

HONORIFICS = ["MR. ", "MRS. ", "DR. ", "MRS. ",
              "SHRI ", "SHRI ", "HON'BLE ", "JUSTICE ", "CJI ", 
              "JUTICE ","(J)","(CJ)","(CJI)"]


def check_match(a, b):
    '''
        Returns if two strings a (or b) is an abbreviation of string b (or a)
                Ex. H. R. KHANNA == HANS RAJ KHANNA
        '''
    l = a.split()
    m = b.split()

    r = len(m)

    if len(l) != r:
        return 0
    j = r
    for i in range(r):
        if l[r - i - 1] != m[r - i - 1]:
            j = i
            break

    if j == 0:  # Title didn't match hence names are different
        return 0

    ans = 0

    for k in range(r - j):

        if l[k][0] != m[k][0]:
            break

        if k == r - j - 1:
            ans = (l[k][0] == m[k][0])

    return ans


def check_typo(a, b):
    '''
        Marks strings a and b as same if their edit distance is at-max 1
                and they differ only in non-abbreviated part of names
                        Ex. P. JAGAN`M`OHAN REDDY == P. JAGAN`B`OHAN REDDY
        '''
    l = a.split()
    m = b.split()

    r = len(m)
    j = r
    if len(l) != r:
        return 0

    for i in range(r):
        if l[i] != m[i]:
            if l[i] != m[i]:
                if len(l[i]) == len(m[i]) and len(l[i]) == 2:
                    return 0
                elif len(l[i]) == len(m[i]) and len(l[i]) != 2:
                    return 1


PARENT = {}
CASE_FILE_TO_ID = {}

def get_parent(a):
    '''
        Returns the global parent in the child-parent tree of a name
                Ex. HANS RAJ KHANNA --> HANS. RAJ. KHANNA --> H. R. KHANNA
        '''
    while a != PARENT[a]:
        a = PARENT[a]
    return a


def get_case_id():
    '''
        Returns the Indlaw SC Id for a case and its name (as in CaseDocuments/All_FT directory)
        '''
    with open("{}/doc_path_ttl_id.txt".format(ENV["DATASET_PATH"])) as doc_file:   

        for line in doc_file.readlines():

            line = line.strip()
            file_name, title, case_id = line.split("-->")
            CASE_FILE_TO_ID[file_name] = case_id


def judge_to_case(graph):
    '''
        This function builds the required graph having judge pointing to his/her cases
        '''
    get_case_id()

    temporary_judges = {}   # Stores the line where a judge may potentially be found
    immediate_next_line = {}    #   Similar to above, handles some more edge cases

    for file_name in CASE_FILE:
        path = os.path.join('./CaseDocuments/All_FT', file_name)

        # Get the key value for CASE_FILE_TO_ID
        idx = re.search(r".txt", file_name)

        if idx is not None:
            idx = idx.start()
        file_key = file_name[:idx]

        # try:
        #     file_key = CASE_FILE_TO_ID[file_key]
        # except:
        #     KeyError
        # else:
        #     file_key = file_key

        if file_key in CASE_FILE_TO_ID:
            file_key = CASE_FILE_TO_ID[file_key]


        with open("{}/CaseDocuments/All_FT/{}".format(ENV["DATASET_PATH"], file_name)) as curr_file:

            found_judge = 0         #   Flags to mark name has been found
            found_next_line = 0

            for line in curr_file.readlines():
                if found_judge:
                    found_next_line = 1
                    immediate_next_line[file_key] = line    
                    #   Done so as to handle cases where the name of the judge is in the line following the one having 'delivered'

                idx = re.search(r"delivered", line)

                if idx is not None and not found_judge:
                    found_judge = 1
                    idx = idx.start()
                    if len(line) <= 150:
                        judge_containing_line = line[idx + 9:]
                    else:
                        judge_containing_line = "NONE"

                elif not found_judge:  # Case with no judge
                    judge_containing_line = "NONE"

                if found_judge and found_next_line:
                    temporary_judges[file_key] = judge_containing_line
                    break

    final_list = {} #   Will store the final_list after separating the names of judges from the lines stored above
    result = {} # Will store the final mapping of the judge names to cases after a lot of filtering below
    cnt = 0

    # print(len(temporary_judges))

    for judge_key in temporary_judges:
        cnt += 1

        judge = temporary_judges[judge_key]

        judge = judge.strip()
        judge = judge.upper()   # Convert names to upper case for easy handling

        judge = judge.replace('.','. ') # Add extra space after . in names so as to separate out the initials from the title 

        for word in HONORIFICS: # Remove all hororifics from the name for easy handling
            if word in judge:
                judge = judge.replace(word, '')

        if 'BY ' in judge:      #  Gets the actual name of the judge by removing all unncessary prepositions
            judge = judge[:judge.index('BY ')] + judge[judge.index('BY ') + 3:]
        if 'BY:' in judge:
            judge = judge[:judge.index('BY:')] + judge[judge.index('BY:') + 3:]
        if ':' in judge:
            judge = judge[:judge.index(':')] + judge[judge.index(':') + 1:]

        if 'BY' == judge[-2:]:
            judge = immediate_next_line[judge_key]

        judge = judge.replace('.','. ') #   Additional checks for cases where next line is considered

        for word in HONORIFICS:
            if word in judge:
                judge = judge.replace(word, '')

        judge = judge.upper()           #   Uppercase the name in case the next line is chosen
        judge = judge.rstrip('J.')      #   Remove all trailing J., J, commas, and leading figures
        judge = judge.rstrip('J')
        judge = judge.rstrip(',')
        judge = judge.strip('1.')

        judge = judge.strip()

        names = re.split(',', judge)
        multiple_names = []             #   Handles multiple judges by splitting the name by commas
        for name in names:
            if name == '':
                continue
            if name.find(' AND ') != -1:    # The substring having the last two judges, split them by ' AND ' and keep both
                temp = name.split(' AND ')
                for tt in temp:
                    if(len(tt) <= 25):
                        number = re.search(r"[0-9]",tt) #   Probably a junk string having digits, remove it
                        if number is None:
                            multiple_names.append(tt)
            else:
                if(len(name) <= 25):        # 25 is set as the limit to prevent random strings from getting into the result
                    number = re.search(r"[0-9]",name)
                    if number is None:
                        multiple_names.append(name)

        for i in range(len(multiple_names)):    # Do the preprocessing and filtering on all the separated multiple names again

            multiple_names[i] = multiple_names[i].strip()
            multiple_names[i] = multiple_names[i].rstrip('J.')

            if multiple_names[i] == '':
                continue
            if multiple_names[i] == ' ':
                continue
            string = ""
            for character in multiple_names[i]:
                if character == '.':
                    string += '. '
                else:
                    string += character

            multiple_names[i] = string
            multiple_names[i] = multiple_names[i].strip()

        multiple_names = list(filter(lambda a: a != 'J. ', multiple_names)) #   Final fine tuning process
        multiple_names = list(filter(lambda a: a != 'J.', multiple_names))
        multiple_names = list(filter(lambda a: a != 'J', multiple_names))

        for i in range(len(multiple_names)):
            multiple_names[i] = " ".join(multiple_names[i].split())

        for name in multiple_names:
            if len(name) <= 2:
                continue
            PARENT[name] = name
            # try:
            #     final_list[name].append(judge_key)  # final_list has all judges (which may have same names repeated, thanks to typos)
            # except KeyError:
            #     final_list[name] = []
            #     final_list[name].append(judge_key)

            if name in final_list:
                final_list[name].append(judge_key)
            else:
                final_list[name] = []
                final_list[name].append(judge_key)

    # print(len(final_list))

    done = set()

    for key_1 in PARENT:    #   Groups isomorphic names together based on the pattern of their initials and titles
        for key_2 in PARENT:
            if key_1 != key_2:
                m = min(key_1, key_2)
                n = max(key_1, key_2)

                if (m, n) not in done:
                    done.add((m, n))
                    check = check_match(n, m)
                    if check:
                        if n.find('.') != -1:
                            if m.find('.') == -1:
                                PARENT[m] = n
                            else:
                                i1 = n.index('.')
                                if i1 == 1:
                                    PARENT[m] = n
                                else:
                                    PARENT[n] = m

    done = set()
    ''' Set the local parent of each name earlier to global parents, 
            such that all n nnumber of variations of a name get the same key in the final result'''

    for key in PARENT:  
        PARENT[key] = get_parent(key)

    '''
        Final filtering step, grouping words with close Edit distance together (Ex. A. B. BHAT & A. B. BHATT)
        '''

    for key_1 in PARENT:
        for key_2 in PARENT:
            if key_1 != key_2:
                m = key_1
                n = key_2
                if (m, n) not in done:
                    done.add((m, n))
                    done.add((n, m))
                    edit_dist = nltk.edit_distance(m, n)
                    if edit_dist <= 1 and check_typo(m, n):
                        if PARENT[m] != n:
                            PARENT[n] = m

    '''
        Appends every name's details to it's parent's dict and constructs the graph
        '''

    done = set()
    marked = set()
    for key in PARENT:
        result[PARENT[key]] = []
    for key_1 in final_list:
        for key_2 in final_list:
            m = min(key_1, key_2)
            n = max(key_1, key_2)

            if (m, n) in done:
                continue
            if m != n:
                done.add((m, n))
                done.add((n, m))
                p = PARENT[n]
                q = PARENT[m]

                if n not in marked:
                    marked.add(n)
                    result[p] += final_list[n]
                if m not in marked:
                    marked.add(m)
                    result[q] += final_list[m]

    '''
        Final process, get the graph with judge -> case constructed
        '''
    for judge in result:
        for key in result[judge]:
            graph.add_edge_judge_case(judge, key)

    return graph
    # with open('test2.json','w') as f:
    #     json.dump(result,f,indent=4)        

# if __name__ == "__main__":
    # judge_to_case()