from endpoints import *

@app.route('/suggestions', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def get_suggestions():
    # Return list of auto-complete suggestions for given query phrase
    #
    # [
    #   { "suggestion": , "score": },
    #   ...
    # ]
    return('Hello')