from endpoints import *


@app.route('/year/<year>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
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
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def year_cases(year):
    # Fetch list of cases that relate to this year from neo4j,
    # and return their details from mongodb as json
    # graph = export_neo4j()
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
    result = []
    subgraph = lkg.query(judges = [], subjects=[], keywords=[], judgements = [], types =[], year_range=[year], acts =[])
    
    data = lkg.nodes(data=True)
    such_cases = subgraph[year]
    for case in such_cases:
        all_metas = lkg.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'keyword':
                keyword = meta
        if result.has_key(keyword):
            result[keyword] += 1
        else:
            result[keyword] =1
    return jsonify(result)