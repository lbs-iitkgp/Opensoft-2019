from flask import request, Flask, jsonify
from flask_cors import CORS, cross_origin
from backend.graph_io import json_to_lkg

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/": {"origins": "http://localhost:3000"}})
lkg = json_to_lkg("LKG.json")
