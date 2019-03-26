import json
import re
import acts_separated as asd
import difflib
from env import ENV
"""makes a dictionary with
    ACT names as keys and the list
        of all its "updated versions with year" tuples as values"""

ACT_TO_ALL_YEARS = dict()
primary = dict() #temporary funny dictonary
rem  = dict()
i = 1
another_final_new_dict = dict()
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
        another_final_new_dict[Act_name] = line

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
    ACT_RECENT_YEARS[another_final_new_dict[act]] = []
    # ACT_RECENT_YEARS[act + ' ' +  rem[act]] = []
    for another_act in ACT_TO_ALL_YEARS:
        #print(another_act)
        if another_act.find(act) == 0:
         #   print(another_act)
          #  print(act)
            [ACT_RECENT_YEARS[another_final_new_dict[act]].append((x[0], another_final_new_dict[x[1]])) for x in ACT_TO_ALL_YEARS[another_act]] 
           # print(another_act)
# print(json.dumps(ACT_TO_ALL_YEARS, indent=4, sort_keys=True))
# print(ACT_RECENT_YEARS["Andhra Pradesh General Sales Tax (Second Amendment)"])
# print((ACT_RECENT_YEARS["Andhra Pradesh General Sales Tax"]))

STATE_WISE_ACTS = asd.get_acts_by_states()

def which_state_are_you_from(given_act_name):
    for akt in STATE_WISE_ACTS:
        for more_akts in STATE_WISE_ACTS[akt]:    
            if given_act_name == more_akts["act"]:
                return more_akts["type"]


# def fetch_all_acts_from_txt():
#     file = open("{}/Acts/all_acts_central_state.txt".format(ENV["DATASET_PATH"]), "r")
#     acts_list = []
#     for line in file:
#         line = line[:-1]
#         acts_list.append(line)
#     return acts_list

# def closest_actual_act(act_str):
#     all_acts = fetch_all_acts_from_txt()
#     if len(difflib.get_close_matches(act_str, all_acts, 5)) > 0:
#         possible = difflib.get_close_matches(act_str, all_acts, 5)
#         act_str = possible[0]
            
#     return act_str



another_new_dict = dict()
for _, act_versions in ACT_RECENT_YEARS.items():
    most_recent_act_year, most_recent_act_name = act_versions[-1]
    # most_recent_act = most_recent_act_name +", " + most_recent_act_year
    most_recent_act = most_recent_act_name
    for (act_year, act_name) in act_versions:
        # act = act_name + ", " + act_year
        act = act_name
        # act = closest_actual_act(act)
        # most_recent_act = closest_actual_act(most_recent_act)
        state_of_act = which_state_are_you_from(act)
        state_of_most_recent_act = which_state_are_you_from(most_recent_act)
        print(state_of_act)
        print(state_of_most_recent_act)
        if act not in another_new_dict and state_of_act == state_of_most_recent_act:
            another_new_dict[act] = most_recent_act

    # for every_act in an_act:
    #     another_new_dict[every_act[1]]=[every_act[0] max(an_act)]





with open('ACTS_TO_ALL_YEARS_u_u2.json','w') as f:
    json.dump(another_new_dict,f,indent=4)
