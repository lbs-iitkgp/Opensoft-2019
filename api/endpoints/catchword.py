from endpoints import *


@app.route('/catchword/<catchword_id>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def catchword_metadata(catchword_id):
    # Just return catchword name, # of cases and precentile among catchwords maybe?
<<<<<<< HEAD
    #catchword = mydb.mytable.find({"catchword_id":catchword_id})
    catchword = {"name":"Babajan","number_of_cases":-20}
    result ={
        'name': catchword["name"],
        'number_of_cases': catchword["number_of_cases"],
        'percentile': 90#mydb.mytable.find({"catchword_id":catchword_id}).count()*100.0/mydb.mytable.count()
    }
    return jsonify(result)
=======
    catch_word = mgdb_handler.read_all(catch_collection, serial=catchword_id)[0]
    number_of_cases = len(get_metas_from_node(catchword_id, "catch", "case"))
    catch_word["number_of_cases"] = number_of_cases

    return jsonify(catch_word)
>>>>>>> upstream/master


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
    subgraph = lkg.query(judges=[], subjects=[catchword_id], keywords=[], judgements=[], types=[], year_range=[],acts = [])
    data = lkg.nodes(data=True)
    such_cases = subgraph[catchword_id]
    for case in such_cases:
        all_metas = lkg.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year)] += 1
    return jsonify(result)


@app.route('/catchword/<catchword_id>/cases', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def catchword_cases(catchword_id):
    result = []

    case_ids = get_metas_from_node(catchword_id, "catch", "case")
    for id in case_ids:
        case = get_metas_from_node(catchword_id, "catch", "case")
        result.append(case)

    return jsonify(result)


