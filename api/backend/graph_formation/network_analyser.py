from backend.graph_io import json_to_lkg
import networkx as nx

# Compute pagerank score
def set_pagerank_scores_for_all_cases(j=None):
    if not j:
        j = json_to_lkg("LKG.json")
    print("Imported lkg")
    j = j.query(judges=[], subjects=[], keywords=[], judgements=[], types=['case'], year_range=[])
    print("Filtered lkg")
    pagerank_dict = nx.pagerank(j)
    print("pageranked lkg")
    return(pagerank_dict)
