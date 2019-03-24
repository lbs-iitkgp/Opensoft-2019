from endpoints import app, cors

@app.route('/catchword/<catchword_id>', methods=['GET'])
def catchword_metadata(catchword_id):
    # Just return catchword name, and precentile among catchwords maybe?
    return('Hello')

@app.route('/catchword/<catchword_id>/plot_line', methods=['GET'])
def catchword_line_distribution(catchword_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    return('Hello')

@app.route('/catchword/<catchword_id>/cases', methods=['GET'])
def catchword_cases(catchword_id):
    # Fetch list of cases that cite this catchword from neo4j and return their details from mongodb as json
    return('Hello')
