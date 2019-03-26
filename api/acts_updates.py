import json
import acts_separated as asd
from env import ENV
"""makes a dictionary with
    ACT names as keys and the list
        of all its "updated versions with year" tuples as values"""

def get_all_versions_of_all_acts():

    ACT_TO_ALL_YEARS = dict()
    ACT_MAPPING_TO_FULL_NAME = dict()
    with open('{}/actlist.txt'.format(ENV["DATASET_PATH"])) as f:

        for line in f.readlines():
            line = line.strip()
            Act_name, year = line[:-4], line[-4:]
            Act_name = Act_name.strip()
            removed = ''
            if "," in Act_name:
                Act_name = Act_name[:Act_name.index(
                    ",")] + Act_name[Act_name.index(",")+1:]

            if 'Act' in Act_name:
                removed = 'Act'
                Act_name = Act_name[:Act_name.rindex('Act')]

            if 'act' in Act_name:
                removed = 'act'
                Act_name = Act_name[:Act_name.rindex('act')]

            Act_name = Act_name.strip()
            ACT_MAPPING_TO_FULL_NAME[Act_name] = line


            if Act_name in ACT_TO_ALL_YEARS:
                ACT_TO_ALL_YEARS[Act_name].append((year, Act_name,))
            else:
                ACT_TO_ALL_YEARS[Act_name] = []
                ACT_TO_ALL_YEARS[Act_name].append((year, Act_name,))

    RECENT_VERSIONS_OF_ACTS = {}

    for act_1 in ACT_TO_ALL_YEARS:
        RECENT_VERSIONS_OF_ACTS[ACT_MAPPING_TO_FULL_NAME[act_1]] = []
        for act_2 in ACT_TO_ALL_YEARS:
            if act_2.find(act_1) == 0:
                [RECENT_VERSIONS_OF_ACTS[ACT_MAPPING_TO_FULL_NAME[act_1]].append((x[0], ACT_MAPPING_TO_FULL_NAME[x[1]])) for x in ACT_TO_ALL_YEARS[act_2]] 

    STATE_WISE_ACTS = asd.get_acts_by_states()

    def which_state_are_you_from(given_act_name):
        for act in STATE_WISE_ACTS:
            for more_acts in STATE_WISE_ACTS[act]:    
                if given_act_name == more_acts["act"]:
                    return more_acts["type"]

    MOST_RECENT_VERSION = dict()
    for _, act_versions in RECENT_VERSIONS_OF_ACTS.items():
        most_recent_act_year, most_recent_act_name = act_versions[-1]
        most_recent_act = most_recent_act_name
        for (act_year, act_name) in act_versions:
            act = act_name
            state_of_act = which_state_are_you_from(act)
            state_of_most_recent_act = which_state_are_you_from(most_recent_act)
            print(state_of_act)
            print(state_of_most_recent_act)
            if act not in MOST_RECENT_VERSION and state_of_act == state_of_most_recent_act:
                MOST_RECENT_VERSION[act] = most_recent_act

    return MOST_RECENT_VERSION

if __name__ == "__main__":
    with open('ACTS_TO_ALL_YEARS.json','w') as f:
        json.dump(get_all_versions_of_all_acts(),f,indent=4) 