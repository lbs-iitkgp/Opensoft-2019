import pickle as pk
import case_citings
import act_nodes
import catch
import successful_judge
from base_class.legal_graph import LegalKnowledgeGraph
import networkx as nx
import case_year

j = LegalKnowledgeGraph()


j = case_citings.citing(j)
j = catch.add_catch_subject(j)
j = act_nodes.act_add(j)
j = successful_judge.judge_to_case(j)

j = case_year.citing(j)
print(len(j.fetch_cases()))

# nx.write_gpickle(j, "LegalKnowledgeGraph.gpickle")
# with open('LegalKnowledgeGraph.pkl', 'w') as f:
    # pk.dump(j, f)
# print(j)
print(len(j.nodes()))
print(len(j.edges()))
# print(j["H. R. KHANNA"])
# print(j.in_edges("H. R. KHANNA"))

# print(j["judgeless"])
# print(len(j["judgeless"   ]))
