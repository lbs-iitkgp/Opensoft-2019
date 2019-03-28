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
    print("Init graph")
    j = add_cases.citing(j)
    print("Citings added")
    j = add_act_nodes.act_add(j)
    print("Acts added")
    j = add_key_and_catch_words.add_catch_subject(j)
    print("Catch/Keyword added")
    j = add_judges.judge_to_case(j)
    print("Judges added")
    j = add_years.citing(j)
    print("Years added")
    j = add_acts.map_acts_with_cases(j)
    return(j)
