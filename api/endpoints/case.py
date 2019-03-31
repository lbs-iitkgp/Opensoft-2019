from endpoints import *


@app.route('/case/<case_id>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def case_metadata(case_id):
<<<<<<< HEAD
    #case = mongo_db.find("case_id",case_id)
    # case  = {   'case_name': "hi",
    #             'case_indlawid': 42,
    #             'case_judges': 'some',
    #             'case_judgements': 'win',
    #             'case_date': '23',
    #             'case_year': 1969
    #     }
    result =  {
        "case_id": case_id,
        "case_name": case['case_name'],
        "case_indlaw_id": case['case_indlawid'],
        "case_judges": case['judge'],
        "case_judgement": case['judgement'],
        "case_date": case['case_date'],
        "case_year": case['case_year']
      }
    return jsonify(result)
=======
    case = mgdb_handler.read_all(cases_collection, case_id)
    judge_ids = get_metas_to_node(case_id, "case", "judge")
    judges = []
    for id in judge_ids:
        judges.append(mgdb_handler.read_all(judges_collection, serial=id)[0]["judge_name"])

    case["judges"] = judges

    return jsonify(case)

>>>>>>> upstream/master

@app.route('/case/<case_id>/plot_line', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def case_line_distribution(case_id):
    result = {}
    for i in range (1947 ,2020):
        result[i] = 0
    subgraph = lkg.query(judges =[],subjects=[], keywords=[] , judgements = [], types =[], year_range=[], acts =[]) 
    data = lkg.nodes(data=True)
    such_cases = subgraph[case_id]
    for case in such_cases:
        all_metas = lkg.in_edges(case)
        for meta, _ in all_metas:
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year)] += 1
    return jsonify(result)


@app.route('/case/<case_id>/timeline', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def case_timeline(case_id):
<<<<<<< HEAD
    # Timeline function w/ sections parser
    #  # [
    #   {
    #       date_1: {
    #           "text": ,
    #           "acts": [
    #               {
    #                   "text":
    #                   "line":
    #                   "index":
    #                   "act_id":
    #                   "sections": [
    #                       {
    #                           "section_id": ,
    #                           "rel_index":  
    #                       },
    #                       {
    #                           ...
    #                       }
    #                   ]
    #               },
    #               {
    #                   ...
    #               }
    #           ]
    #       },
    #       ...
    #   }
    # ]
    result = {"12-12-12":"Test 1","12-12-11":"Test 2","12-12-14":"Test 3","12-12-15":"Test 4"}
    return jsonify(result)
=======
    case_file = mgdb_handler.read_all(cases_collection, serial=case_id)[0]["file_name"]

    result = {item[0]: item[1] for item in get_timelines(case_file, nlp)}

    return jsonify(result)

>>>>>>> upstream/master

@app.route('/case/<case_id>/citations', methods=['GET'])
@cross_origin(origin='localhost',headers=["Content- Type","Authorization"])
def case_citations(case_id):
    # Get citer id's from neo4j, and respective names from mongo
<<<<<<< HEAD
    #
    # {
    #   "cited_acts": [
    #       { "act_id": , "act_name": },
    #       ...
    #   ],
    #   cited_cases: [
    #       { "case_id": , "case_name": },
    #       ...
    #   ],
    #   cited_by_cases: [
    #       { "case_id": , "case_name": },
    #       ...
    #   ]
    # }
    result = { "cited_acts": [{'1':"Criminal"},{'2':"Land"}], "cited_cases": [{'1':"Criminal"},{'2':"Land"}], "cited_by_cases": [{'1':"Criminal"},{'2':"Land"}]  }
=======

    result = {
        "cited_acts": [],
        "cited_cases": [],
        "cited_by_cases": []
    }

    act_ids = get_metas_to_node(case_id, "case", "act")
    for id in act_ids:
        act = mgdb_handler.read_all(acts_collection, serial=id)[0]
        result["cited_acts"].append({act["serial"]: act["name"]})

    cited_case_ids = get_metas_to_node(case_id, "case", "case")
    for id in cited_case_ids:
        cited_case = mgdb_handler.read_all(cases_collection, serial=id)[0]
        result["cited_cases"].append({cited_case["serial"]: cited_case["title"]})

    cited_by_cases = get_metas_from_node(case_id, "case", "case")
    for id in cited_by_cases:
        cited_by_case = mgdb_handler.read_all(cases_collection, serial=id)[0]
        result["cited_by_cases"].append({cited_by_case["serial"]: cited_by_case["title"]})

>>>>>>> upstream/master
    return jsonify(result)
