'''
    This module generates the list of details of all the acts in
        'actslist.txt' comprising of [year, type (central/state), No. of sections]
        '''
import os
import glob
import re
from env import ENV


def get_acts_by_states():
    serial = 0

    STATE_FILES = os.listdir("{}/Acts/State_Text".format(ENV["DATASET_PATH"]))
    CENTRAL_FILES = os.listdir("{}/Acts/Central_Text".format(ENV["DATASET_PATH"]))

    DICTIONARY_OF_ACTS = {}
    '''
        Finds the acts in the central acts folder
        '''
    for g in CENTRAL_FILES:

        curr_files = os.listdir("{}/Acts/Central_Text/{}".format(ENV["DATASET_PATH"], g))

        for filed in curr_files:
            serial += 1
            with open("{}/Acts/Central_Text/{}/{}".format(ENV["DATASET_PATH"], g, filed)) as fg:

                # Type of these kind of acts is CENTRAL

                type_f = "Central"
                myline = fg.readline()

                # Gets the name of the act by taking all the words before the _Section Keyword
                idx = re.search(r"(_Section)", myline)
                if idx is not None:
                    idx = idx.start()

                # Gets the year of the act
                i1 = re.search(r"([0-9]{4})", myline)
                if i1 is not None:
                    i1 = i1.start()
                i2 = re.search(r"([0-9]{4})", myline)
                if i2 is not None:
                    i2 = i2.end()

                yr = myline[i1:i2]

                act = myline[:idx]
                act = act.strip()

                # No. of sections of a act = No. of lines in it's act file
                sections = sum(1 for ln in fg)

                if act == "":
                    continue
                this_dict = {
                    "serial": serial,
                    "name":act,
                    "type":type_f,
                    "year":yr,
                    "file":"/Acts/Central_Text/{}/{}".format(g, filed),
                    "sections":sections,
                }
                if act in DICTIONARY_OF_ACTS:
                    DICTIONARY_OF_ACTS[act].append(this_dict)
                else:
                    DICTIONARY_OF_ACTS[act] = []
                    DICTIONARY_OF_ACTS[act].append(this_dict)

    for g in STATE_FILES:

        curr_files = os.listdir("{}/Acts/State_Text/{}".format(ENV["DATASET_PATH"], g))

        for filed in curr_files:
            serial += 1
            with open("{}/Acts/State_Text/{}/{}".format(ENV["DATASET_PATH"], g, filed)) as fg:

                myline = fg.readline()
                myline = str(myline)

                # Type of these acts varies with the state they belong to
                type_f = g

                # Gets the name of the act by taking all the words before the _Section Keyword
                idx = re.search(r"(_Section)", myline)
                if idx is not None:
                    idx = idx.start()

                # Gets the year of the act
                i1 = re.search(r"([0-9]{4})", myline)
                if i1 is not None:
                    i1 = i1.start()
                i2 = re.search(r"([0-9]{4})", myline)
                if i2 is not None:
                    i2 = i2.end()

                yr = myline[i1:i2]

                act = myline[:idx]

                act = act.strip()
                # No. of sections of a act = No. of lines in it's act file

                sections = sum(1 for ln in fg)
                if act == "":
                    continue
                this_dict = {
                    "serial": serial,
                    "name":act,
                    "type":type_f,
                    "year":yr,
                    "file":"/Acts/State_Text/{}/{}".format(g, filed),
                    "sections":sections,
                }
                if act in DICTIONARY_OF_ACTS:
                    DICTIONARY_OF_ACTS[act].append(this_dict)
                else:
                    DICTIONARY_OF_ACTS[act] = []
                    DICTIONARY_OF_ACTS[act].append(this_dict)
    # Final dict having the acts as key and their year, type (State/central) and no. of sections as vals
    return DICTIONARY_OF_ACTS

if __name__ == "__main__":
    D = get_acts_by_states()
    import json 
    with open('acts_db.json','w') as f:
        json.dump(D,f,indent=4)
