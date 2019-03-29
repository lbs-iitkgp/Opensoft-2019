from endpoints import *
from nlp.topic import subject_extraction
from elasticsearch_utils.getters import *

@app.route('/search/cards', methods=['GET', 'POST']) 
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def fetch_cards():
    if request.method == 'POST':
        subjects = set(request.form['subjects'])
        # keywords = set(request.form['keywords'])
        years = set(request.form['years'])
        judges = set(request.form['judges'])
        # judgements = set(request.form['judgements'])
        # types = set(request.form['types'])
        acts = set(request.form['acts'])
        cards = {
            'judges': judges,
            # 'judgements' : judgements,
            'year_range' : years,
            # 'keywords' : keywords,
            # 'types' : types,
            'subjects' : subjects,
            'acts' :acts
        }
        return jsonify(cards)
    else if request.method == 'GET':
        query = request.args.get('query','')
        if query == '':
            return jsonify({})
        year_range = subject_extraction.search_years(query)
        subjects = subject_extraction.get_subject_matches(query)
        judge = get_doc_with_maxscore(query, 'judge')
        act = get_doc_with_maxscore(query, 'act')
        cards = {
            'judges': judge,
            'year_range' : year_range,
            'subjects' : subjects,
            'acts' : act
        }
        return jsonify(cards)
        # case = get_doc_with_maxscore(query, 'case')
        



@app.route('/search/advanced', methods=['GET', 'POST']) 
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def advanced_search():      
    subjects = set(request.form.get('subjects',''))
    # keywords = set(request.form.get('keywords','')
    years = set(request.form.get('years',''))
    judges = set(request.form.get('judges',''))
    # judgements = set(request.form['judgements'])
    types = set(request.form.get('types',''))
    acts = set(request.form.get('acts',''))
    params = {
        'judges': judges,
        # 'judgements' : judgements,
        'years' : years,
        # 'keywords' : keywords,
        # 'types' : types,
        'subjects' : subjects,
        'acts' :acts
    }
    subgraph = LKG.query(params=params)
    cases = list(subgraph.fetch_cases())
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
    query = request.args.get('query','')

    year_range = subject_extraction.search_years(query)
    subjects = subject_extraction.get_subject_matches(query)
    judge = get_doc_with_maxscore(query, 'judge')
    act = get_doc_with_maxscore(query, 'act')
    case = get_doc_with_maxscore(query, 'case')

    if judge is "":
        judge = []
    else:
        judge = [judge['name']]

    if act is "":
        act = []
    else:
        act = [act['name']]

    if case is "":
        case = []
    else:
        case = [case['name']]

    if query == '':
        return('No query sent')
    else:
        judge = ["judge_"+str(mgdb_handler.read_all(judges_collection, name=j)[0]["serial"]) for j in judge]
        act = ["act_"+str(mgdb_handler.read_all(acts_collection, name=a)[0]["serial"]) for a in act]
        keywords = ["keyword_"+str(mgdb_handler.read_all(keyword_collection, name=k[0])[0]["serial"]) for k in subjects]
        params = {
            'judges': set(judge),
            'years' : set(year_range),
            'keywords' : set(keywords),
            'acts' : set(act)
        }

        subgraph = LKG.query(**params)
        cases = rank_cases_by_pagination(subgraph)
        return jsonify(cases)
        

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
