from endpoints import app, cors

@app.route('/act/<act_id>', methods=['GET'])
def act_metadata():
    return('Hello')

@app.route('/act/<act_id>/plot_line', methods=['GET'])
def act_line_distribution():
    return('Hello')

@app.route('/act/<act_id>/plot_radar', methods=['GET'])
def act_radar_distribution():
    return('Hello')

@app.route('/act/<act_id>/timeline', methods=['GET'])
def act_timeline():
    return('Hello')

@app.route('/act/<act_id>/citations', methods=['GET'])
def act_citations():
    return('Hello')
