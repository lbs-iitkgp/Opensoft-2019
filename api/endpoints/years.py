from endpoints import app, cors

@app.route('/year/<year>', methods=['GET'])
def year_metadata(year):
    # Just return year name, and number of cases?
    #
    # {
    #   "year": ,
    #   "number_of_cases": ,
    #   "percentile": 
    # }
    return('Hello')

@app.route('/year/<year>/plot_radar', methods=['GET'])
def year_radar_distribution(year):
    # Fetch cases that relate to this year from neo4j, and have a distribution of keywords
    # in this year
    return('Hello')

@app.route('/year/<year>/cases', methods=['GET'])
def year_cases(year):
    # Fetch list of cases that relate to this year from neo4j,
    # and return their details from mongodb as json
    return('Hello')
