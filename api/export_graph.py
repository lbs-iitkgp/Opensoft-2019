'''
    Script to convert a networkx graph to a json file
    '''

import json
from networkx.readwrite import json_graph


class Export:

    def __init__(self, graph):
        self.export_graph(graph)

    def export_graph(self, graph):
        '''
            Helper function which exports a given graph to a json file
            '''
        exporting_file = json_graph.node_link_data(graph)
        
        with open('result.json', 'w') as file_exporting:
            json.dump(exporting_file, file_exporting, indent=4)
