from endpoints import app, cors

@app.route('/catchword/<catchword_id>', methods=['GET'])
def catchword_metadata():
    return('Hello')

@app.route('/catchword/<catchword_id>/plot_line', methods=['GET'])
def catchword_line_distribution():
    return('Hello')

@app.route('/catchword/<catchword_id>/plot_radar', methods=['GET'])
def catchword_radar_distribution():
    return('Hello')

@app.route('/catchword/<catchword_id>/cases', methods=['GET'])
def catchword_cases():
    return('Hello')
