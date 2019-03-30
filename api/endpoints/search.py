from endpoints import *
from nlp.topic import subject_extraction
from elasticsearch_utils.getters import *

@app.route('/search/cards', methods=['GET', 'POST']) 
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
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
            'acts': acts
        }
        return jsonify(cards)
    elif request.method == 'GET':
        query = request.args.get('query','')
        if query == '':
            return jsonify({})
        year = subject_extraction.search_years(query)
        subjects = subject_extraction.get_subject_matches(query)
        judge = get_doc_with_maxscore(query, 'judge')
        act = get_doc_with_maxscore(query, 'act')
        case = get_doc_with_maxscore(query, 'case')


        print(year)
        print(subjects)
        cards = []
        for j in judge:
            try:
                card = mgdb_handler.read_all(judges_collection, serial=j["serial"])[0]
                if card["percentile"] != 0.0:
                    card["result_type"] = "judge"
                    cards.append(card)
            except IndexError:
                pass

        for s in subjects:
            try:
                card = mgdb_handler.read_all(keyword_collection, name=s[0])[0]
                card["result_type"] = "keyword"
                if card["percentile"] != 0.0:
                    card["result_type"] = "keyword"
                    cards.append(card)
            except IndexError:
                pass

        for a in act:
            try:
                card = mgdb_handler.read_all(acts_collection, serial=a["serial"])[0]
                card["result_type"] = "act"
                cards.append(card)
            except IndexError:
                pass

        for y in year:
            try:
                card = mgdb_handler.read_all(years_collection, name=str(y))[0]
                card["result_type"] = "year"
                cards.append(card)
            except IndexError:
                pass

        for c in case:
            try:
                card = mgdb_handler.read_all(cases_collection, serial=c["serial"])[0]
                card["result_type"] = "case"
                cards.append(card)
            except IndexError:
                pass
        # cards = {
        #     'judges': judge,
        #     'year_range' : year_range,
        #     'subjects' : subjects,
        #     'acts' : act
        # }
        return jsonify(cards)
        # case = get_doc_with_maxscore(query, 'case')
        



@app.route('/search/advanced', methods=['GET', 'POST']) 
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def advanced_search():
    # Get query
    query = request.args.get('query','')

    # Get active cards
    subjects = set(request.form.get('subjects',''))
    years = set(request.form.get('years',''))
    judges = set(request.form.get('judges',''))
    acts = set(request.form.get('acts',''))

    # Fetch cards for given query

    if query:
        fetched_years = subject_extraction.search_years(query)
        fetched_subjects = subject_extraction.get_subject_matches(query)
        fetched_judges = get_doc_with_maxscore(query, 'judge')
        fetched_acts = get_doc_with_maxscore(query, 'act')

        if fetched_judges is "":
            fetched_judges = []
        else:
            fetched_judges = [ j['name'] for j in fetched_judges ]  

        if fetched_acts is "":
            fetched_acts = []
        else:
            fetched_acts = [ a['name'] for a in fetched_acts]

    else:
        fetched_years = set()
        fetched_subjects = set()
        fetched_judges = set()
        fetched_acts = set()
        fetched_cases = set()

    # Merge fetched cards and active cards
    merged_subjects = subjects.union(set(fetched_subjects))
    merged_judges = judges.union(set(fetched_judges))
    merged_acts = acts.union(set(fetched_acts))
    merged_year = years.union(set(fetched_years))

    # Return data
    params = {
        'judges':merged_judges,
        'years' : merged_years,
        'subjects' : merged_subjects,
        'acts': merged_acts
    }
    subgraph = LKG.query(params=params)
    cases = list(subgraph.fetch_cases())
    return jsonify(cases)


@app.route('/search/basic/stage_1', methods=['GET', 'POST'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
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
        # judge = [judge['name']]
        judge = [ j['name'] for j in judge ]  

    if act is "":
        act = []
    else:
        act = [ a['name'] for a in act ]

    if case is "":
        case = []
    else:
        case = [ c['name'] for c in case]

    if query == '':
        return('No query sent')
    else:
        new_judge = []
        for j in judge:
            mongo_j = mgdb_handler.read_all(judges_collection, name=j)
            print(mongo_j)
            if mongo_j:
                new_judge.append("judge_"+str(mongo_j[0]["serial"]))

        new_act = []
        for a in act:
            mongo_a = mgdb_handler.read_all(acts_collection, name=a)
            print(mongo_a)
            if mongo_a:
                new_act.append("act_"+str(mongo_a[0]['serial']))

        new_subjects = []
        for k in subjects:
            mongo_k = mgdb_handler.read_all(keyword_collection, name=k[0])
            print(mongo_k)
            if mongo_k:
                new_subjects.append("keyword_"+str(mongo_k[0]["serial"]))

        params = {
            'judges': set(new_judge),
            'years' : set(year_range),
            'keywords' : set(new_subjects),
            'acts' : set(new_act)
        }

        print(params)
        subgraph = LKG.query(**params)
        cases = [c.split("_")[1] for c in subgraph.fetch_cases()]
        print(cases, len(cases))
        ranked_cases = rank_cases_by_pagination(cases)
        return jsonify(ranked_cases)
        

@app.route('/search/basic/stage_2', methods=['GET', 'POST', 'OPTIONS'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def basic_search_to_get_results_from_cards():
    # [
    #   {
    #       "case_id": 4,
    #       "case_name": "X vs Y",
    #       ...
    #   },
    #   ...
    # ]

    judges = []
    years = []
    keywords = []
    acts = []

    print(request.form['active_cards'])
    print(request.args.get('active_cards', [])
    active_cards = request.args.get('active_cards', [])

    for active_card in active_cards:
        node_type, node_id = active_card.split("_")

        if node_type == "judge":
            judges.append(active_card)
        elif node_type == "act":
            acts.append(active_card)
        elif node_type == "keyword":
            keywords.append(active_card)
        elif node_type == "year":
            years.append(int(node_id)+1952)

    params = {
        'judges': set(judges),
        'years' : set(years),
        'keywords' : set(keywords),
        'acts' : set(acts)
    }

    subgraph = LKG.query(**params)
    cases = [c.split("_")[1] for c in subgraph.fetch_cases()]
    print(cases, len(cases))
    ranked_cases = rank_cases_by_pagination(cases)
    return jsonify(ranked_cases)
