'''
    This module merges the ACTS_TO_ALL_YEARS (The file having all years of all the acts)
        and ACTS_BY_STATES (The file grouping acts by their origin i.e. state/central)
        '''

import json

with open('ACTS_TO_ALL_YEARS.json', 'r') as f:
    ALL_ACTS_FILE = json.load(f)
with open('ACTS_BY_STATES.json', 'r') as g:
    GROUPED_BY_STATES_FILE = json.load(g)

RESULT_DICT = {}

for key_1 in ALL_ACTS_FILE:
    for key_2 in GROUPED_BY_STATES_FILE:
        if key_1 == key_2:
            RESULT_DICT[key_1] = ALL_ACTS_FILE[key_1]
            RESULT_DICT[key_1].append(GROUPED_BY_STATES_FILE[key_1])
            RESULT_DICT[key_1].append(max(GROUPED_BY_STATES_FILE[key_1]))

for key in ALL_ACTS_FILE:
    if key not in RESULT_DICT:
        RESULT_DICT[key] = ALL_ACTS_FILE[key]

for key in GROUPED_BY_STATES_FILE:
    if key not in RESULT_DICT:
        RESULT_DICT[key] = GROUPED_BY_STATES_FILE[key]

CNT = 0
for key in RESULT_DICT:
    CNT += 1
print(CNT)

with open('result_2.json', 'w') as res:
    json.dump(RESULT_DICT, res, indent=4)
