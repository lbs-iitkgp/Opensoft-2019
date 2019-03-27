from endpoints import *
import os
import json
import re
from string_matching import 
@app.route('/suggestions', methods=['GET'])
def get_suggestions():
    PATH = os.path.join('base_class', 'act.json')
    file = open(PATH, 'r')
    act_list = json.loads(file.read())
    acts = [act_data[0] for act_data in act_list]

    return('Hello')