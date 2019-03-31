from endpoints import *


@app.route('/year/<year>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def year_metadata(year):
    year = mgdb_handler.read_all(keyword_collection, name=year)[0]
    number_of_cases = len(get_metas_from_node(year["serial"], "year", "case"))
    year["number_of_cases"] = number_of_cases

    return jsonify(year)


@app.route('/year/<year>/cases', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def year_cases(year):
    result = []
    year = mgdb_handler.read_all(keyword_collection, name=year)[0]
    case_ids = get_metas_from_node(year["serial"], "year", "case")
    for id in case_ids:
        case = get_metas_from_node(year["serial"], "year", "case")
        result.append(case)

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
