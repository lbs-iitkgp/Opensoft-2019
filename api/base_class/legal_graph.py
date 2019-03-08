import networkx as nx
from Judge_class import Judge
from Case_class import Case

class LegalKnowledgeGraph(nx.DiGraph):
    def add_key_node(self,keyword):
        self.add_node(keyword, type='keyword')
    
    def add_key_word_to_case(self,key_word, case):
        self.add_key_node(key_word)
        self.add_edge(key_word, case)
        self.add_case(case)
        
    def add_catch_node(self, catch):
        self.add_node(catch, type='catch')

    def add_catch_to_case(self, case, catch):
        self.add_case(case)
        self.add_catch_node(catch)
        self.add_edge(catch, case)

    def add_act(self, act):
        self.add_node(act, type='act')

    def add_case(self, case):
        # TODO: Abstract case and add more metadata support w/ categories
        self.add_node(case, type='case')

    def add_judge(self, judge):
        self.add_node(judge, type='judge')

    def add_edge_judge_case(self, input_json):
        for judge_name in input_json:
            judge_node = Judge(judge_name)
            for cases in input_json[judge_name]:
                case_node = Case(cases["Case"], cases["Title"], cases["Date"])
                self.graph.add_edge(judge_node, case_node)
    
    def add_citings(self, case1_id, case2_id):
        self.add_case(case1_id)
        self.add_case(case2_id)
        self.add_edge(case1_id, case2_id)

    # def add_citation(self, from_case, to_case):
    #     self.add_case(from_case)
    #     self.add_case(to_case)
    #     self.add_edge(from_case.uuid, to_case.uuid)

    