from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
import networkx as nx
import matplotlib.pyplot as plt
from env import ENV
from legal_graph import LegalKnowledgeGraph

'''
    This function reads the NEO4J graph stored in the neo4j browser and converts it into a networkx graph
'''
def export_neo4j():
    types=['judge','keyword','case','catch']
    graph = LegalKnowledgeGraph()
    db = GraphDatabase(ENV["DB_URL"], username=ENV["DB_USERNAME"], password=ENV["DB_PASSWORD"]) # Authentication for NEO4J Browser
    for i in range(len(types)):
        print(types[i])
        q = 'MATCH (c:'+types[i]+') return c'   #Quering for all nodes in the graph
        results = db.query(q)
        for record in results:
            props={}
            node = record[0]
            if node:
                label=node['metadata']['labels']
                id=node['data']['id']
                node['data'].pop('id',None)
                props= node['data']
                props["type"] = label
                graph.add_node(id, **props)
            #  print(props)
    for i in range(len(types)):
        for j in range(len(types)):
            q='MATCH (c:'+types[i]+')-[r]->(m:'+types[j]+') return c,m' # Quering for all Relationships in the graph
            results=db.query(q)
            for record in results:
                node1,node2=record
                graph.add_edge(node1['data']['id'],node2['data']['id'])

    print('Number of edges in the networkx graph = ',graph.number_of_edges())
    print('Number of nodes in the networkx graph = ',graph.number_of_nodes())
#    nx.draw(graph,with_labels=True)
#    plt.draw()
#    plt.show()


if __name__ == "__main__":
    print(ENV["DB_URL"], ENV["DB_USERNAME"], ENV["DB_PASSWORD"])
    export_neo4j()