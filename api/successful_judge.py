'''
    This module finds the list of all the judges and the details of their related cases
            '''

import os
import networkx as nx

j = nx.DiGraph()


JUDGE_NAMES_DICT_FINAL = {}

ALL_FILES = os.listdir("./All_FT")
ALL_CASES = list(filter(lambda x: x[-4:] == ".txt", ALL_FILES))

print(len(ALL_CASES))

JUDGE_NAMES = {}
JUDGE_NAMES_AS_SET = []
CASE_WITHOUT_JUDGE = 0
FLAG = 0
FIRST_LINE = 1

for case in ALL_CASES:

    file = open("./All_FT/" + case, 'r')
    FLAG = 0
    FIRST_LINE = 1
    for line in file:
        line = line[0: -1]

        if FIRST_LINE:
            title = line
            FIRST_LINE = 0
        words = line.split(" ")
        '''
            The various variations of Judgement found in the given data
            '''
        search_str1 = "Judgement"
        search_str2 = "Judgment"
        search_str3 = "judgement"
        search_str4 = "judgment"
        search_str5 = "delivered"

        year = case[0:4]

        if year in words and len(words) <= 4:
            date_line = line

        if (search_str1 in words or search_str2 in words or search_str3 in words or search_str4 in words) and search_str5 in words:
            FLAG = 1
            for i, item in enumerate(words):
                if words[i] == "by:" or words[i] == ":":
                    name = ""
                    i = i + 1

                    while i < len(words):
                        name = name + " " + words[i]
                        i = i + 1

                    if ':' in name:
                        name = name[: name.index(':')] + name[name.index(':') + 1:]

                    if ',' in name:
                        name = name[: name.index(',')] + name[name.index(',') + 1:]

                    if name != "":
                        if name in JUDGE_NAMES:
                            JUDGE_NAMES[name].append({"Case": case, "Date": date_line, "Title": title})
                        else:
                            JUDGE_NAMES[name] = []
                            JUDGE_NAMES[name].append({"Case": case, "Date": date_line, "Title": title})
                        break

                elif words[i] == "by":
                    name = ""
                    i = i + 1

                    while i < len(words):
                        name = name + " " + words[i]
                        i = i + 1

                    if ':' in name:
                        name = name[: name.index(':')] + name[name.index(':') + 1:]

                    if ',' in name:
                        name = name[: name.index(',')] + name[name.index(',') + 1:]
                    name = name.strip()
                    if name != "":
                        if name in JUDGE_NAMES:
                            JUDGE_NAMES[name].append({"Case": case, "Date": date_line, "Title": title})
                        else:
                            JUDGE_NAMES[name] = []
                            JUDGE_NAMES[name].append({"Case": case, "Date": date_line, "Title": title})
                        break
            break

print(len(JUDGE_NAMES))

JUDGE_NAME_AS_LIST = []


for judge in JUDGE_NAMES:
    s = set()
    l = [s.add(k) for k in judge.split()]
    if s not in JUDGE_NAMES_AS_SET:
        JUDGE_NAMES_DICT_FINAL[judge] = []
        JUDGE_NAMES_DICT_FINAL[judge].append(JUDGE_NAMES[judge])
        JUDGE_NAMES_AS_SET.append(s)
        JUDGE_NAME_AS_LIST.append(judge)
    else:
        JUDGE_NAMES_DICT_FINAL[JUDGE_NAME_AS_LIST[JUDGE_NAMES_AS_SET.index(s)]].append(JUDGE_NAMES[judge])


CASE_FILE_TO_ID = dict()


with open('doc_path_ttl_id.txt') as f:
    for line in f.readlines():
        line = line.strip()
        file_name, title, case_id = line.split("-->")
        CASE_FILE_TO_ID[file_name] = case_id

for k in JUDGE_NAME_AS_LIST:
    for diction in JUDGE_NAMES_DICT_FINAL[k]:
        for x, val in enumerate(diction):   
            if diction[x]["Case"][:-4] in CASE_FILE_TO_ID:
                j.add_edge(k, CASE_FILE_TO_ID[diction[x]["Case"][:-4]])

print(len(j.nodes()))

print(j[JUDGE_NAME_AS_LIST[0]])
