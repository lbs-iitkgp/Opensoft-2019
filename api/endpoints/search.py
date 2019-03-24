from endpoints import app, cors

@app.route('/search/advanced', methods=['GET', 'POST'])
def advanced_search():
# [
#   {
#       "case_id": 4,
#       "case_name": "X vs Y",
#       ...
#   },
#   ...
# ]
#
    return('Hello')

@app.route('/search/basic', methods=['GET', 'POST'])
def basic_search():
# [
#   {
#       "type": "JUDGE",
#       "name": "Judge name",
#       "toggle_state": true
#   },
#   {
#   }
# ]
#
    return('Hello')
