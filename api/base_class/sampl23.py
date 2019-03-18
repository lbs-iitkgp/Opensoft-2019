import neonx
import networkx as nx
from graph_sample import graph as leGgraph
import json

G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edge(1, 2)
G.add_edge(2, 3)

def get_node(node_id, properties):

    return {"method": "POST",
            "to": "/node",  
            "id": node_id,
            "body": properties}

def get_label(i, label):
    """adds a label to the given (Neo4j) node.

    :param i: the index of a NetworkX node
    :param label: the label to be added to the node
    :rtype: a dictionary representing a Neo4j POST request
    """
    return {"method": "POST",
            "to": "{{{0}}}/labels".format(i),
            "body": label}

def get_relationship(from_id, to_id, rel_name, properties):

    body = {"to": "{{{0}}}".format(to_id), "type": rel_name,
            "data": properties}

    return {"method": "POST",
            "to": "{{{0}}}/relationships".format(from_id),
            "body": body}


def generate_data(graph, edge_rel_name, label, encoder):
    is_digraph = isinstance(graph, nx.DiGraph)
    entities = []
    nodes = {}

    for i, (node_name, properties) in enumerate(graph.nodes(data=True)):
        entities.append(get_node(i, properties))
        nodes[node_name] = i

    if label:
        for i in nodes.values():
            entities.append(get_label(i, label))

    for from_node, to_node, properties in graph.edges(data=True):
        edge = get_relationship(nodes[from_node], nodes[to_node],
                                edge_rel_name, properties)
        entities.append(edge)

        if not is_digraph:
            reverse_edge = get_relationship(nodes[to_node],
                                            nodes[from_node],
                                            edge_rel_name, properties)
            entities.append(reverse_edge)

    # print(entities)
    # for i in entities:
    #     try:
    #         encoder.encode(i)
    #     except Exception as e:
    #         print("Error here")
    #         print(i)
    #         break
    # return entities
    return encoder.encode(entities)


encoder = json.JSONEncoder()

#all_server_urls = get_server_urls(server_url)
#batch_url = all_server_urls['batch']

data = generate_data(G, "LINKS_TO", label='CASE', encoder=encoder)
#data = generate_data(leGgraph, "LINKS_TO", label='CASE', encoder=encoder)


#data = neonx.get_geoff(graph, "LINKS_TO")
results = neonx.write_to_neo("http://localhost:7474/db/data/", G, 'LINKS_TO','CASE')