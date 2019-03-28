from endpoints import *


@app.route('/year/<year>', methods=['GET'])
def year_metadata(year):
    year = mgdb_handler.read_all(keyword_collection, name=year)[0]
    number_of_cases = len(get_metas_from_node(year["serial"], "year", "case"))
    year["number_of_cases"] = number_of_cases

    return jsonify(year)


@app.route('/year/<year>/cases', methods=['GET'])
def year_cases(year):
    result = []
    year = mgdb_handler.read_all(keyword_collection, name=year)[0]
    case_ids = get_metas_from_node(year["serial"], "year", "case")
    for id in case_ids:
        case = get_metas_from_node(year["serial"], "year", "case")
        result.append(case)

    return jsonify(result)


@app.route('year/<year>/piechart', methods=['GET'])
def year_piechart(year):
    return jsonify('Hello)
