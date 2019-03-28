
from endpoints import *
from base_class.neo4j_to_networkx_graph import export_neo4j
from base_class.subgraph import fetch_subgraph_with_judges

@app.route('/judge/<judge_id>', methods=['GET'])
def judge_metadata(judge_id):
    # Just return judge name, # of cases, and percentile among judges maybe?
    judge = mydb.mytable.find({"judge_id":judge_id})        
    result =  {
      "name": judge['name'],
      "number_of_cases": judge['number_of_cases'],
      "percentile": mydb.mytable.find({"judge_id":judge_id}).count()*100.0/mydb.mytable.count()
    }
    return jsonify(result)

@app.route('/judge/<judge_id>/plot_line', methods=['GET'])
def judge_line_distribution(judge_id):
    # Iterate through each case of judge in neo4j
    #   Find case's year from mongo
    nx_graph = export_neo4j()
    result=[]
    for i in range (1947,2020):
        result.append({i: 0})
    subgraph = fetch_subgraph_with_judges(nx_graph , set(judge_id))
    for node in subgraph['nodes']:
        case = mydb.mytable.find({"case_id":node['case_id']})
        result[int(case['year'])] = result[int(case['year'])]+1
    return jsonify(result)

@app.route('/judge/<judge_id>/cases', methods=['GET'])
def judge_cases(judge_id):
    # Fetch list of cases that relate to this judge from neo4j,
    # and return their details from mongodb as json
    nx_graph = export_neo4j()
    result = []
    subgraph = fetch_subgraph_with_judges(nx_graph , set(judge_id))
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
