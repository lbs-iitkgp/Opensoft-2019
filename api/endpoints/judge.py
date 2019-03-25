from endpoints import app, cors

@app.route('/judge/<judge_id>', methods=['GET'])
def judge_metadata(judge_id):
    # Just return judge name, # of cases, and percentile among judges maybe?
    #
    # {
    #   "name": ,
    #   "number_of_cases": ,
    #   "percentile": 
    # }
    return('Hello')

@app.route('/judge/<judge_id>/plot_line', methods=['GET'])
def judge_line_distribution(judge_id):
    # Iterate through each case of judge in neo4j
    #   Find case's year from mongo
    return('Hello')

@app.route('/judge/<judge_id>/plot_radar', methods=['GET'])
def judge_radar_distribution(judge_id):
    # Fetch cases that relate to this judge from neo4j, and have a distribution of keywords
    return('Hello')

@app.route('/judge/<judge_id>/cases', methods=['GET'])
def judge_cases(judge_id):
    # Fetch list of cases that relate to this judge from neo4j,
    # and return their details from mongodb as json
    return('Hello')
