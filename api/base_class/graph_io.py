import json
from networkx.readwrite import json_graph
from itertools import chain, count
def export_graph(graph, filename):
    '''
    Helper function which exports a given graph to a json file
    '''

    graph_data = json_graph.node_link_data(graph)

    with open(filename, 'w') as f:
        json.dump(graph_data, f, indent=4)


def import_graph(filename):
    '''
    Helper function which imports a networkx graph from a given
    json file
    '''

    with open(filename, 'r') as file_name:
        imported_file = json.load(file_name)

    graph = json_graph.node_link_graph(imported_file)

    return graph
