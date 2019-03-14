import pickle as pk
import case_citings
import act_nodes
import catch
import successful_judge
from legal_graph import LegalKnowledgeGraph
import networkx as nx
j = LegalKnowledgeGraph()


j = case_citings.citing(j)
j = catch.add_catch_subject(j)
j = act_nodes.act_add(j)
j = successful_judge.judge_to_case(j)


nx.write_gpickle(j, "LegalKnowledgeGraph.gpickle")
# with open('LegalKnowledgeGraph.pkl', 'w') as f:
    # pk.dump(j, f)

print(len(j.nodes()))
print(len(j.edges()))
print(j["V. Gopala Gowda J."])
print(j.in_edges("V. Gopala Gowda J."))

print(j["judgeless"])
print(len(j["judgeless"]))
