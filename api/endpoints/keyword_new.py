from endpoints import *


@app.route('/keyword/<keyword_id>', methods=['GET'])
def keyword_metadata(keyword_id):
    catch_word = mgdb_handler.read_all(keyword_collection, serial=keyword_id)[0]
    number_of_cases = len(get_metas_from_node(keyword_id, "keyword", "case"))
    catch_word["number_of_cases"] = number_of_cases

    return jsonify(catch_word)


@app.route('/keyword/<keyword_id>/plot_line', methods=['GET'])
def keyword_line_distribution(keyword_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    # nx_graph = export_neo4j()
    result = []
    for i in range(1947, 2020):
        result[i] = 0
    subgraph = lkg.query(judges=[], subjects=[], keywords=[keyword_id], judgements=[], types=[], year_range=[])

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
    result = []

    case_ids = get_metas_from_node(keyword_id, "keyword", "case")
    for id in case_ids:
        case = get_metas_from_node(keyword_id, "keyword", "case")
        result.append(case)

    return jsonify(result)
