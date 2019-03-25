from flask import request, Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})
