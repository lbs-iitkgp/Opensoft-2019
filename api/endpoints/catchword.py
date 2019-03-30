from endpoints import *


@app.route('/catchword/<catchword_id>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def catchword_metadata(catchword_id):
    # Just return catchword name, # of cases and precentile among catchwords maybe?
    catch_word = mgdb_handler.read_all(catch_collection, serial=int(catchword_id))[0]
    return jsonify(catch_word)


@app.route('/catchword/<catchword_id>/plot_line', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def catchword_line_distribution(catchword_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    # nx_graph = export_neo4j()
    result={}

    # catchword = fetch_from_mongo(catchword_id)

    for i in range(1947,2020):
        result[i] = 0
    
    data = LKG.nodes(data=True)
    such_cases = LKG["catch_"+ str(catchword_id)]
    for case in such_cases:
        all_metas = LKG.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year.split("_")[1])+1947] += 1

    return jsonify(result)


@app.route('/catchword/<catchword_id>/cases', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def catchword_cases(catchword_id):
    case_ids = get_metas_from_node(catchword_id, "catch", "case")
    cases = rank_cases_by_pagination(case_ids)
    return jsonify(cases)
