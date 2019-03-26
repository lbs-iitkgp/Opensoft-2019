import json
import re
import acts_separated as asd
from env import ENV
"""makes a dictionary with
    ACT names as keys and the list
        of all its "updated versions with year" tuples as values"""

ACT_TO_ALL_YEARS = dict()
primary = dict() #temporary funny dictonary
rem  = dict()
i = 1
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

        rem[Act_name] = removed
        # print(Act_name)

        if Act_name in ACT_TO_ALL_YEARS:
            ACT_TO_ALL_YEARS[Act_name].append((year, Act_name,))
        else:
            ACT_TO_ALL_YEARS[Act_name] = []
            ACT_TO_ALL_YEARS[Act_name].append((year, Act_name,))

        # return rem

ACT_RECENT_YEARS = {}

for act in ACT_TO_ALL_YEARS:
    ACT_RECENT_YEARS[act + ' ' +  rem[act]] = []
    for another_act in ACT_TO_ALL_YEARS:
        print(another_act)
        if another_act.find(act) == 0:
            print(another_act)
            print(act)
            [ACT_RECENT_YEARS[act + ' ' +  rem[act]].append((x[0], x[1] + ' ' + rem[x[1]])) for x in ACT_TO_ALL_YEARS[another_act]] 
            print(another_act)
# print(json.dumps(ACT_TO_ALL_YEARS, indent=4, sort_keys=True))
# print(ACT_RECENT_YEARS["Andhra Pradesh General Sales Tax (Second Amendment)"])
# print((ACT_RECENT_YEARS["Andhra Pradesh General Sales Tax"]))

STATE_WISE_ACTS = asd.get_acts_by_states()

def which_state_are_you_from(given_act_name):
    for act_serial in STATE_WISE_ACTS:
        print(STATE_WISE_ACTS[act_serial])
        if given_act_name == STATE_WISE_ACTS[act_serial]["act"]:
            return STATE_WISE_ACTS[act_serial][""]


another_new_dict = dict()
for _, act_versions in ACT_RECENT_YEARS.items():
    most_recent_act_year, most_recent_act_name = act_versions[-1]
    most_recent_act = most_recent_act_name +", " + most_recent_act_year
    for (act_year, act_name) in act_versions:
        act = act_name + ", " + act_year
        state_of_act = which_state_are_you_from(act)
        state_of_most_recent_act = which_state_are_you_from(most_recent_act)
        print(state_of_act)
        print(state_of_most_recent_act)
        if act not in another_new_dict and state_of_act == state_of_most_recent_act:
            another_new_dict[act] = most_recent_act

    # for every_act in an_act:
    #     another_new_dict[every_act[1]]=[every_act[0] max(an_act)]





with open('ACTS_TO_ALL_YEARS_u.json','w') as f:
    json.dump(another_new_dict,f,indent=4)