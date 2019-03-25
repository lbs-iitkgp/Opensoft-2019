from endpoints import app, cors

@app.route('/suggestions', methods=['GET'])
def get_suggestions():
    # Return list of auto-complete suggestions for given query phrase
    #
    # [
    #   { "suggestion": , "score": },
    #   ...
    # ]
    return('Hello')
