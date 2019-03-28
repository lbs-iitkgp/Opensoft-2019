from endpoints import *


@app.route('/act/<act_id>', methods=['GET'])
def act_metadata(act_id):
    # get the act
    act = mgdb_handler.read_all(acts_collection, serial=act_id)[0]

    # get its recent version
    new_act_id = mgdb_handler.read_all(recent_acts_collection, Old_id=act_id)[0]["New_id"]
    new_act_name = mgdb_handler.read_all(acts_collection, serial=new_act_id)[0]["name"]
    act["recent_version"] = {"id": new_act_id, "name": new_act_name}

    # get its abbreviations
    abbr = mgdb_handler.read_all(abbreviations_collection, actual=act["name"])[0]["abbrev"]
    act["abbreviation"] = abbr

    return jsonify(act)


@app.route('/act/<act_id>/sections', methods=['GET'])
def act_sections(act_id):
    act_file_path = mgdb_handler.read_all(acts_collection, serial=act_id)[0]["file"]
    result = get_sections_in_act(act_file_path)

    return jsonify(result)


@app.route('/act/<act_id>/section/<section_id>', methods=['GET'])
def act_section(act_id, section_id):
    act_file_path = mgdb_handler.read_all(acts_collection, serial=act_id)[0]["file"]
    text = get_text_in_section(act_file_path, section_id)

    result = {
        'section_id': section_id,
        'section_text': text
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


@app.route('/act/<act_id>/cases', methods=['GET'])
def act_citations(act_id):
    # Fetch list of cases that cite this act from neo4j and return their details from mongodb as json
    result = []
    case_ids = get_metas_from_node(act_id, "act", "case")
    for id in case_ids:
        case = mgdb_handler.read_all(cases_collection, serial=id)[0]
        result.append(case)

    return jsonify(result)