# Makes subgraph of intersection of subgraphs of different query_params
# Also makes subgraph for a given query_param for all valcase values of it ex. subgraph of judges and cases w/out keywords etc

'''
todo : 
OK |Handle citations of cases -- Depends on data we get
OK |Populate the year range
OK |try-except-else block
OK |implement union --> (Done) and intersection --> (Done) --> BUT ! When to use what ?
OK |implement dfs --> Done /
'''

import json
import networkx as nx
# from generate_graph import GenerateGraph
# from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
from collections import defaultdict
# from base_class.graph_io import import_graph, export_graph


def merge_graphs_by_intersection(universal_graph, subgraphs):
    matching_nodes = set(universal_graph.nodes())

    for subgraph in subgraphs:
        matching_nodes = matching_nodes.intersection(set(subgraph.nodes()))

    return(universal_graph.subgraph(list(matching_nodes)))

def fetch_subgraph_from_matching_cases(graph, cases):
    data = graph.nodes(data=True)
    # print(data)
    meta_nodes = set()

    for case in cases:
        for meta_node in graph.in_edges(case):
            meta_node = meta_node[0]
            # print(meta_node)
            # if meta_node in data:
            #     print(data[meta_node]['type'])
            if meta_node in data and data[meta_node]['type'] != 'case':
                meta_nodes.add(meta_node)

    # print(meta_nodes)
    return(graph.subgraph(list(cases.union(meta_nodes))))

def fetch_subgraph_from_meta_nodes(graph, set_of_meta_nodes=set()):
    if not set_of_meta_nodes:
        return(graph)

    data = graph.nodes(data=True)
    matching_cases = set()

    for meta_node in set_of_meta_nodes:
        for case in graph[meta_node]:
            matching_cases.add(case)

    return(fetch_subgraph_from_matching_cases(graph, matching_cases))

# How exactly are case years stored in graph?
def fetch_subgraph_with_year_range(graph, years=set()):
    if not years:
        return graph

    data = graph.nodes(data=True)
    matching_cases = set()

    for case in graph.fetch_cases():
        if int(data[case]['year']) in years:
            matching_cases.add(case)

    return(fetch_subgraph_from_matching_cases(graph, matching_cases))

def fetch_subgraph_with_judges(graph, judges=set()):
    return(fetch_subgraph_from_meta_nodes(graph, judges))

def fetch_subgraph_with_subjects(graph, subjects=set()):
    return(fetch_subgraph_from_meta_nodes(graph, subjects))

# How exactly is judgement stored in graph?
def fetch_subgraph_with_judgements(graph, judgements=set()):
    # if not judgements:
    #     return graph

    # data = graph.nodes(data=True)
    # matching_cases = set()

    # for judgement in judgements:
    #     for case in graph[judgements]:
    #         matching_cases.add(case)

    # return(fetch_subgraph_from_matching_cases(matching_cases))
    return(fetch_subgraph_from_meta_nodes(graph, judgements))

def fetch_subgraph_with_keywords(graph, keywords=set()):
    return(fetch_subgraph_from_meta_nodes(graph, keywords))

# For extracting subgraphs of **only** some particular types like acts & judges etc...
def fetch_subgraph_with_types(graph, node_types=set()):
    if not node_types:
        return(graph)

    data = graph.nodes(data=True)
    matching_nodes = set()

    for node, data in graph.nodes(data=True):
        if data['type'] in node_types:
            matching_nodes.add(node)

    return(graph.subgraph(list(matching_nodes)))

def graph_query(G, **query_params):
    d = G.nodes(data=True)
    d = dict(d)
    specific_queries = set()

    gph_with_judges = fetch_subgraph_with_judges(G, query_params['judges'])
    gph_with_judgements = fetch_subgraph_with_judgements(G, query_params['judgements'])
    gph_with_subjects = fetch_subgraph_with_subjects(G, query_params['subjects'])
    gph_with_keywords = fetch_subgraph_with_keywords(G, query_params['keywords'])
    gph_with_year_range = fetch_subgraph_with_year_range(G, query_params['year_range'])
    gph_with_types = fetch_subgraph_with_types(G, query_params['types'])    

    result = merge_graphs_by_intersection(G, [gph_with_judges, gph_with_judgements, gph_with_subjects, gph_with_keywords, gph_with_year_range, gph_with_types])

    return(result)

'''
def printGraph(graph):
    pos = graphviz_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.show()
'''

def prepare_corpus_dist_file(graph, query_type):
    query_dist = dict()
    query_members = fetch_subgraph_with_types(graph, [query_type])
    for q in query_members:
        query_dist[q] = len(graph[q])
    query_dist = sorted(query_dist.items(), key=lambda k: k[1], reverse=True)
    with open("{}.json".format(query_type), 'w') as f:
        json.dump(query_dist, f, indent=4)

if __name__ == "__main__":

    # file = open('output.txt', 'r')
    # graph = GenerateGraph(file)
    # graph = graph.return_graph()
    from legal_graph import LegalKnowledgeGraph

    filename = "LegalKnowledgeGraph"
    graph = nx.read_gpickle("{}.gpickle".format(filename))
    export_graph(graph.to_nx(), "{}.json".format(filename))
    graph_2 = import_graph("{}.json".format(filename))

    # result = graph_query(graph, judges=[], subjects=[], keywords=[], judgements=[], types=['judge', 'case'], year_range=list(range(2002, 2005)))
    result = graph_query(graph_2, judges=[], subjects=[], keywords=[], judgements=[], types=['judge', 'keyword'], year_range=[])

    print(result.nodes())
    print("Criminal" in result.nodes())
    prepare_corpus_dist_file(graph_2, 'judge')
    prepare_corpus_dist_file(graph_2, 'keyword')
    prepare_corpus_dist_file(graph_2, 'act')
    prepare_corpus_dist_file(graph_2, 'catch')

    # print(result.fetch_cases())

    # query_params = defaultdict(set)
    # # query_params['judge'].add('gNn')
    # # query_params['judgement'].add('guilty')
    # # query_params['keyword'].add('3')
    # # query_params['subject'].add('KVJ')
    # # query_params['year'].add('2003')

    # result = graph_query(graph, query_params)
    # # print(result.nodes())
