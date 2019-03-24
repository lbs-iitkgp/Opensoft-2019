from endpoints import app, cors

@app.route('/judge/<judge_id>', methods=['GET'])
def judge_metadata():
    return('Hello')

@app.route('/judge/<judge_id>/plot_line', methods=['GET'])
def judge_line_distribution():
    return('Hello')

@app.route('/judge/<judge_id>/plot_radar', methods=['GET'])
def judge_radar_distribution():
    return('Hello')

@app.route('/judge/<judge_id>/cases', methods=['GET'])
def judge_cases():
    return('Hello')
