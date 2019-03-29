from endpoints import *


@app.route('/case/<case_id>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def case_metadata(case_id):
    case = mgdb_handler.read_all(cases_collection, serial=str(case_id))[0]
    judge_ids = get_metas_to_node(case_id, "case", "judge")
    judges = []
    for id in judge_ids:
        judges.append(mgdb_handler.read_all(judges_collection, serial=int(id))[0])

    case["judges"] = judges
    case["year"] = mgdb_handler.read_all(years_collection, name=case["file_name"].split("_")[0])[0]
    return jsonify(case)


@app.route('/case/<case_id>/plot_line', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def case_line_distribution(case_id):
    result = {}
    for i in range (1947 ,2020):
        result[i] = 0
    subgraph = LKG
    data = LKG.nodes(data=True)
    such_cases = subgraph.in_edges(["case_" + str(case_id)])
    for case in such_cases:
        all_metas = LKG.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year.split("_")[1])+1946] += 1
    return jsonify(result)


@app.route('/case/<case_id>/timeline', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def case_timeline(case_id):
    case_file = mgdb_handler.read_all(cases_collection, serial=str(case_id))[0]["file_name"]

    result = [[item[0]: item[1]] for item in get_timelines(case_file, nlp)]

    return jsonify(result)


@app.route('/case/<case_id>/citations', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def case_citations(case_id):
    # Get citer id's from neo4j, and respective names from mongo

    result = {
        "cited_acts": [],
        "cited_cases": [],
        "cited_by_cases": []
    }

    act_ids = get_metas_to_node(case_id, "case", "act")
    for id in act_ids:
        act = mgdb_handler.read_all(acts_collection, serial=int(id))[0]
        result["cited_acts"].append({act["serial"]: act["name"]})

    cited_case_ids = get_metas_to_node(case_id, "case", "case")
    for id in cited_case_ids:
        cited_case = mgdb_handler.read_all(cases_collection, serial=str(id))[0]
        result["cited_cases"].append({cited_case["serial"]: cited_case["name"]})

    cited_by_cases = get_metas_from_node(case_id, "case", "case")
    for id in cited_by_cases:
        cited_by_case = mgdb_handler.read_all(cases_collection, serial=str(id))[0]
        result["cited_by_cases"].append({cited_by_case["serial"]: cited_by_case["name"]})

    return jsonify(result)
