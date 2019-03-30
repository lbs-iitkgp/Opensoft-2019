import requests as req 
import json

ES_URL = "http://localhost:9200/"
# ES_URL = "http://88234f03.ngrok.io/"
# 

headers = {
	'Content-Type' : 'application/json'
}

def get_doc_with_maxscore(inp, index):
	# doc_data = req.get(ES_URL + "{}/_search?q=name:{}".format(index, inp.replace(' ', '%20'))).json()
	

	if index == "act":
		data = {
			"query": {
		    "simple_query_string" : {
		        "query": inp,
		        "fields": ["name"],
		        "default_operator": "or",
		        "minimum_should_match" : "3<80%"
		    }
		  }
		}
	else:
		data = {
			"query": {
		    "simple_query_string" : {
		        "query": inp,
		        "fields": ["name"],
		        "default_operator": "or"
		    }
		  }
		}
	doc_data = req.post(ES_URL + "{}/_search".format(index), json=data, headers=headers).json()

	# max_score = doc_data["hits"]['max_score']
	# if max_score is None or max_score is []:
		# return ''
	docs = [(d["_source"],d['_score']) for d in doc_data["hits"]["hits"][:5]]
	return([{"name" : doc[0]["name"], "serial" : doc[0]["serial"], "score" : doc[1]} for doc in docs])


def get_judge_with_maxscore(inp, index):
	judge_data = req.get(ES_URL + "judge/_search?q=judge_name:{}".format(inp.replace(' ', '%20'))).json()
	if max_score is None:
		return None
	max_score = judge_data["hits"]['max_score']
	judge = judge_data["hits"]["hits"][0]["_source"]
	return {
			"judge" : judge["judge_name"], 
			"serial" : judge["serial"],
			"score" : max_score
			}
