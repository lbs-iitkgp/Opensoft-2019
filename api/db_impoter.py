'''
    This script exports data to the two databases used mongo and neo4j (if needed).
        Different functions handle exporting different categories of data
    '''

# ==============================================================================|
#                               TO DO                                           |
# ==============================================================================|
# Acts :Serial_id, name, to state/year, act_file.name, Page rank score          |DONE
# ==============================================================================|
# Acts ka updated versions: Serial_id1 to Serial_id2                            |Done
# ==============================================================================|
# Judge :serial_id, ka Name, No.of cases, Page rank score (Pagerank left)       |Done
# ==============================================================================|
# Cases :serial_id, file name , indlaw , title, date, judgement, Page rank score|DONE
# ==============================================================================|
# catch words, key words (Clustering is very slow!), act ka abbreviations (Done)|
# ==============================================================================|
# IMPORT REQUIRED

import json
import pymongo
import base64
from db_importers import acts_updates
from db_importers import acts_separated
from db_importers import case_data_extractor as case_data
from env import ENV
from encode_helper import custom_encode, custom_decode
import os
import mongodb_handler as handler
from db_importers import abbreviation
import networkx as nx
from backend.graph_formation.network_analyser import set_pagerank_scores_for_all_cases 
from nlp.summarizer import nltk
from backend.graph_io import json_to_lkg, lkg_to_neo4j
from backend.graph_formation.base.subgraph import graph_query
# ====================================================================================================================================

# ASSIGNS_MONGO_COLLECTIONS
acts_collection = "act_db"
recent_acts_collection = "recent_act_db"
cases_collection = "case_db"
abbreviations_collection = "abbreviation_db"
judges_collection = "judge_db"
catch_collection = "catch_db"
keyword_collection = "keyword_db"
# ====================================================================================================================================
# DEFINE_FUNCTIONS_TO_PROCESS_VARIOUS_DATAS


def process_cases_data(knowledgeGraph):
    '''
        Extracts all data related to all cases
    '''
    ALL_CASE_FILES = os.listdir("{}/All_FT".format(ENV["DATASET_PATH"]))

    ALL_CASES = [filename for filename in ALL_CASE_FILES if filename[-4:]
                 == ".txt"][:100]  # restricts to first 100 cases for now
    case_data.compute_mapping()

    pagerank_scores = set_pagerank_scores_for_all_cases(knowledgeGraph)
    l = []
    for case in ALL_CASES:
        temp_dict = dict()
        case_data.serial_id += 1
        temp_dict[str(case_data.serial_id)] = case_data.citing(case)
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
                "pagerank": pagerank_scores[cases[case][1]],
                "summary": nltk.fetch_summary_for_case(cases[case][0])[0]
            }

            final_case_data_dictonaries_list.append(case_dict)
            
    return final_case_data_dictonaries_list


def process_acts_data(acts):
    acts_data = []
    acts_list = acts

    for act in acts_list:
        for act_details in acts_list[act]:
            acts_data.append(act_details)

    return acts_data

def process_recent_acts_data(act_wise_data_list):
    '''
        Gets the serial ids for all acts and maps an act id 
            with the id of the most recent amendment of it (if any)
    '''
    temp_list = []
    mapping = acts_updates.get_all_versions_of_all_acts()   # a dictionary act: newest act

    for act in act_wise_data_list:
        temp_dict = {}  
        new_act_name = acts_updates.get_latest_version_of_an_act(str(act["act"]), mapping)
        if new_act_name:
            # temp_dict[str(act["serial"])] = act_serial_mapping[new_act_name]
            temp_list.append({"Serial_id": str(act["serial"]), "new_act_name": str(act_serial_mapping[new_act_name])})

    return temp_list


def process_judge_data(graph):
    '''
        Serializes the judge names and adds them to the db (mongodb)
    '''
    judge_list = []
    # graph = Test_file.get_graph()
    nodes = graph.nodes(data=True)
    judge_list = graph_query(graph, judges=[], subjects=[], keywords=[], judgements=[], types=['judge'], year_range=[])
    serial = 1
    judge_list = judge_list.nodes()

    serial_to_judge = []

    for judge in judge_list:
        serial_to_judge.append({"judge_name": judge, "serial_id": serial})
        serial += 1
    return serial_to_judge


def update_legal_graph_with_serial_id(lkg):
    '''
        Updates the legalKnowledgeGraph generated after exporting to mongodb 
            with the names of judges as their serial ids
    '''
    
    node_types = ['judge', 'case', 'act', 'keyword', 'catch', 'year']
    # judge_list = []
    # graph = Test_file.get_graph()
    nodes = lkg.nodes(data=True)
    for node_type in node_types:
        node_list = lkg.query(judges=[], subjects=[], keywords=[], judgements=[], types=[node_type], year_range=[])
        node_list = node_list.nodes()

        mapping = {}
        serial = 1
        for node in node_list:
            mapping[node] = "{}_{}".format(node_type, serial)
            serial += 1

        nx_graph = nx.relabel_nodes(graph.to_nx(), mapping)
        graph = LegalKnowledgeGraph()
        graph.from_nx(nx_graph)
        print(graph.nodes())
    return graph

# def update_pagerank_score(knowledgeGraph):
#     pagerank_scores = set_pagerank_scores_for_all_cases(knowledgeGraph)
#     for indlaw_id, score in pagerank_scores.items():
#         case = handler.read_all(cases_collection, indlaw_ID=indlaw_id)
#         case["pagerank"] = score
#         handler.write(case, cases_collection)

# ====================================================================================================================================
# CALLS_PROCESSING FUNCTIONS and DOES OTHER PROCESSING if needed

# update_legal_graph_with_serial_id()


# processed_case_data = process_cases_data()
# processed_abbreviations_data = abbreviation.get_abbreviations()
# acts_ka_data = acts_separated.get_acts_by_states()



# act_serial_mapping = {act["act"]: act["serial"] for act in s_acts_ka_data}
# processed_recent_acts_data = process_recent_acts_data(s_acts_ka_data)

# processed_judge_data = processed_judge_data()

# ====================================================================================================================================
# ADDS_DATA_TO_VARIOUS_COLLECTIONS

# handler.write_all(processed_abbreviations_data, abbreviations_collection)
# handler.write_all(s_acts_ka_data, acts_collection)
# handler.write_all(processed_case_data, cases_collection)
# handler.write_all(processed_recent_acts_data, recent_acts_collection)
# handler.write_all(process_judge_data, judges_collection)
# =====================================================================================================================================

# DEBUGGING STATEMENTS

# lists = handler.read_all(recent_acts_collection)
# print(lists[:100])

# list1 = handler.read_all(acts_collection, serial=37)[0]
# list2 = handler.read_all(acts_collection, serial=98)[0]

# print(list1)
# print(list2)

# l = processed_judge_data()
# print(l)
# print(type(l))
# print(type(l[0]))

knowledgeGraph = json_to_lkg("LKG.json")

def main(lkg):
    # write_everything_to_mongo_first()
    # lkg = remap_node_values(lkg)
    # lkg_to_neo4j(lkg)

    # cases_data = process_cases_data(knowledgeGraph)
    # acts_data = process_acts_data(acts_separated.get_acts_by_states())
    # act_serial_mapping = {act["act"]: act["serial"] for act in acts_data}
    # judges_data = process_judge_data(knowledgeGraph)
    # acts_mapping = process_recent_acts_data(act_serial_mapping)

    abbr_data = abbreviation.get_abbreviations()

    # handler.write_all(acts_data, acts_collection)
    # print("Wrote acts")
    # handler.write_all(cases_data, cases_collection)
    # print("Wrote cases")
    # handler.write_all(act_serial_mapping, recent_acts_collection)
    # handler.write_all(judges_data, judges_collection)
    # print("Wrote judge")
    # handler.write_all(acts_mapping, recent_acts_collection)
    handler.write_all(abbr_data, abbreviations_collection)
    print("Wrote abbr")


main(knowledgeGraph)