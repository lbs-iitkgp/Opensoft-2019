'''
    This module generates the list of details of all the acts in
        'actslist.txt' comprising of [year, type (central/state), No. of sections]
        '''
import os
import glob
import re
from env import ENV

def get_acts_by_states():

    STATE_FILES = os.listdir("{}/State_Text".format(ENV["DATASET_PATH"]))
    CENTRAL_FILES = os.listdir("{}/Central_Text".format(ENV["DATASET_PATH"]))  
    
    DICTIONARY_OF_ACTS = {}
    '''
        Finds the acts in the central acts folder
        '''
    for g in CENTRAL_FILES:
        
        curr_files = os.listdir("{}/Central_Text/{}".format(ENV["DATASET_PATH"], g))

        for filed in curr_files:
            # r = os.path.join(path, filed)
            with open("{}/Central_Text/{}/{}".format(ENV["DATASET_PATH"],g, filed)) as fg:
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
                act = act.strip()
                sections = sum(1 for ln in fg)
                if act == "":
                    continue
                try:
                    DICTIONARY_OF_ACTS[act].append([yr, type_f, sections + 1])
                except KeyError:
                    DICTIONARY_OF_ACTS[act] = []
                    DICTIONARY_OF_ACTS[act].append([yr, type_f, sections + 1])
    for g in STATE_FILES:

        curr_files = os.listdir("{}/State_Text/{}".format(ENV["DATASET_PATH"], g))

        for filed in curr_files:
            with open("{}/State_Text/{}/{}".format(ENV["DATASET_PATH"],g, filed)) as fg:
                myline = fg.readline()
                myline = str(myline)
                type_f = g

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

                act = act.strip()
                sections = sum(1 for ln in fg)
                if act == "":
                    continue
                try:
                    DICTIONARY_OF_ACTS[act].append([yr, type_f, sections + 1])
                except KeyError:
                    DICTIONARY_OF_ACTS[act] = [] 
                    DICTIONARY_OF_ACTS[act].append([yr, type_f, sections + 1])
    return DICTIONARY_OF_ACTS