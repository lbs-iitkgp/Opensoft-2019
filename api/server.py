from endpoints import *

# from flask import request, Flask, jsonify
# from flask_cors import CORS, cross_origin

# app = Flask(__name__)
# app.config['CORS_HEADERS'] = 'Content-Type'

# cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})

from endpoints.case import *
from endpoints.dummy import *

# @app.route('/hello', methods=['GET'])
# def hello():
#     return('Hello')

# @app.route('/keyword', methods=['GET'])       
# @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
# def keyword():        # endpoint for case subjects
#     query = request.args
#     key = int(request.args.get('page_no', 1))
#     keywords_list = query.values()
#     keywords = set(keywords_list)
#     keywords.remove(key)
#     sub = fetch_subgraph_with_keywords(graph, keyword)
#     cases = list(sub.nodes)
#     result = cases[(10*key):(min(10*key+10, len(cases)))]
#     return jsonify(result)

# @app.route('/years', methods=['GET'])
# @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
# def year():
#     from_year = int(request.args.get('from_year', '2100'))# to be input as string
#     to_year = int(request.args.get('to_year', '2018'))
#     particular_year = request.args.get('particular_year', '2100')
#     years = set()
#     for i in range(from_year, to_year+1):
#         years.add(i)
#     subgraph = fetch_subgraph_with_year_range(graph, years)
#     cases = subgraph.getnodes()
#     return jsonify(cases)
   
# @app.route('/judges', methods=['GET'])
# @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
# def judge():
#     query = request.args
#     key = int(request.args.get('page_no', 1))
#     judges_list = query.values()
#     judges = set(judges_list)
#     judges.remove(key)
#     sub = fetch_subgraph_with_judges(graph, judges)
#     cases = list(sub.nodes)
#     result = cases[(10*key):(min(10*key+10, len(cases)))]
#     return jsonify(result)

# @app.route('/judgement', methods=['GET'])
# @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
# def judgements():
#     query = request.args
#     key = int(request.args.get('page_no', 1))
#     judgements_list = query.values()
#     judgements = set(judgements_list)
#     judgements.remove(key)
#     sub = fetch_subgraph_with_judgements(graph, judgements)
#     cases = list(sub.nodes)
#     result = cases[(10*key):(min(10*key+10, len(cases)))]
#     return jsonify(result)

# @app.route('/subject', methods=['GET'])
# @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
# def subject():     
#     query = request.args
#     key = request.args.get('page_no', 1)
#     subjects_list = query.values()
#     subjects = set(subjects_list)
#     subjects.remove(key)
#     sub = fetch_subgraph_with_subjects(graph, subjects)
#     cases = list(sub.nodes)
#     result = cases[(10*key):(min(10*key+10, len(cases)))]
#     return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    