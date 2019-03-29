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
	
	data = {
			    "query": {
			        "match_phrase" : {
			            "name" : inp
			        }
			    }
			}

	doc_data = req.post(ES_URL + "{}/_search".format(index), json=data, headers=headers).json()

	max_score = doc_data["hits"]['max_score']
	if max_score is None or max_score is []:
		return ''
	doc = doc_data["hits"]["hits"][0]["_source"]
	return {
			"name" : doc["name"], 
			"serial" : doc["serial"],
			"score" : max_score
			}

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