import json
from elasticsearch import Elasticsearch, RequestsHttpConnection, exceptions
import requests as req

class ESHandler:
	def __init__(self, url):
		self.url = url

	def info(self):
		return req.get(self.url).json()

	def create(self, index, mappings=None):
		headers ={
			'Content-Type': 'application/json'
		}
		data = {
			    "settings" : {
			        "number_of_shards" : 1
			    },
			    "mappings" : {
			        "_doc" : {
			            "properties" : {
			            }
			        }
			    }
			}
		return req.put(self.url+'/'+index, json=data, headers=headers).json()

	def delete(self, index):
		headers ={
			'Content-Type': 'application/json'
		}
		return req.delete(self.url+'/'+index, headers=headers).json()

p = lambda x: print(json.dumps(x, indent=4, sort_keys=False))

# ES_HOST = "http://ec2-3-90-3-26.compute-1.amazonaws.com"
# ES_HOST = "http://ec2-3-90-3-26.compute-1.amazonaws.com"

try:
	es = ESHandler(ES_HOST)
	p(es.info())
	# p(es.create('judge'))
	p(es.delete('judge'))
except Exception as e:
	print('Unexpected Error Occurred. Exiting')
	raise e from None

