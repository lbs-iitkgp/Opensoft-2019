from endpoints import *


@app.route('/judge/<judge_id>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def judge_metadata(judge_id):
    judge = mgdb_handler.read_all(judges_collection, serial=judge_id)[0]

    cases_count = len(get_metas_from_node(judge_id, "judge", "case"))
    judge["number_of_cases"] = cases_count

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
    subgraph = lkg.query(judges =[judge_id],subjects=[], keywords=[] , judgements = [], types =[], year_range=[],acts = [])
    
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
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def judge_cases(judge_id):
    result = []

    case_ids = get_metas_from_node(judge_id, "judge", "case")
    for id in case_ids:
        case = get_metas_from_node(judge_id, "judge", "case")
        result.append(case)

    return jsonify(result)
