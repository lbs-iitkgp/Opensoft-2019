from endpoints import app, cors

@app.route('/keyword/<keyword_id>', methods=['GET'])
def keyword_metadata(keyword_id):
    # Just return keyword name, # of cases and precentile among keywords maybe?
    #
    # {
    #   "name": ,
    #   "number_of_cases": ,
    #   "percentile": 
    # }
    return('Hello')

@app.route('/keyword/<keyword_id>/plot_line', methods=['GET'])
def keyword_line_distribution(keyword_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    return('Hello')

@app.route('/keyword/<keyword_id>/cases', methods=['GET'])
def keyword_cases(keyword_id):
    # Fetch list of cases that cite this keyword from neo4j and return their details from mongodb as json
    return('Hello')
