def get_closest_match(query, suggestions):

    suggestions = [(text, find_score(query, text)) for text in suggestions]
    # suggestions = sorted(suggestions, key=lambda x: fuzz.token_set_ratio(query, x), reverse=True)
    suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)
    # return [text for text in suggestions if text[1] >= 0.9 * suggestions[0][1] and text[1] <= 1.1 * suggestions[0][1]]
    # return [text for text in suggestions if text[1] == suggestions[0][1]]
    return suggestions[0]

  
PATH = os.path.join('base_class', 'act.json')
file = open(PATH, 'r')
act_list = json.loads(file.read())
acts = [act_data[0] for act_data in act_list]

query = input("Enter Act name : ")
