from endpoints import *


@app.route('/judge/<judge_id>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def judge_metadata(judge_id):
    judge = mgdb_handler.read_all(judges_collection, serial=int(judge_id))[0]

    return jsonify(judge)


@app.route('/judge/<judge_id>/plot_line', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def judge_line_distribution(judge_id):
    # Iterate through each case of judge in neo4j
    #   Find case's year from mongo
    # nx_graph = export_neo4j()
    result = []
    for i in range (1947, 2020):
        result[i] = 0
    
    data = LKG.nodes(data=True)
    such_cases = LKG["judge_"+judge_id]
    for case in such_cases:
        all_metas = LKG.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year.split("_")[1])+1946] += 1
    return jsonify(result)


@app.route('/judge/<judge_id>/cases', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def judge_cases(judge_id):
    result = []

    case_ids = get_metas_from_node(judge_id, "judge", "case", split=False)
    for id in case_ids:
        case = mgdb_handler.read_all(cases_collection, serial=str(id))[0]
        result.append(case)
    return jsonify(result)
