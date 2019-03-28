from endpoints import *


@app.route('/keyword/<keyword_id>', methods=['GET'])
def keyword_metadata(keyword_id):
    keyword = mongo_db.find("keyword_id", keyword_id)  
    # keyword ={'name': "Hot Damn",'number_of_cases':10}    
    result = {
      "name": keyword['name'],
      "number_of_cases": keyword['number_of_cases'],
      "percentile": mongo_db.find({"keyword_id":keyword_id}).count()*100.0/mongo_db.count() 
    }
    return jsonify(result)

@app.route('/keyword/<keyword_id>/plot_line', methods=['GET'])
def keyword_line_distribution(keyword_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    # nx_graph = export_neo4j()
    result=[]
    for i in range (1947,2020):
        result[i] = 0
    subgraph = lkg.query(judges =[],subjects=[], keywords=[keyword_id] , judgements = [], types =[], year_range=[])
    
    data = lkg.nodes(data=True)
    such_cases = subgraph[keyword_id]
    for case in such_cases:
        all_metas = lkg.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year)] += 1
    return jsonify(result)

@app.route('/keyword/<keyword_id>/cases', methods=['GET'])
def keyword_cases(keyword_id):
#     # Fetch list of cases that cite this keyword from neo4j and return their details from mongodb as json
#     nx_graph = export_neo4j()
    result = []
    for i in range (1947,2020):
        result[i] = 0
    subgraph = lkg.query(judges =[], subjects=[], keywords=[keyword_id], judgements = [], types =[], year_range=[])
    
    for node in subgraph['nodes']:
        case = mongo_db.find("case_id",node['case_id'])
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
