from endpoints import *

@app.route('/dummy_arr', methods=['GET'])
def dummy_arr():
    a = [1,2,3]
    return(jsonify(a))

@app.route('/dummy_dict', methods=['GET'])
def dummy_dict():
    d = {"x": 1, "y": 2, "z": 3}
    return(jsonify(d))

@app.route('/dummy_sum', methods=['GET'])
def dummy_args():
    d = dict()
    x = request.args.get('x')
    y = request.args.get('y')
    d[x] = y
    return(jsonify(d))
