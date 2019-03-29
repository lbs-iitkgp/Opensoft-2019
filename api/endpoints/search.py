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
            'judges': list(set(judge)),
            'year_range' : list(set(year_range)),
            'subjects' : list(set(subjects)),
            'acts' : list(set(act))
        }
        return jsonify(cards)
        # case = get_doc_with_maxscore(query, 'case')
        



@app.route('/search/advanced', methods=['GET', 'POST']) 
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def advanced_search():      
    subjects = set(request.form['subjects'])
    keywords = set(request.form['keywords'])
    years = set(request.form['years'])
    judges = set(request.form['judges'])
    # judgements = set(request.form['judgements'])
    types = set(request.form['types'])
    acts = set(request.form['acts'])
    params = {
        'judges': judges,
        # 'judgements' : judgements,
        'year_range' : years,
        'keywords' : keywords,
        # 'types' : types,
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
    query = request.args.get('query','')

    year_range = subject_extraction.search_years(query)
    subjects = subject_extraction.get_subject_matches(query)
    judge = get_doc_with_maxscore(query, 'judge')
    act = get_doc_with_maxscore(query, 'act')
    case = get_doc_with_maxscore(query, 'case')

    if judge is None:
        judge = ''
    else:
        judge = judge['name']

    if act is None:
        act = ''
    else:
        act = act['name']

    if case is None:
        case = ''
    else:
        case = case['name']

    if key == '':
        return('No query sent')
    else:
        params = {
            'judges': set(judge),
            'year_range' : set(year_range),
            'subjects' : set(subjects),
            'acts' : set(act)
        }
        subgraph = lkg.query(params)
        cases = list(subgraph.nodes())
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
