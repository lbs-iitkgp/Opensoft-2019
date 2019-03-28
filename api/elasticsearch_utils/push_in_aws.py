import json
from elasticsearch import Elasticsearch, RequestsHttpConnection, exceptions
import requests as req

es = Elasticsearch()

settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "_doc": {
            "properties": {
                "name": {
                    "type": "text"
                },
                "number_of_cases":{
                	"type": "integer"
                }
            }
        }
     }
}

p = lambda x: print(json.dumps(x, indent=4, sort_keys=False))

es.indices.create(index='judge', body=settings)
# es.indices.delete(index='judge')

with open('judge.json', 'r') as f:
	judges = json.load(f)


for index, value in enumerate(judges):
	body = {
		"name" : value[0],
		"number_of_cases": value[1]
	}
	p(es.index(index='judge', doc_type="_doc", id=index, body=body))
