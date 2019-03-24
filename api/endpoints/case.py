from endpoints import app, cors

@app.route('/case/<case_id>', methods=['GET'])
def case_metadata(case_id):
    # Read from mongo
    return('Hello '+case_id)

@app.route('/case/<case_id>/plot_line', methods=['GET'])
def case_line_distribution(case_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    return('Hello')

@app.route('/case/<case_id>/plot_radar', methods=['GET'])
def case_radar_distribution(case_id):
    # Get subjects of particular case, normalize them based on something
    return('Hello')

@app.route('/case/<case_id>/timeline', methods=['GET'])
def case_timeline(case_id):
    # Timeline function
    return('Hello')

@app.route('/case/<case_id>/citations', methods=['GET'])
def case_citations(case_id):
    # Get citer id's from neo4j, and respective names from mongo
    return('Hello')
