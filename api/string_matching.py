from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
import json
import re


def find_score(query, text):
    '''
    Finds the similarity score between the query and the given text.
    '''
    score_without_bracket = -1
    bracket_regex = '(\(((\w|\s|\.)+)\))'
    match = re.search(bracket_regex, text)
    if match:
        score_without_bracket = fuzz.token_set_ratio(query, text.replace(match.groups()[0], ''))
    return max(score_without_bracket, fuzz.token_set_ratio(query, text))


def get_closest_match(query, suggestions):
    '''
    Finds the closest matched string given a query and a list of suggestions.
    Sorts the suggestions list in descending order according to their similarity score with the query.
    returns the first one from the list.
    '''
    suggestions = [(text, find_score(query, text)) for text in suggestions]
    suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)
    return suggestions[0]


if __name__ == '__main__':
    PATH = os.path.join('base_class', 'act.json')
    file = open(PATH, 'r')
    act_list = json.loads(file.read())
    acts = [act_data[0] for act_data in act_list]

    query = input("Enter Act name : ")

    print(get_closest_match(query, acts))
