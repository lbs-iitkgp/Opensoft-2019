from ..endpoints import *
from ..base_class.subgraph import fetch_subgraph_with_keywords

@app.route('/keywords', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def subject():     
    query = request.form['keywords']
    key = request.form.get('page_no', '1')
    keywords = set(query)
    sub = fetch_subgraph_with_keywords(graph, keywords)
    cases = list(sub.nodes)
    result = cases[(10*key):(min(10*key+10, len(cases)))]
    return jsonify(result)