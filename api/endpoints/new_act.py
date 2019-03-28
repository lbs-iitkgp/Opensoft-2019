from endpoints import *

import mongodb_handler as mgdb_handler

acts_collection = "act_db"
recent_acts_collection = "recent_act_db"
cases_collection = "case_db"
abbreviations_collection = "abbreviation_db"
judges_collection = "judge_db"
catch_collection = "catch_db"
keyword_collection = "keyword_db"


@app.route('/act/<act_id>', methods=['GET'])
def act_metadata(act_id):
    # get the act
    act = mgdb_handler.read_all(acts_collection, serial=act_id)

    # get its recent version
    new_act_id = mgdb_handler.read_all(recent_acts_collection, Old_id=act_id)["New_id"]
    new_act_name = mgdb_handler.read_all(acts_collection, serial=new_act_id)["name"]
    act["recent_version"] = {"id": new_act_id, "name": new_act_name}

    # get its abbreviations
    abbr = mgdb_handler.read_all(abbreviations_collection, actual=act["name"])["abbrev"]
    act["abbreviation"] = abbr
    # # get
    # # act = {
    # #     'name': 'name',
    # #     'year': 2010,
    # #     'type': 'idid',
    # #     'recent_version_id':'2.0',
    # #     'recent_version_name': 'beta',
    # #     'abbreviation': 'jefu'
    # # }
    # result = {
    #     # 'name': act['name'],
    #     # 'year': act['year'],
    #     # 'type': act['type'],
    #     'recent_version': {
    #         'id': act['recent_version_id'],
    #         'name': act['recent_version_name']
    #     },
    #     'abbreviation': act['abbreviation']
    # }
    return jsonify(act)


@app.route('/act/<act_id>/sections', methods=['GET'])
def act_sections(act_id):
    result = []
    for section in mongo_db.find("act_id", act_id):
        section = {
            'section_id': section['section_id'],
            'section_text': section['section_text']
        }
        result.append(section)
    return jsonify(result)


@app.route('/act/<act_id>/section/<section_id>', methods=['GET'])
def act_section(act_id, section_id):
    sections = mongo_db.find("act_id", act_id)
    section = mongo_db.find("section_id", section_id)
    result = {
        'section_id': section_id,
        'section_text': section['section_text']
        # 'section_text': "hiya"
    }
    return jsonify(result)


# TODO: From graph
@app.route('/act/<act_id>/plot_line', methods=['GET'])
def act_line_distribution(act_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    result = {}

    # catchword = fetch_from_mongo(catchword_id)

    for i in range(1947, 2020):
        result[i] = 0
    subgraph = lkg.acts_query(acts=[act_id])
    data = lkg.nodes(data=True)
    such_cases = subgraph[act_id]
    for case in such_cases:
        all_metas = lkg.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year)] += 1
    return jsonify(result)


# TODO: From graph
app.route('/act/<act_id>/cases', methods=['GET'])
def act_citations(act_id):
    # Fetch list of cases that cite this act from neo4j and return their details from mongodb as json
    result = []
    for i in range(1947, 2020):
        result[i] = 0
    subgraph = lkg.acts_query(acts=[act_id])

    data = lkg.nodes(data=True)
    such_cases = subgraph[act_id]
    for case in such_cases:
        all_metas = lkg.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year)] += 1
    return jsonify(result)
