from endpoints import *


@app.route('/year/<year>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def year_metadata(year):
    year = mgdb_handler.read_all(keyword_collection, name=year)[0]
    return jsonify(year)


@app.route('/year/<year>/cases', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def year_cases(year):
    result = []
    year = mgdb_handler.read_all(keyword_collection, name=year)[0]
    case_ids = get_metas_from_node(year["serial"], "year", "case", split=False)
    for id in case_ids:
        if id.startswith("case_"):
            case = mgdb_handler.read_all(cases_collection, serial=str(id))[0]
            result.append(case)

    return jsonify(result)


@app.route('/year/<year>/piechart',methods=['GET'])
def year_piechart(year):
    result = [] 
   
    data = LKG.nodes(data=True)
    such_cases = LKG[year]
    for case in such_cases:
        all_metas = LKG.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'keyword':
                keyword = meta
        if result.has_key(keyword):
            result[keyword] += 1
        else:
            result[keyword] =1
    return jsonify(result)
