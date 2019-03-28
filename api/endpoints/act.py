from endpoints import *

@app.route('/act/<act_id>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def act_metadata(act_id):
    #act = mydb.mytable.find({"act_id":act_id})
    act = {"name":"Aadi","year":1990,"type":"Criminal","recent_version_name":"190","recent_version_id":"Aadi05","abbreviation":"CRM"}
    result ={
        'name': act['name'],
        'year': act['year'],
        'type': act['type'],
        'recent_version': {
            'id': act['recent_version_id'],
            'name': act['recent_version_name']
        },
        'abbreviation': act['abbreviation'] 
    }
    return jsonify(result)

@app.route('/act/<act_id>/sections', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def act_sections(act_id):
    result = []
    for section in mongo_db.find("act_id",act_id):
        section = {
                'section_id': section['section_id'],
                'section_text': section['section_text']
            }
        result.append(section)
    return jsonify(result)

@app.route('/act/<act_id>/section/<section_id>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def act_section(act_id, section_id):
    sections = mongo_db.find("act_id", act_id)
    section = mongo_db.find("section_id", section_id)
    result = {
        'section_id': section_id,
        'section_text': section['section_text'] 
        # 'section_text': "hiya"
    }
    return jsonify(result)


@app.route('/act/<act_id>/plot_line', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def act_line_distribution(act_id):
    # Iterateacts=[act_id] through each citer in neo4j
    #   Find citer's year from mongo
    #
    # 
    result = { 1934: 19,1936: 7,1940: 42,1943: 5, 1935: 19,1937: 7,1941: 42,1944: 5}
    return jsonify(result)


    # catchword = fetch_from_mongo(catchword_id)

    for i in range(1947,2020):
        result[i] = 0
    subgraph = lkg.query(judges =[],subjects=[], keywords=[] , judgements = [], types =[], year_range=[], acts =[act_id])
    data = lkg.nodes(data=True)
    such_cases = subgraph[act_id]
    for case in such_cases:
        all_metas = lkg.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year)] += 1
    return jsonify(result)

@app.route('/act/<act_id>/cases', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def act_citations(act_id):
    # Fetch list of cases that cite this act from neo4j and return their details from mongodb as json
    result = []
    for i in range (1947,2020):
        result[i] = 0
    subgraph = lkg.query(judges =[],subjects=[], keywords=[] , judgements = [], types =[], year_range=[], acts =[act_id])
    
    data = lkg.nodes(data=True)
    such_cases = subgraph[act_id]
    for case in such_cases:
        all_metas = lkg.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year)] += 1
    return jsonify(result)
