from endpoints import *

@app.route('/search/advanced', methods=['GET', 'POST']) 
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def advanced_search():      
    subjects = set(request.form['subjects'])
    keywords = set(request.form['keywords'])
    years = set(request.form['years'])
    judges = set(request.form['judges'])
    judgements = set(request.form['judgements'])
    types = set(request.form['types'])
    acts = set(request.form['acts'])
    params = {
        'judges': judges,
        'judgements' : judgements,
        'year_range' : years,
        'keywords' : keywords,
        'types' : types,
        'subjects' : subjects,
        'acts' :acts
    }
    subgraph = lkg.query(params)
    cases = list(subgraph.nodes())
    return jsonify(cases)


@app.route('/search/basic/stage_1', methods=['GET', 'POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def basic_search_to_propose_topic_cards():
    # [
    #   {
    #       "type": "JUDGE",
    #       "name": "Judge name",
    #       "toggle_state": true
    #   },
    #   ...
    # ]
    #
    return('Hello')

@app.route('/search/basic/stage_2', methods=['GET', 'POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def basic_search_to_get_results_from_cards():
    # [
    #   {
    #       "case_id": 4,
    #       "case_name": "X vs Y",
    #       ...
    #   },
    #   ...
    # ]

    return('Hello')
