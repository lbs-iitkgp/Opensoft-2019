import requests as req
import json
from env import ENV

p = lambda x: print(json.dumps(x, indent=4, sort_keys=False))

# with open('name.json','r') as f:
# 	judges = json.load(f)

ES_URL = ENV["ELASTICSEARCH_URL"]

headers = {
		'Content-Type': 'application/json'
	}

def create_indices():
	## create for judge
	mapping = {
	    "settings" : {
	        "number_of_shards" : 1
	    },
	    "mappings" : {
	        "_doc" : {
	            "properties" : {
	                "name" : { "type" : "text" },
	                "serial" : { "type" : "integer" }
	            }
	        }
	    }
	}
	p(req.put(ES_URL + 'judge', json=mapping, headers=headers).json())
	p(req.put(ES_URL + 'case', json=mapping, headers=headers).json())
	p(req.put(ES_URL + 'act', json=mapping, headers=headers).json())
	print("Succesfully done")

def populate_ES(index,list_data):
	for item in list_data:
		index_url = ES_URL + index + "/_doc/" + str(item['serial'])
		p(req.put(index_url, json=data, headers=headers).json())


def put_data(data, index):
	index_url = ES_URL + index + "/_doc/" + str(index)
	return req.put(index_url, json=data, headers=headers).json()


if __name__ == "__main__":
	for index, judge in enumerate(judges):
		temp = {
			"serial" : None,
			"judge_name" : None
		}
		temp['serial'] = int(index)
		temp['judge_name'] = judge
		try:
			p(put_data(temp, index))
		except Exception as e:
			print(e)
			print(judge, index)

