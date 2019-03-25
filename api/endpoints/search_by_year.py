from ..endpoints import *
from ..base_class.subgraph import fetch_subgraph_with_year_range

@app.route('/years', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def year():
    from_year = int(request.args.get('from_year', '2100'))
    to_year = int(request.args.get('to_year', '2018'))
    particular_year = request.args.get('particular_year', '2100')
    years = set()
    for i in range(from_year, to_year+1):
        years.add(i)
    subgraph = fetch_subgraph_with_year_range(graph, years)
    cases = subgraph.getnodes()
    return jsonify(cases)