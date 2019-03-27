import backend.graph_formation.add_cases
import backend.graph_formation.add_act_nodes
import backend.graph_formation.add_key_and_catch_words
import backend.graph_formation.add_judges
import backend.graph_formation.add_years
import backend.graph_formation.add_acts

from backend.graph_formation.base.legal_knowledge_graph import LegalKnowledgeGraph

from env import ENV

def prepare_graph():
    j = LegalKnowledgeGraph()
    # j = add_cases.citing(j)
    j = add_act_nodes.act_add(j)
    # j = add_key_and_catch_words.add_catch_subject(j)
    # j = add_judges.judge_to_case(j)
    # j = add_years.citing(j)
    j = add_acts.map_acts_with_cases(j)
    return(j)
