# ==============================================================================|
#                               TO DO                                           |
# ==============================================================================|
# Acts :Serial_id, name, to state/year, act_file.name, Page rank score          |DONE
# ==============================================================================|
# Acts ka updated versions: Serial_id1 to Serial_id2                            |Done
# ==============================================================================|
# Judge :serial_id, ka Name, No.of cases, Page rank score                       |Done
# ==============================================================================|
# Cases :serial_id, file name , indlaw , title, date, judgement, Page rank score|DONE
# ==============================================================================|
# catch words, key words (Clustering is very slow!), act ka abbreviations (Done)|
# ==============================================================================|
# IMPORT REQUIRED
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
from base_class.subgraph import graph_query
import Test_file


# ====================================================================================================================================
# ASSIGNS_MONGO_COLLECTIONS
acts_collection = "acts_ka_db"
future_acts_collection = "future_acts_ka_db"
cases_collection = "cases_ka_db"
abbreviations_collection = "abbreviations_ka_db"
judges_collection = "judges_ka_db"
# ====================================================================================================================================
# DEFINE_FUNCTIONS_TO_PROCESS_VARIOUS_DATAS


def process_cases_data():

    ALL_CASE_FILES = os.listdir("{}/CaseDocuments/All_FT".format(ENV["DATASET_PATH"]))

    ALL_CASES = [filename for filename in ALL_CASE_FILES if filename[-4:]
                 == ".txt"][:100]  # restricts to first 100 cases for now
    ckdn.compute_mapping()
    l = []
    # l_encoded = []
    for case in ALL_CASES:
        temp_dict = dict()
        ckdn.serial_id += 1
        temp_dict[str(ckdn.serial_id)] = ckdn.citing(case)
        l.append(temp_dict)
    final_case_data_dictonaries_list = []
    for cases in l:
        for case in cases:
            case_dict = {
                "serial": case,
                "file_name": cases[case][0],
                "indlaw_ID": cases[case][1],
                "title": cases[case][2],
                "date": cases[case][3],
                "judgement": cases[case][4],
                "pagerank": "Page Rank Score",
            }

            final_case_data_dictonaries_list.append(case_dict)
    return final_case_data_dictonaries_list


def process_future_acts_data(act_wise_data_list):
    temp_list = []
    mapping = acts_updates.get_all_versions_of_all_acts()   # a dictionary act: newest act

    for act in act_wise_data_list:
        temp_dict = {}
        new_act_name = acts_updates.get_latest_version_of_an_act(act["act"], mapping)
        if new_act_name:
            # temp_dict[str(act["serial"])] = act_serial_mapping[new_act_name]
            temp_list.append({"Serial_id": act["serial"], "new_act_name": act_serial_mapping[new_act_name]})

    return temp_list


def processed_judge_data():
    judge_list = []
    graph = Test_file.get_graph()
    nodes = graph.nodes(data=True)
    # print(nodes)
    # judge_list = [node for node in nodes if nodes[node]['type'] == 'judge']
    # for node in nodes:
    #     print(node)
    judge_list = graph_query(graph, judges=[], subjects=[], keywords=[], judgements=[], types=['judge'], year_range=[])
    # print(judge_list.nodes())
    serial = 1
    judge_list = judge_list.nodes()

    serial_to_judge = []

    for judge in judge_list:
        serial_to_judge.append({"judge_name": judge, "serial_id": serial})
        serial += 1
    # judge_list_to_serial = []
    # for serial in serial_to_judge:
    #     judge_list_to_serial.append({str(serial):serial_to_judge[serial]})
    return serial_to_judge


# ====================================================================================================================================
# CALLS_PROCESSING FUNCTIONS and DOES OTHER PROCESSING if needed
processed_case_data = process_cases_data()
processed_abbreviations_data = abbreviation.get_abbreviations()
# print(processed_abbreviations_data)
acts_ka_data = acts_separated.get_acts_by_states()

s_acts_ka_data = []

for x in acts_ka_data:
    for phew in acts_ka_data[x]:
        s_acts_ka_data.append(phew)

act_serial_mapping = {act["act"]: act["serial"] for act in s_acts_ka_data}
processed_future_acts_data = process_future_acts_data(s_acts_ka_data)

process_judge_data = processed_judge_data()

# ====================================================================================================================================
# ADDS_DATA_TO_VARIOUS_COLLECTIONS

handler.write_all(processed_abbreviations_data, abbreviations_collection)
handler.write_all(s_acts_ka_data, acts_collection)
# handler.write_all(processed_case_data, cases_collection)
# handler.write_all(processed_future_acts_data, future_acts_collection)
# handler.write_all(process_judge_data, judges_collection)
# =====================================================================================================================================

# DEBUGGING STATEMENTS

# lists = handler.read_all(future_acts_collection)
# print(lists[:100])

# list1 = handler.read_all(acts_collection, serial=37)[0]
# list2 = handler.read_all(acts_collection, serial=98)[0]

# print(list1)
# print(list2)

# l = processed_judge_data()
# print(l)
# print(type(l))
# print(type(l[0]))
