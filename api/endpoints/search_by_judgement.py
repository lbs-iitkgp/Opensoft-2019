from ..endpoints import *
from ..base_class.subgraph import fetch_subgraph_with_judgements

@app.route('/judgement', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def judgements():
    query = request.form['judgements']
    key = int(request.form.get('page_no', '1'))
    judgements = set(query)
    sub = fetch_subgraph_with_judgements(graph, judgements)
    cases = list(sub.nodes)
    result = cases[(10*key):(min(10*key+10, len(cases)))]
    return jsonify(result)