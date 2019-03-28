from endpoints import *

@app.route('/judge/<judge_id>', methods=['GET'])
def judge_metadata(judge_id):
    judge = mongo_db.find({"judge_id":judge_id})    
    # judge ={'name': "Divyang",'number_of_cases':10}    
    result =  {
      "name": judge['name'],
      "number_of_cases": judge['number_of_cases'],
       "percentile": mongo_db.find("judge_id",judge_id).count()*100.0/mongo_db.count()
    #    90
    }
    return jsonify(result)

@app.route('/judge/<judge_id>/plot_line', methods=['GET'])
def judge_line_distribution(judge_id):
    # Iterate through each case of judge in neo4j
    #   Find case's year from mongo
    # nx_graph = export_neo4j()
    result = []
    for i in range (1947, 2020):
        result[i] = 0
    subgraph = lkg.query(judges =[judge_id],subjects=[], keywords=[] , judgements = [], types =[], year_range=[])
    
    data = lkg.nodes(data=True)
    such_cases = subgraph[judge_id]
    for case in such_cases:
        all_metas = lkg.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year)] += 1
    return jsonify(result)

@app.route('/judge/<judge_id>/cases', methods=['GET'])
def judge_cases(judge_id):
#     # Fetch list of cases that relate to this judge from neo4j,
#     # and return their details from mongodb as json
#     nx_graph = export_neo4j()
    result = []
    for i in range (1947,2020):
        result[i] = 0
    subgraph = lkg.query(judges =[judge_id], subjects=[], keywords=[], judgements = [], types =[], year_range=[])
    
    for node in subgraph['nodes']:
        case = mongo_db.find("case_id", node['case_id'])
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
     