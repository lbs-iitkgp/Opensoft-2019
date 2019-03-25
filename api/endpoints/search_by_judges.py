from ..endpoints import *
from ..base_class.subgraph import fetch_subgraph_with_judges

@app.route('/judges', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def judge():
    query = request.form['judges']
    key = int(request.form.get('page_no',1))
    judges = set(query)
    sub = fetch_subgraph_with_judges(graph, judges)
    cases = list(sub.nodes)
    result = cases[(10*key):(min(10*key+10, len(cases)))]
    return jsonify(query)