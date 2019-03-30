from endpoints import *


@app.route('/keyword/<keyword_id>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def keyword_metadata(keyword_id):
    key_word = mgdb_handler.read_all(keyword_collection, serial=int(keyword_id))[0]
    number_of_cases = len(get_metas_from_node(keyword_id, "keyword", "case"))

    return jsonify(key_word)


@app.route('/keyword/<keyword_id>/plot_line', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def keyword_line_distribution(keyword_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    # nx_graph = export_neo4j()
    result={}
    for i in range (1947,2020):
        result[i] = 0
    
    data = LKG.nodes(data=True)
    such_cases = LKG["keyword_"+ keyword_id]
    for case in such_cases:
        all_metas = LKG.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year.split("_")[1])+1946] += 1
    return jsonify(result)


@app.route('/keyword/<keyword_id>/cases', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def keyword_cases(keyword_id):
    case_ids = get_metas_from_node(keyword_id, "keyword", "case")
    cases = rank_cases_by_pagination(case_ids)

    return jsonify(cases)
