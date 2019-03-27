from endpoints import *
from base_class.subgraph import fetch_subgraph_with_keywords
from base_class.neo4j_to_networkx_graph import export_neo4j

@app.route('/keyword/<keyword_id>', methods=['GET'])
def keyword_metadata(keyword_id):
    keyword = mydb.mytable.find({"keyword_id":keyword_id})  
    result = {
      "name": keyword['name'],
      "number_of_cases": keyword['number_of_cases'],
      "percentile": mydb.mytable.find({"keyword_id":keyword_id}).count()*100.0/mydb.mytable.count() 
    }
    return('Hello')

@app.route('/keyword/<keyword_id>/plot_line', methods=['GET'])
def keyword_line_distribution(keyword_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    nx_graph = export_neo4j()
    result=[]
    for i in range (1947,2020):
        result.append({i: 0})
    subgraph = fetch_subgraph_with_keywords(nx_graph , set(keyword_id))
    for node in subgraph['nodes']:
        case = mydb.mytable.find({"case_id":node['case_id']})
        result[int(case['year'])] = result[int(case['year'])]+1
    return jsonify(result)

@app.route('/keyword/<keyword_id>/cases', methods=['GET'])
def keyword_cases(keyword_id):
    # Fetch list of cases that cite this keyword from neo4j and return their details from mongodb as json
    nx_graph = export_neo4j()
    result = []
    subgraph = fetch_subgraph_with_keywords(nx_graph , set(keyword_id))
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
