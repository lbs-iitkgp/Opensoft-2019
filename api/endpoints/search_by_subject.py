from ..endpoints import *
from ..base_class.subgraph import fetch_subgraph_with_subjects

@app.route('/subject', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def subject():     
    query = request.form['subject']
    key = request.form.get('page_no', '1')
    subjects = set(query)
    sub = fetch_subgraph_with_subjects(graph, subjects)
    cases = list(sub.nodes)
    result = cases[(10*key):(min(10*key+10, len(cases)))]
    return jsonify(result)