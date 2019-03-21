'''
    This module generates the list of details of all the acts in
        'actslist.txt' comprising of [year, type (central/state), No. of sections]
        '''

import os
import glob
import json
import re

CENTRAL = [d for d in os.listdir(
    './Central_Text')]
STATE = [d for d in os.listdir(
    './State_Text')]

CENTRAL_FILES = list(
    glob.glob('./Central_Text/*'))
STATE_FILES = list(
    glob.glob('./State_Text/*'))
# print(len(CENTRAL_FILES))
# print(len(STATE_FILES))
DICTIONARY_OF_ACTS = {}
'''
    Finds the acts in the central acts folder
    '''
for g in CENTRAL_FILES:
    print(g,end=' : ')
    path = g
    curr_files = [files for files in os.listdir(path)]
    for filed in curr_files:
        print(filed,end=' ')
        r = os.path.join(path, filed)
        with open(r) as fg:
            type_f = "Central"
            myline = fg.readline()

            idx = re.search(r"(_Section)", myline)
            if idx is not None:
                idx = idx.start()
            i1 = re.search(r"([0-9]{4})", myline)
            if i1 is not None:
                i1 = i1.start()
            i2 = re.search(r"([0-9]{4})", myline)
            if i2 is not None:
                i2 = i2.end()

            yr = myline[i1:i2]

            act = myline[:idx]

            # if 'Act' in act:
            #     act = act[:act.rindex('Act')]
            # if 'act' in act:
            #     act = act[:act.rindex('act')]
            act = act.strip()
            sections = sum(1 for ln in fg)
            if act == "":
                continue
            try:
                DICTIONARY_OF_ACTS[act].append([yr, type_f, sections + 1])
            except KeyError:
                DICTIONARY_OF_ACTS[act] = []
                DICTIONARY_OF_ACTS[act].append([yr, type_f, sections + 1])
        # i += 1
    print('\n')
for g in STATE_FILES:
    # print(g)
    path = g
    curr_files = [files for files in os.listdir(path)]
    curr_act = []   
    for filed in curr_files:
        r = os.path.join(path, filed)
        with open(r) as fg:
            myline = fg.readline()
            myline = str(myline)
            head, tail = os.path.split(path)
            type_f = tail

            idx = re.search(r"(_Section)", myline)
            if idx is not None:
                idx = idx.start()
            i1 = re.search(r"([0-9]{4})", myline)
            if i1 is not None:
                i1 = i1.start()
            i2 = re.search(r"([0-9]{4})", myline)
            if i2 is not None:
                i2 = i2.end()

            yr = myline[i1:i2]

            act = myline[:idx]

            # if 'Act' in act:
            #     act = act[:act.rindex('Act')]
            # if 'act' in act:
            #     act = act[:act.rindex('act')]
            act = act.strip()
            sections = sum(1 for ln in fg)
            if act == "":
                continue
            try:
                DICTIONARY_OF_ACTS[act].append([yr, type_f, sections + 1])
            except KeyError:
                DICTIONARY_OF_ACTS[act] = [] 
                DICTIONARY_OF_ACTS[act].append([yr, type_f, sections + 1])
# CNT = 0
# for key in DICTIONARY_OF_ACTS:
#     CNT += 1
# print(CNT)

with open('ACTS_BY_STATES.json', 'w') as ff:
    json.dump(DICTIONARY_OF_ACTS, ff, indent=4,sort_keys=True)
