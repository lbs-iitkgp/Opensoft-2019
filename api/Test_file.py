import pickle as pk
import case_citings
import act_nodes
import catch
import successful_judge
from base_class.legal_graph import LegalKnowledgeGraph
import networkx as nx
import case_year
import act_section_parser
j = LegalKnowledgeGraph()


j = case_citings.citing(j)
j = catch.add_catch_subject(j)
j = act_nodes.act_add(j)
j = successful_judge.judge_to_case(j)

j = case_year.citing(j)
print(len(j.fetch_cases()))

CASE_ID_TO_FILE = dict()
def compute_mapping():
    with open("{}/doc_path_ttl_id.txt".format(ENV["DATASET_PATH"])) as f:
        for line in f.readlines():
            line = line.strip()
        
            file_name, title, case_id = line.split("-->")
            CASE_FILE_TO_ID[case_id] = file_name
compute_mapping()

for case in j.fetch_cases():
    case_file = CASE_ID_TO_FILE[case]
    acts = act_section_parser.fetch_all_acts_in_a_case(case_file)
    for act in acts:
        j.add_act(act)
        j.add_edge(act, case)

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
