import pickle as pk
import case_citings
import act_nodes
import catch
import successful_judge
from base_class.legal_graph import LegalKnowledgeGraph
import networkx as nx

def get_graph():

    j = LegalKnowledgeGraph()


    # j = case_citings.citing(j)
    # j = catch.add_catch_subject(j)
    # j = act_nodes.act_add(j)
    j = successful_judge.judge_to_case(j)

    # print(j.fetch_cases())

    # nx.write_gpickle(j, "LegalKnowledgeGraph.gpickle")
    # with open('LegalKnowledgeGraph.pkl', 'w') as f:
        # pk.dump(j, f)
    # print(j)
    # print(len(j.nodes()))
    # print(len(j.edges()))

    return j
