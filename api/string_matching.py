def find_score(query, text):
    score_without_bracket = -1
    bracket_regex = '(\(((\w|\s|\.)+)\))'
    match = re.search(bracket_regex, text)
    if match:
        score_without_bracket = fuzz.token_set_ratio(query, text.replace(match.groups()[0], ''))
    # if query[-4:].isnumeric() and text[-4:].isnumeric():
    #     query_year = int(query[-4:])
    #     text_year = int(text[-4:])
    #     return fuzz.token_set_ratio(query, text) + 100 - abs(query_year - text_year)/(2018 - 1900)*100
    return max(score_without_bracket, fuzz.token_set_ratio(query, text))


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
