from endpoints import app, cors

@app.route('/case/<case_id>', methods=['GET'])
def case_metadata(case_id):
    case = mydb.mytable.find({"case_id":case_id}) 
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
def case_line_distribution(case_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    


@app.route('/case/<case_id>/timeline', methods=['GET'])
def case_timeline(case_id):
    # Timeline function w/ sections parser
    #
    # [
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