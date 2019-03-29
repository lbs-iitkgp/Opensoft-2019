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
from backend.graph_io import *
from backend.graph_formation.base.subgraph import graph_query
from backend.graph_formation import prepare_graph
from elasticsearch_utils.populate_ES import populate_ES, create_indices

# ====================================================================================================================================

# ASSIGNS_MONGO_COLLECTIONS
acts_collection = "act_db"
recent_acts_collection = "recent_act_db"
cases_collection = "case_db"
abbreviations_collection = "abbreviation_db"
judges_collection = "judge_db"
catch_collection = "catch_db"
keyword_collection = "keyword_db"
years_collection = "year_db"
# ====================================================================================================================================
# DEFINE_FUNCTIONS_TO_PROCESS_VARIOUS_DATAS

def process_years(graph):

    nodes = graph.nodes(data=True)
    year_list = graph_query(graph, judges=[], subjects=[], keywords=[], judgements=[], types=['year'], year_range=[])
    serial = 1
    year_list = year_list.nodes()
    year_list = list(year_list)
    year_list.sort()

    serial_to_year = []
    percentiles = graph.get_percentile('year')
    for year in year_list:
        serial_to_year.append({"name": year, "serial": serial, "percentile": percentiles[year], "no of cases": len(graph[year])})
        serial += 1
    print(len(year_list))
    return serial_to_year


def process_catch(graph):
    # catch_list = []
    # graph = Test_file.get_graph()
    nodes = graph.nodes(data=True)
    catch_list = graph_query(graph, judges=[], subjects=[], keywords=[], judgements=[], types=['catch'], year_range=[])
    serial = 1
    catch_list = catch_list.nodes()

    serial_to_catch = []
    percentiles = graph.get_percentile('catch')
    for catch in catch_list:
        serial_to_catch.append({"name": catch, "serial": serial, "percentile": percentiles[catch], "no of cases": len(graph[catch])})
        serial += 1
    return serial_to_catch

def process_keyword(graph):
    # keyword_list = []
    # graph = Test_file.get_graph()
    nodes = graph.nodes(data=True)
    keyword_list = graph_query(graph, judges=[], subjects=[], keywords=[], judgements=[], types=['keyword'], year_range=[])
    serial = 1
    keyword_list = keyword_list.nodes()

    serial_to_keyword = []
    percentiles = graph.get_percentile('keyword')
    for keyword in keyword_list:
        serial_to_keyword.append({"name": keyword, "serial": serial, "percentile": percentiles[keyword], "no of cases": len(graph[keyword])})
        serial += 1
    return serial_to_keyword


def process_cases_data(knowledgeGraph):
    '''
        Extracts all data related to all cases
    '''
    ALL_CASE_FILES = os.listdir("{}/All_FT".format(ENV["DATASET_PATH"]))

    ALL_CASES = [filename for filename in ALL_CASE_FILES if filename[-4:]
                 == ".txt" and filename[0] != "."][:100]  # restricts to first 100 cases for now
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
        # print(cases)
        for case in cases:
            # print(case)
            case_dict = {
                "serial": case,
                "file_name": cases[case][0],
                "indlaw_ID": cases[case][1],
                "name": cases[case][2],
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
        new_act_name = acts_updates.get_latest_version_of_an_act(act, mapping)
        if new_act_name:
            # temp_dict[str(act["serial"])] = act_serial_mapping[new_act_name]
            temp_list.append({"Old_id": str(act_wise_data_list[act]), "New_id": str(act_wise_data_list[new_act_name])})

    return temp_list


def process_judge_data(graph):
    '''
        Serializes the judge names and adds them to the db (mongodb)
    '''
    # judge_list = []
    # graph = Test_file.get_graph()
    nodes = graph.nodes(data=True)
    judge_list = graph_query(graph, judges=[], subjects=[], keywords=[], judgements=[], types=['judge'], year_range=[])
    serial = 1
    judge_list = judge_list.nodes()
    # print(judge_list)
    serial_to_judge = []
    percentiles = graph.get_percentile('judge')
    for judge in judge_list:
        serial_to_judge.append({"name": judge, "serial": serial, "percentile": percentiles[judge], "no of cases": len(graph[judge])})
        serial += 1
    return serial_to_judge


def update_legal_graph_with_serial_id(lkg):
    '''
        Updates the legalKnowledgeGraph generated after exporting to mongodb 
            with the names of judges as their serial ids
    '''
    
    node_types = ['judge', 'act', 'keyword', 'catch', 'year', 'case']
    # judge_list = []
    # graph = Test_file.get_graph()
    nx_graph = lkg_to_nx(lkg)
    nodes = lkg.nodes(data=True)
    mapping = {}

    for node_type in node_types:
        node_list = lkg.query(judges=[], subjects=[], keywords=[], judgements=[], types=[node_type], year_range=[])
        node_list = node_list.nodes()
        collection = node_type + '_db'

        results = handler.read_all(collection)
        for result in results:
            if node_type == 'case':
                old_node_name = result["indlaw_ID"]
            else:
                old_node_name = result["name"]
            new_node_name = node_type + "_" + str(result["serial"])
            mapping[old_node_name] = new_node_name
 
    nx_graph = nx.relabel_nodes(nx_graph, mapping)
    # print(nx_graph.nodes())
    lkg = nx_to_lkg(nx_graph)
    return lkg

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

# knowledgeGraph = json_to_lkg("LKG.json")

def write_everything_to_mongo_first(lkg):
    cases_data = process_cases_data(lkg)
    print("1")
    acts_data = process_acts_data(acts_separated.get_acts_by_states())
    print("2")
    act_serial_mapping = {act["name"]: act["serial"] for act in acts_data}
    print("3")
    judges_data = process_judge_data(lkg)
    print("4")
    acts_mapping = process_recent_acts_data(act_serial_mapping)
    print("5")

    abbr_data = abbreviation.get_abbreviations()

    handler.write_all(acts_data, acts_collection)
    print("6")
    handler.write_all(cases_data, cases_collection)
    print("Wrote cases")
    handler.write_all(acts_mapping, recent_acts_collection)
    print("Wrote mappings")
    # print(judges_data)
    handler.write_all(judges_data, judges_collection)
    print("Wrote judge")
    handler.write_all(abbr_data, abbreviations_collection)
    print("Wrote abbr")

    keywords = process_keyword(lkg)
    handler.write_all(keywords, keyword_collection)
    print("Wrote Keywords")

    # act_serial_mapping = {act["act"]: act["serial"] for act in acts_data}
    # print(act_serial_mapping)

    handler.write_all(process_years(lkg), years_collection)
    # print(process_years(knowledgeGraph))
    print("Wrote years")
    handler.write_all(process_catch(lkg), catch_collection)
    # print(process_catch(knowledgeGraph))
    print("Wrote catch")
    # collections = set()

def populate_elasticsearch():
    try:
        create_indices()
    except:
        pass
    collections = ['judge', 'case', 'act']
    for coll in collections:
        results = handler.read_all(coll+"_db")
        data_list = []
        for result in results:
            data_dict = {}
            data_dict["name"] = result["name"]
            data_dict["serial"] = int(result["serial"])
            data_list.append(data_dict)
        populate_ES(coll, data_list)

def main(lkg):
    write_everything_to_mongo_first(lkg)
    print("Updating lkg")
    lkg_new = update_legal_graph_with_serial_id(lkg)
    print("Updated lkg")
    lkg_to_neo4j(lkg_new)
    print("Written to neo4j")
    populate_elasticsearch()
    print("ES done")

if __name__ == "__main__":
    # lkg = prepare_graph()
    lkg = json_to_lkg("main_lkg.json")
    main(lkg)
