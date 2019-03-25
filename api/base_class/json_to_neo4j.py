import json
from py2neo import Graph, authenticate, Node,Relationship
from env import ENV

# from dotenv import load
# import os

# load("graph.env")
# ENV = os.environ
'''
        This function converts the JSON file to a neo4j graph and stores it into the NEO4J browser.
'''
def import_to_neo4j(filename):
    print(ENV)
    authenticate(ENV["DB_URL"], ENV["DB_USERNAME"],ENV["DB_PASSWORD"]) # Accessing the NEO4J server
    graph = Graph()

    string_to_instance=dict()
    with open(filename,'r') as data_file:
        data = json.load(data_file)
        for node in data["nodes"]:
            a = Node(node["type"], id=node["id"])
            string_to_instance[node["id"]]=a
        for link in data["links"]:
            b = Relationship(string_to_instance[link["source"]],"MAPS TO",string_to_instance[link["target"]])
            graph.create(b)


def json_file():
    filename='LegalKnowledgeGraph.json'
    import_to_neo4j(filename)


if __name__ == "__main__":
    json_file()
