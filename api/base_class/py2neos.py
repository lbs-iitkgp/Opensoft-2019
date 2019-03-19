import json
from py2neo import Graph, authenticate, Node,Relationship
from graph_io import import_graph
from subgraph import graph_query

# replace 'foobar' with your password
authenticate("localhost:7474", "neo4j", "12345")
graph = Graph()

# a = Node("Person", name="Alice")
# graph.create(a)
# print(graph)
string_to_instance=dict()

#nx_graph = import_graph('LegalKnowledgeGraph.json')
#nx_graph_2 = graph_query(nx_graph, judges=["Hans Raj Khanna J."], subjects=[], keywords=[], judgements=[], types=[], year_range=[])

#data = nx_graph_2.nodes(data=True)
#for n in nx_graph_2:
#    print(data[n]["type"], n)
#    a = Node(data[n]["type"], id=n)
#    # print(n)
#    string_to_instance[n] = a

#for n in nx_graph_2:
#    for neigh in nx_graph_2[n]:
#        print(n, neigh, n in string_to_instance, neigh in string_to_instance)
#        b = Relationship(string_to_instance[n], "MAPS TO", string_to_instance[neigh])
#        graph.create(b)

with open('LegalKnowledgeGraph.json','r') as data_file:
        data = json.load(data_file)
        for node in data["nodes"]:
                a = Node(node["type"], id=node["id"])
                string_to_instance[node["id"]]=a
 #              graph.create(a)
        for link in data["links"]:
                b = Relationship(string_to_instance[link["source"]],"MAPS TO",string_to_instance[link["target"]])
                graph.create(b)
#for record in graph.cypher.execute("MATCH (c:case) RETURN c.id AS id"):
# print(record.id)
#results = graph.cypher.execute("MATCH (n:Person) RETURN n")

# query = """
# with {data} as document
# UNWIND document.nodes as nodes
# MERGE (:)
# """

# # Send Cypher query.
# print(graph.cypher.execute(query, data = data))