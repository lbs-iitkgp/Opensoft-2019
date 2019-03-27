# ==============================================================================|
# TO DO :                                                                       |
# ==============================================================================|
# Acts :Serial_id, name, to state/year, act_file.name, Page rank score          |DONE
# ==============================================================================|
# Acts ka updated versions: Serial_id1 to Serial_id2                            |###################
# ==============================================================================|
# Judge :serial_id, ka Name, No.of cases, Page rank score                       |
# ==============================================================================|
# Cases :serial_id, file name , indlaw , title, date, judgement, Page rank score|DONE
# ==============================================================================|
# catch words, key words     , act ka abbreviations (Done)                      |##############3
# ==============================================================================|
#IMPORT REQUIRED 
import json
import pymongo
import base64
import acts_updates
import acts_separated
from encode_helper import custom_encode, custom_decode
import os
import case_ka_data_nikal as ckdn
from env import ENV
import mongodb_handler as handler
import abbreviation
from base_class.legal_graph import LegalKnowledgeGraph

#====================================================================================================================================
#ASSIGNS_MONGO_COLLECTIONS
acts_collection = "acts_ka_db"
future_acts_collection = "future_acts_ka_db"
cases_collection = "cases_ka_db"
abbreviations_collection = "abbreviations_ka_db"

#====================================================================================================================================
#DEFINE_FUNCTIONS_TO_PROCESS_VARIOUS_DATAS
def process_cases_data():
    
    ALL_CASE_FILES = os.listdir("{}/CaseDocuments/All_FT".format(ENV["DATASET_PATH"]))

    ALL_CASES = [filename for filename in ALL_CASE_FILES if filename[-4:] == ".txt"][:100]  # restricts to first 100 cases for now
    ckdn.compute_mapping()
    l = []
    # l_encoded = []
    for case in ALL_CASES:
        temp_dict = dict()
        ckdn.serial_id += 1
        temp_dict[str(ckdn.serial_id)] = ckdn.citing(case)
        l.append(temp_dict)
    final_case_data_dictonaries_list= []
    for cases in l:
        for case in cases:
            case_dict = {
                "serial" : case,
                "file_name" : cases[case][0],
                "indlaw_ID" : cases[case][1],
                "title" : cases[case][2],
                "date" : cases[case][3],
                "judgement" : cases[case][4],
                "pagerank" : "Page Rank Score",
            }

            final_case_data_dictonaries_list.append(case_dict)
    return final_case_data_dictonaries_list


def process_future_acts_data(act_wise_data_list):
    temp_list = []
    mapping = acts_updates.get_all_versions_of_all_acts()   # a dictionary act: newest act
    
    for act in act_wise_data_list:
        temp_dict= {}
        new_act_name = acts_updates.get_latest_version_of_an_act(act["act"], mapping)
        if new_act_name:
            temp_dict[str(act["serial"])] = act_serial_mapping[new_act_name]
            temp_list.append(temp_dict)

    return temp_list



#====================================================================================================================================
#CALLS_PROCESSING FUNCTIONS and DOES OTHER PROCESSING if needed
processed_case_data = process_cases_data()
processed_abbreviations_data = abbreviation.get_abbreviations()

acts_ka_data = acts_separated.get_acts_by_states()

s_acts_ka_data = []

for x in acts_ka_data:
    for phew in acts_ka_data[x]:
        s_acts_ka_data.append(phew)

act_serial_mapping = {act["act"]: act["serial"] for act in s_acts_ka_data}
processed_future_acts_data = process_future_acts_data(s_acts_ka_data)



#====================================================================================================================================
#ADDS_DATA_TO_VARIOUS_COLLECTIONS
handler.write_all(processed_abbreviations_data, abbreviations_collection)
handler.write_all(s_acts_ka_data, acts_collection)
handler.write_all(processed_case_data, cases_collection)
handler.write_all(processed_future_acts_data, future_acts_collection)
