from endpoints import *

# Requires Graph
@app.route('/case/<case_id>', methods=['GET'])
def case_metadata(case_id):
    case = mgdb_handler.read_all(cases_collection, case_id)
    judge_ids = get_metas_of_node(case_id, "judge")
    judges = []
    for id in judge_ids:
        judges.append(mgdb_handler.read_all(judges_collection, serial=id)[0]["judge_name"])

    case["judges"] = judges

    return jsonify(case)


@app.route('/case/<case_id>/plot_line', methods=['GET'])
def case_line_distribution(case_id):
    result = {}
    for i in range (1947, 2020):
        result[i] = 0
    subgraph = lkg.query(judges =[],subjects=[], keywords=[] , judgements = [], types =['case'], year_range=[])
    data = lkg.nodes(data=True)
    such_cases = subgraph.in_edges(case_id)
    for case in such_cases:
        for meta, _ in lkg.in_edges(case):
            if data[meta]['type'] == 'year':
                year = meta
        result[int(year)] += 1
    return jsonify(result)



@app.route('/case/<case_id>/timeline', methods=['GET'])
def case_timeline(case_id):
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
    return('Hello')


#TODO: From graph
@app.route('/case/<case_id>/citations', methods=['GET'])
def case_citations(case_id):
    # Get citer id's from neo4j, and respective names from mongo
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
    return('Hello')