'''
    Script to convert a json-file to a networkx graph
    '''

import json
from networkx.readwrite import json_graph


class Import:

    def __init__(self, filename):
        self.import_file(filename)

    def import_file(self, filename):
        '''
            Helper function which imports from a given graph json file, a networkx graph
            '''
        with open(filename, 'r') as file_name:
            imported_file = json.load(file_name)

        graph = json_graph.node_link_graph(imported_file)

        return graph
