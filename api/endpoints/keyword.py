from endpoints import *
#from base_class.subgraph import fetch_subgraph_with_keywords
#from base_class.neo4j_to_networkx_graph import export_neo4j

@app.route('/keyword/<keyword_id>', methods=['GET'])
@cross_origin(origin='localhost',headers=["Content- Type","Authorization"])
def keyword_metadata(keyword_id):
<<<<<<< HEAD
    # keyword = mydb.mytable.find({"keyword_id":keyword_id})  
    keyword ={'name': "Hot Damn",'number_of_cases':10}    
    result = {
      "name": keyword['name'],
      "number_of_cases": keyword['number_of_cases'],
      "percentile": 90 
    #   mydb.mytable.find({"keyword_id":keyword_id}).count()*100.0/mydb.mytable.count() 
    }
    return jsonify(result)
=======
    key_word = mgdb_handler.read_all(keyword_collection, serial=keyword_id)[0]
    number_of_cases = len(get_metas_from_node(keyword_id, "keyword", "case"))
    key_word["number_of_cases"] = number_of_cases

    return jsonify(key_word)

>>>>>>> upstream/master

@app.route('/keyword/<keyword_id>/plot_line', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def keyword_line_distribution(keyword_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    # nx_graph = export_neo4j()
    result=[]
    for i in range (1947,2020):
        result[i] = 0
    subgraph = lkg.query(judges =[],subjects=[], keywords=[keyword_id] , judgements = [], types =[], year_range=[],acts =[])
    
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
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def keyword_cases(keyword_id):
    result = []

    case_ids = get_metas_from_node(keyword_id, "keyword", "case")
    for id in case_ids:
        case = get_metas_from_node(keyword_id, "keyword", "case")
        result.append(case)

    return jsonify(result)
