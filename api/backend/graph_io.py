from backend.graph_formation.base.legal_knowledge_graph import LegalKnowledgeGraph
from env import ENV

import json
from networkx.readwrite import json_graph
from itertools import chain, count
from py2neo import Graph, authenticate, Node, Relationship
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
import networkx as nx

def lkg_to_json(lkg, filename):
    """
    Helper function which exports a LegalKnowledgegraph to a json file
    """

    nx_graph = lkg_to_nx(lkg)
    nx_to_json(nx_graph, filename)

def lkg_to_neo4j(lkg):
    """
    This function converts a LegalKnowledgeGraph to a neo4j graph and stores it into the NEO4J browser.
    """

    nx_graph = lkg_to_nx(lkg)
    nx_to_neo4j(nx_graph)

def lkg_to_nx(lkg):
    nx_graph = nx.DiGraph()
    nx_graph.add_nodes_from(lkg.nodes(data=True))
    nx_graph.add_edges_from(lkg.edges())
    return(nx_graph)
    
def nx_to_lkg(nx_graph):
    lkg = LegalKnowledgeGraph()
    lkg.add_nodes_from(graph.nodes(data=True))
    lkg.add_edges_from(graph.edges())
    return(lkg)

def nx_to_neo4j(nx_graph=None):
    """
    This function converts the Networkx DiGraph to a neo4j graph and stores it into the NEO4J browser.
    """

    if not nx_graph:
        nx_graph = json_to_nx("LegalKnowledgeGraph.json")
    authenticate(ENV["DB_URL"], ENV["DB_USERNAME"],ENV["DB_PASSWORD"]) # Accessing the NEO4J server
    neo4j_graph = Graph()
    string_to_instance_mapping = dict()

    list_node = list(nx_graph.nodes(data=True))
    for i in range(len(list_node)):
        node_instance = Node(list_node[i][1]["type"], id=list_node[i][0])
        string_to_instance_mapping[list_node[i][0]] = node_instance

    list_edges=list(nx_graph.edges())
    for i in range(graph.number_of_edges()):
        source_node_instance = string_to_instance_mapping[list_edges[i][0]]
        target_node_instance = string_to_instance_mapping[list_edges[i][1]]
        b = Relationship(source_node_instance, "MAPS TO", target_node_instance)
        neo4j_graph.create(b)

def nx_to_json(graph, filename):
    """
    Helper function which exports a NetworkX DiGraph to a json file
    """
    graph_data = json_graph.node_link_data(graph)

    with open(filename, "w") as f:
        json.dump(graph_data, f, indent=4)

def json_to_nx(filename):
    """
    Helper function which imports a networkx graph from a given
    json file
    """

    with open(filename, "r") as file_name:
        imported_file = json.load(file_name)

    nx_graph = json_graph.node_link_graph(imported_file)

    return(nx_graph)

def json_to_lkg(filename):
    """
    Helper function which imports a LegalKnowledgeGraph from a given
    json file
    """

    nx_graph = json_to_nx(filename)
    lkg = nx_to_lkg(nx_graph)
    return(lkg)

def json_to_neo4j(filename):
    """
    This function converts the JSON file to a neo4j graph and stores it into the NEO4J browser.
    """
    authenticate(ENV["DB_URL"], ENV["DB_USERNAME"],ENV["DB_PASSWORD"]) # Accessing the NEO4J server
    neo4j_graph = Graph()
    string_to_instance_mapping = dict()

    with open(filename, "r") as f:
        json_data = json.load(f)
        for node in json_data["nodes"]:
            node_instance = Node(node["type"], id=node["id"])
            string_to_instance_mapping[node["id"]] = node_instance
        for link in json_data["links"]:
            source_node_instance = string_to_instance_mapping[link["source"]]
            target_node_instance = string_to_instance_mapping[link["target"]]
            edge = Relationship(source_node_instance, "MAPS TO", target_node_instance)
            neo4j_graph.create(edge)

def neo4j_to_lkg():
    """
    This function reads the NEO4J graph stored in the neo4j browser and converts it into a networkx graph
    """
    node_types = ["judge", "keyword", "case", "catch"]
    lkg = LegalKnowledgeGraph()
    db = GraphDatabase(ENV["DB_URL"], username=ENV["DB_USERNAME"], password=ENV["DB_PASSWORD"])
    # Authentication for NEO4J Browser

    for node_type in node_types:
        q = "MATCH (c:{}) return c".format(node_type)   #Quering for all nodes in the graph
        results = db.query(q)
        for record in results:
            props={}
            node = record[0]
            if node:
                label = node["metadata"]["labels"]
                node_id = node["data"]["id"]
                node["data"].pop("id",None)
                props = node["data"]
                props["type"] = label
                graph.add_node(id, **props)
    for node_type_1 in node_types:
        for node_type_2 in node_types:
            q = "MATCH (c:{})-[r]->(m:{}) return c,m".format(node_type_1, node_type_2) # Quering for all Relationships in the graph
            results = db.query(q)
            for record in results:
                node1 , node2 = record
                lkg.add_edge(node1["data"]["id"], node2["data"]["id"])
    return(lkg)

def neo4j_to_nx():
    lkg = neo4j_to_lkg()
    nx_graph = lkg_to_nx(lkg)
    return(nx_graph)

def neo4j_to_json(filename):
    lkg = neo4j_to_lkg()
    lkg_to_json(lkg, filename)
