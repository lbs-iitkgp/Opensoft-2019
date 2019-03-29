
from endpoints import *


def provide_line_distribution(judges,judgements,subjects,keywords,years,types,nx_graph):
    params = {
        'judges' : judges,
        'judgements' : judgements,
        'subjects' : subjects,
        'keywords' : keywords,
        'year_range' : years,
        'types' : types
    }
    subgraph = graph_query(nx_graph, params)
    result=[]
    for i in range (1947,2020):
        result.append({i: 0})
    for node in subgraph['nodes']:
        case = mongo_db.find({"case_id":node['case_id']})
        result[int(case['year'])] = result[int(case['year'])]+1
    return jsonify(result)


def provide_cases(judges,judgements,subjects,keywords,years,types,nx_graph):
    params = {
        'judges' : judges,
        'judgements' : judgements,
        'subjects' : subjects,
        'keywords' : keywords,
        'year_range' : years,
        'types' : types
    }
    subgraph = graph_query(nx_graph, params)
    result = []
    for node in subgraph['nodes']:
        case = mongo_db.find({"keyword":node['keyword']})
        point = {
            "case_id": case['case_id'],
            "case_name": case['case_name'],
            "case_indlaw_id": case['case_indlawid'],
            "case_judges": case['judge'],
            "case_judgement": case['judgement'],
            "case_date": case['case_date'],
            "case_year": case['case_year'],
            "case_subjects": case['subjects'],
            "case_keywords": case['keywords']
            }
        result.append(point)
    return jsonify(result)


def provide_metadata(judge,judgement,subject,keyword,year,type,nx_graph):
    # gives union of all the required values
    result = []
    query = mongo_db.find({"keyword_id":keyword_id})  


def get_metas_to_node(id, node_type, meta_type, split = True):
    nodes = lkg.nodes(data=True)
    ids = []
    for meta,_ in lkg.in_edges("{}_{}".format(node_type, id)):
        if nodes[meta]["type"] == meta_type:
            if split:
                ids.append(meta.split('_')[1])
            else:
                ids.append(mets)
    return ids


def get_metas_from_node(id, node_type, meta_type, split = True):
    nodes = lkg.nodes(data=True)
    ids = []
    for meta,_ in lkg.out_edges("{}_{}".format(node_type, id)):
        if nodes[meta]["type"] == meta_type:
            if split:
                ids.append(meta.split('_')[1])
            else:
                ids.append(meta)
    return ids

