from backend.graph_formation import prepare_graph
from backend.graph_io import lkg_to_json, lkg_to_neo4j, lkg_to_nx

j = prepare_graph()
j.remove_node("")

print(len(j.fetch_cases()))
print(len(j.nodes()))
print(len(j.edges()))

print("Starting to write to json")
lkg_to_json(j, "LKG.json")
print("Finished writing to json")


print("Importing lkg to neo4j")
lkg_to_neo4j(j)
print("Imported lkg to neo4j")
