
from endpoints import *
from base_class.subgraph import fetch_subgraph_with_subjects

@app.route('/catchword/<catchword_id>', methods=['GET'])
def catchword_metadata(catchword_id):
    # Just return catchword name, # of cases and precentile among catchwords maybe?
    catchword = mydb.mytable.find({"catchword_id":catchword_id})
    result ={
        'name': catchword["name"],
        'number_of_cases': catchword["number_of_cases"],
        'percentile': mydb.mytable.find({"catchword_id":catchword_id}).count()*100.0/mydb.mytable.count()
    }
    return jsonify(result)


@app.route('/catchword/<catchword_id>/plot_line', methods=['GET'])
def catchword_cases(catchword_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    nx_graph = export_neo4j()
    result=[]
    for i in range (1947,2020):
        result.append({i: 0})
    subgraph = fetch_subgraph_with_subjects(nx_graph , set(catchword_id))
    for node in subgraph['nodes']:
        case = mydb.mytable.find({"case_id":node['case_id']})
        result[int(case['year'])] = result[int(case['year'])]+1
    return jsonify(result)

@app.route('/catchword/<catchword_id>/cases', methods=['GET'])
def catchword_cases(catchword_id):
# Fetch list of cases that cite this catchword from neo4j and return their details from mongodb as json
    nx_graph = export_neo4j()
    result = []
    subgraph = fetch_subgraph_with_subjects(nx_graph , set(catchword_id))
    for node in subgraph['nodes']:
        case = mydb.mytable.find({"keyword":node['keyword']})
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

