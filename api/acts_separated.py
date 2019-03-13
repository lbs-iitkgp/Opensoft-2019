'''
    This module generates the list of details of all the acts in
        'actslist.txt' comprising of [year, type (central/state), No. of sections]
        '''

import os
import glob
import json

CENTRAL = [d for d in os.listdir(
    './Central_Text')]
STATE = [d for d in os.listdir(
    './State_Text')]

CENTRAL_FILES = list(
    glob.glob('./Central_Text/*'))
STATE_FILES = list(
    glob.glob('./State_Text/*'))

DICTIONARY_OF_ACTS = {}
# i = 0
'''
    Finds the acts in the central acts folder
    '''
for g in CENTRAL_FILES:
    path = g
    curr_files = [files for files in os.listdir(path)]
    for filed in curr_files:
        r = os.path.join(path, filed)
        with open(r) as fg:
            type_f = "Central"
            myline = fg.readline()
            idx = myline.find('_Section')
            yr = myline[idx - 4:idx]
            act = myline[:idx - 6]
            sections = sum(1 for ln in fg)
            try:
                DICTIONARY_OF_ACTS[act].append([yr, type_f, sections + 1])
            except KeyError:
                DICTIONARY_OF_ACTS[act] = []
                DICTIONARY_OF_ACTS[act].append([yr, type_f, sections + 1])
        # i += 1
for g in STATE_FILES:
    path = g
    curr_files = [files for files in os.listdir(path)]
    curr_act = []
    for filed in curr_files:
        r = os.path.join(path, filed)
        with open(r) as fg:
            myline = fg.readline()
            head, tail = os.path.split(path)
            type_f = tail
            idx = myline.find('_Section')
            yr = myline[idx - 4:idx]
            act = myline[:idx - 6]
            sections = sum(1 for ln in fg)
            try:
                DICTIONARY_OF_ACTS[act].append([yr, type_f, sections + 1])
            except KeyError:
                DICTIONARY_OF_ACTS[act] = [yr, type_f, sections + 1]
            # if act in DICTIONARY_OF_ACTS:
                # print(act)

with open('acts_by_STATEs.json', 'w') as ff:
    json.dump(DICTIONARY_OF_ACTS, ff, indent=4)
