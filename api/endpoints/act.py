from endpoints import app, cors

@app.route('/act/<act_id>', methods=['GET'])
def act_metadata(act_id):
    # Fetch filename path from mongodb
    return('Hello')

@app.route('/act/<act_id>/sections', methods=['GET'])
def act_sections(act_id):
    # Fetch sections for a particular act from file
    return('Hello')

@app.route('/act/<act_id>/section/<section_id>', methods=['GET'])
def act_sections(act_id, section_id):
    # Fetch sections for a particular act from file
    return('Hello')

@app.route('/act/<act_id>/plot_line', methods=['GET'])
def act_line_distribution(act_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    return('Hello')

@app.route('/act/<act_id>/plot_radar', methods=['GET'])
def act_radar_distribution(act_id):
    # Fetch cases that cite this act from neo4j, and have a distribution of keywords
    return('Hello')

@app.route('/act/<act_id>/cases', methods=['GET'])
def act_citations(act_id):
    # Fetch list of cases that cite this act from neo4j and return their details from mongodb as json
    return('Hello')
