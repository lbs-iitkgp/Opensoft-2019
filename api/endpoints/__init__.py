from flask import request, Flask, jsonify
from flask_cors import CORS, cross_origin
from backend.graph_io import json_to_lkg
from sections_in_act import get_sections_in_act, get_text_in_section
from nlp.timeline import get_timelines
from backend.graph_io import *

import mongodb_handler as mgdb_handler
import spacy

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/": {"origins": "http://localhost:3000"}})
# lkg = json_to_lkg("LKG.json")
#LKG = neo4j_to_lkg()
#import pickle as pk
#with open("lp.pkl")
LKG = json_to_lkg("lkg_old.json")
#lkg_to_json(LKG, "neo4j_lkg.json")

acts_collection = "act_db"
recent_acts_collection = "recent_act_db"
cases_collection = "case_db"
abbreviations_collection = "abbreviation_db"
judges_collection = "judge_db"
catch_collection = "catch_db"
keyword_collection = "keyword_db"
years_collection = "year_db"

nlp = spacy.load('en')

from endpoints.common import *
