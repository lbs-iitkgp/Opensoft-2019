'''
    This module generates the list of details of all the acts in
        'actslist.txt' comprising of [year, type (central/state), No. of sections]
        '''
from env import ENV
import os
import glob
import json


CENTRAL_FILES = os.listdir('{}/ActDocuments/Central_Text/'.format(ENV["DATASET_PATH"]))
STATE_FILES = os.listdir('{}/ActDocuments/State_Text/'.format(ENV["DATASET_PATH"]))

DICTIONARY_OF_ACTS = {}
'''
    Finds the acts in the central acts folder
    '''


def acts_data_miner():
    serial = 0
    for g in CENTRAL_FILES:
        path = g
        curr_files = [files for files in os.listdir(path)]
        for filed in curr_files:
            serial += 1
            with open(path+"/{}".format(filed)) as fg:
                type_f = "Central"
                myline = fg.readline()
                idx = myline.find('_Section')
                yr = myline[idx - 4:idx]
                act = myline[:idx - 6]

                if 'Act' in act:
                    act = act[:act.rindex('Act')]
                if 'act' in act:
                    act = act[:act.rindex('act')]
                act = act.strip()
                sections = sum(1 for ln in fg)
                if act == "":
                    continue
                try:
                    DICTIONARY_OF_ACTS[act].append([serial, yr, type_f, filed, "Space For Page Rank Score"])
                except KeyError:
                    DICTIONARY_OF_ACTS[act] = []
                    DICTIONARY_OF_ACTS[act].append([serial, yr, type_f, filed, "Space For Page Rank Score"])
            # i += 1
    for g in STATE_FILES:
        path = g
        curr_files = [files for files in os.listdir(path)]
        curr_act = []
        for filed in curr_files:
            serial += 1
            r = os.path.join(path, filed)
            with open(r) as fg:
                myline = fg.readline()
                head, tail = os.path.split(path)
                type_f = tail
                idx = myline.find('_Section')
                yr = myline[idx - 4:idx]
                act = myline[:idx - 6]

                if 'Act' in act:
                    act = act[:act.rindex('Act')]
                if 'act' in act:
                    act = act[:act.rindex('act')]
                act = act.strip()
                sections = sum(1 for ln in fg)
                if act == "":
                    continue
                try:
                    DICTIONARY_OF_ACTS[act].append([serial, yr, type_f, filed, "Space For Page Rank Score"])
                except KeyError:
                    DICTIONARY_OF_ACTS[act] = []
                    DICTIONARY_OF_ACTS[act].append([serial, yr, type_f, filed, "Space For Page Rank Score"])
    return DICTIONARY_OF_ACTS


if __name__ == "__main__":
    acts_data_miner()
    with open('ACTS_BY_STATES.json', 'w') as ff:
        json.dump(DICTIONARY_OF_ACTS, ff, indent=4,sort_keys=True)
