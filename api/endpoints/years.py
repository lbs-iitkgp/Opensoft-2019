from endpoints import *


@app.route('/year/<year>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def year_metadata(year):
    year = mgdb_handler.read_all(years_collection, name=str(year))[0]
    return jsonify(year)


@app.route('/year/<year>/cases', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def year_cases(year):
    result = []
    year = mgdb_handler.read_all(years_collection, name=str(year))[0]
    case_ids = get_metas_from_node(year["serial"], "year", "case", split=False)
    for case_id in case_ids:
        case = mgdb_handler.read_all(cases_collection, serial=str(case_id))[0]
        result.append(case)

    return jsonify(result)


@app.route('/year/<year>/piechart',methods=['GET'])
def year_piechart(year):
    result = {} 

    year_id = mgdb_handler.read_all(years_collection, name=str(year))
    if year_id:
        year = "year_"+str(year_id[0]["serial"])
    else:
        return {}
    data = LKG.nodes(data=True)
    such_cases = LKG[year]
    for case in such_cases:
        all_metas = LKG.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'keyword':
                keyword = meta
        if keyword in result:
            result[keyword] += 1
        else:
            result[keyword] =1

    new_result = dict()
    for keyword in result:
        keyword_name = mgdb_handler.read_all(keyword_collection, serial=int(keyword.split("_")[1]))[0]["name"]
        new_result[keyword_name] = result[keyword]
    return jsonify(new_result)
