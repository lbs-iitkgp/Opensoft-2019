from endpoints import app, cors

@app.route('/search/advanced', methods=['GET', 'POST'])
def advanced_search():
    # [
    #   {
    #       "case_id": 4,
    #       "case_name": "X vs Y",
    #       ...
    #   },
    #   ...
    # ]
    return('Hello')

@app.route('/search/basic/stage_1', methods=['GET', 'POST'])
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
