from endpoints import app, cors
from base_class.subgraph import fetch_subgraph_with_year_range
from base_class.neo4j_to_networkx_graph import export_neo4j
import os
import json
import re

@app.route('/year/<year>', methods=['GET'])
def year_metadata(year):

    result = []
    for year_node in mydb.mytable.find({"year":year}) :
        part = {
        "year": year,
        "number_of_cases": mydb.mytable.find({"year":year}).count(),
        "percentile": mydb.mytable.find({"year":year}).count()*100.0/mydb.mytable.count() 
        }
        result.append(part)
    return jsonify(result)


@app.route('/year/<year>/cases', methods=['GET'])
def year_cases(year):
    # Fetch list of cases that relate to this year from neo4j,
    # and return their details from mongodb as json
    graph = export_neo4j()
    result = []
    subgraph = fetch_subgraph_with_year_range(graph , set(year))
    for node in subgraph['nodes']:
        case = mydb.mytable.find({"case_id":node['case_id']})
        point = {
            "case_id": case['case_id'],
            "case_name": case['case_name'],
            "case_indlaw_id": case['case_indlawid'],
            "case_judges": case['judge'],
            "case_judgement": case['judgement'],
            "case_date": case['case_date'],
            "case_year": case['case_year']
            }
        result.append(point)
    return jsonify(result)

@app.route('year/<year>/piechart',methods=['GET'])
def year_piechart(year):
    PATH = os.path.join('base_class', 'keyword.json')
    file = open(PATH, 'r')
    keyword_list = json.loads(file.read())
    data_points = {}
    keywords = [keyword_data[0] for keyword_data in keyword_list]
    for keyword_data in keyword_list:
        data_points[keyword_data[0]] = 0
    for case in mydb.mytable.find({"year":year}) :
        data_points[case['keywords']] = data_points[case['keywords']] +1
    for i in range (0,64):
        data_points 
    return jsonify(result)
