from endpoints import *

@app.route('/case/<case_id>', methods=['GET'])
def case_metadata():
    return('Hello')

@app.route('/case/<case_id>/plot_line', methods=['GET'])
def case_line_distribution():
    return('Hello')

@app.route('/case/<case_id>/plot_radar', methods=['GET'])
def case_radar_distribution():
    return('Hello')

@app.route('/case/<case_id>/timeline', methods=['GET'])
def case_timeline():
    return('Hello')

@app.route('/case/<case_id>/citations', methods=['GET'])
def case_citations():
    return('Hello')
