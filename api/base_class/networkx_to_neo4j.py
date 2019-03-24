import json
from py2neo import Graph, authenticate, Node,Relationship
from env import ENV
from graph_io import import_graph

'''
	This function converts the Networkx DiGraph to a neo4j graph and stores it into the NEO4J browser.
'''
def import_to_neo4j():
	graph=import_graph('LegalKnowledgeGraph.json')
	# print(graph.number_of_nodes())
	# print(graph.number_of_edges())
	authenticate(ENV["DB_URL"], ENV["DB_USERNAME"],ENV["DB_PASSWORD"]) # Accessing the NEO4J server
	G = Graph()
	string_to_instance=dict()
	list_node=list(graph.nodes(data=True))
	for i in range(len(list_node)):
		a=Node(list_node[i][0],type=list_node[i][1]['type'])
		string_to_instance[list_node[i][0]]=a
	list_edges=list(graph.edges())
	for i in range(graph.number_of_edges()):
		b = Relationship(string_to_instance[list_edges[i][0]],"MAPS TO",string_to_instance[list_edges[i][1]])
		G.create(b)


if __name__ == "__main__":
	import_to_neo4j()