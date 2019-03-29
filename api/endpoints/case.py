from endpoints import *

@app.route('/case/<case_id>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def case_metadata(case_id):
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

@app.route('/case/<case_id>/citations', methods=['GET'])
@cross_origin(origin='localhost',headers=["Content- Type","Authorization"])
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
    result = { "cited_acts": [{'1':"Criminal"},{'2':"Land"}], "cited_cases": [{'1':"Criminal"},{'2':"Land"}], "cited_by_cases": [{'1':"Criminal"},{'2':"Land"}]  }
    return jsonify(result)
