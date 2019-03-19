from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

db = GraphDatabase("http://localhost:7474", username="neo4j", password="12345")
q = 'MATCH (u:judge)-[r]->(m:case) RETURN u, r , m'

results = db.query(q, returns=(client.Node, str, client.Node))

for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["id"], r[1], r[2]["id"]))


