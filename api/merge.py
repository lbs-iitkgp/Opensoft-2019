'''
    This module merges the ACTS_TO_ALL_YEARS (The file having all years of all the acts)
        and ACTS_BY_STATES (The file grouping acts by their origin i.e. state/central)
        '''
from acts_updates import get_all_versions_of_all_acts
from acts_separated import get_acts_by_states

def get_acts_details():

    GROUPED_BY_STATES_FILE = get_acts_by_states()
    ALL_ACTS_FILE = get_all_versions_of_all_acts()

    RESULT_DICT = {}    # Stores the final dict of act keys and values as all its details

    ''' Iterates through the two dicts having 
            acts sep. by groups and acts sep. by amendments and merges the ones with same keys
        '''
    for key_1 in ALL_ACTS_FILE:
        for key_2 in GROUPED_BY_STATES_FILE:
            if key_1 == key_2:
                RESULT_DICT[key_1] = ALL_ACTS_FILE[key_1]
                RESULT_DICT[key_1].append(GROUPED_BY_STATES_FILE[key_1])
                RESULT_DICT[key_1].append(max(GROUPED_BY_STATES_FILE[key_1]))


    ''' Leftover acts which were in one dict but not in other put in the final dict separately
        '''
    for key in ALL_ACTS_FILE:
        if key not in RESULT_DICT:
            RESULT_DICT[key] = ALL_ACTS_FILE[key]

    for key in GROUPED_BY_STATES_FILE:
        if key not in RESULT_DICT:
            RESULT_DICT[key] = GROUPED_BY_STATES_FILE[key]

    # CNT = 0
    # for key in RESULT_DICT:
    #     CNT += 1
    # print(CNT)

    return RESULT_DICT
