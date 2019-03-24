from endpoints import app, cors

@app.route('/keyword/<keyword_id>', methods=['GET'])
def keyword_metadata():
    return('Hello')

@app.route('/keyword/<keyword_id>/plot_line', methods=['GET'])
def keyword_line_distribution():
    return('Hello')

@app.route('/keyword/<keyword_id>/plot_radar', methods=['GET'])
def keyword_radar_distribution():
    return('Hello')

@app.route('/keyword/<keyword_id>/cases', methods=['GET'])
def keyword_cases():
    return('Hello')
