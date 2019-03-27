"""This is our graph-helper file
    it defines LKG class with many methods to
    help make the LKG directed graph"""

import networkx as nx
from backend.graph_formation.base.judge import Judge
from backend.graph_formation.base.case import Case
from backend.graph_formation.base.subgraph import graph_query

class LegalKnowledgeGraph(nx.DiGraph):  # LKG class
    """class with methods to build/help_build
        the Legal_Knowledge_Graph which inherits nx.DiGraph
            for keeping LKG also a directed one """

    def to_nx(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(self.nodes(data=True))
        graph.add_edges_from(self.edges())
        return(graph)

    
    def from_nx(self, graph):
        self.add_nodes_from(graph.nodes(data=True))
        self.add_edges_from(graph.edges())
    
    def add_key_node(self, keyword):
        """method to add keyword type node"""

        self.add_node(keyword, type='keyword')

    def add_key_word_to_case(self, key_word, case):
        """method to add edge from
            key_word type node to case type node"""

        self.add_key_node(key_word)
        self.add_edge(key_word, case)
        self.add_case(case)

    def add_catch_node(self, catch):
        """method to add catch type node"""

        self.add_node(catch, type='catch')

    def add_catch_to_case(self, case, catch):
        """method to add edge from
            case type node to catch type node"""

        self.add_case(case)
        self.add_catch_node(catch)
        self.add_edge(catch, case)

    def add_act(self, act):
        """method to add act type node"""

        self.add_node(act, type='act')

    def add_case(self, case):
        """method to add case type node"""

        self.add_node(case, type='case')

    def add_judge(self, judge):
        """method to add judge type node"""

        self.add_node(judge, type='judge')

    def add_edge_judge_case(self, judge, case_id):
        """method to add edge from judge to case_id
        of cases he has worked on"""

        self.add_judge(judge)
        self.add_case(case_id)
        self.add_edge(judge, case_id)

    def add_citings(self, from_case_id, to_case_id):
        """adds edge from cited case's id(from case)
            to citing case's id(to case) """

        self.add_case(from_case_id)
        self.add_case(to_case_id)
        self.add_edge(from_case_id, to_case_id)

    def fetch_type(self, node_type):
        matching_nodes = [node for (node, data) in self.nodes(data=True) if data['type'] == node_type]
        return(matching_nodes)

    def fetch_judges(self):
        return(self.fetch_type('judge'))

    def fetch_cases(self):
        return(self.fetch_type('case'))

    def fetch_acts(self):
        return(self.fetch_type('act'))

    def fetch_catchwords(self):
        return(self.fetch_type('catch'))

    def fetch_keywords(self):
        return(self.fetch_type('keyword'))

    def query(self, **query_params):
        return(graph_query(self, **query_params))
