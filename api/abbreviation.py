import os
import json
from abbreviations import schwartz_hearst
from env import ENV 
import encode_helper
file = open("data.txt", "w")

all_files = os.listdir("{}/CaseDocuments/All_FT".format(ENV["DATASET_PATH"]))
all_cases = list(filter(lambda x: x[-4:] == ".txt", all_files))[:1000]
abb = {}
ignore = {}
count = 0


def function(word):
    upper_case = 0
    lower_case = 0
    if len(word) > 0:
        if word[0].isupper():
            upper_case += 1
        elif word[0].islower():
            lower_case += 1
    return upper_case, lower_case

def get_abbreviations():

    for case in all_cases:
        with open("{}/CaseDocuments/All_FT/{}".format(ENV["DATASET_PATH"], case), 'r') as file:
            file_content = file.read()
            pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text=file_content)

            for pair in pairs:
                flag = 0

                upper_case, lower_case = function(pair)
                if(lower_case == 0):
                    flag = 1

                words = pairs[pair].split(' ')

                upper_case = 0
                lower_case = 0
                for word in words:
                    upper_case_1, lower_case_1 = function(word)
                    upper_case += upper_case_1
                    lower_case += lower_case_1

                if lower_case == 0 or upper_case/lower_case > 0.8:
                    flag = 1

                if flag == 0:
                    if pair not in ignore:
                        ignore[pair] = []
                        ignore[pair].append(pairs[pair])
                    else:
                        if pairs[pair] not in ignore[pair]:
                            ignore[pair].append((pairs[pair]))
                else:
                    if pair not in abb:
                        abb[pair] = []
                        abb[pair].append(pairs[pair])
                    else:
                        if pairs[pair] not in abb[pair]:
                            abb[pair].append((pairs[pair]))

    actual_abb = {}

    for a in abb:
        if len(abb[a]) > 10:
            ignore[a] = abb[a]
        else:
            actual_abb[a] = abb[a]
            
    temp_list = []
    for act_short_form in actual_abb:
        temp_dict = { "abbrev": act_short_form , "actual" : " ".join(actual_abb[act_short_form])}
        temp_list.append(temp_dict)


    
    return temp_list


if __name__ == "__main__":
    
    print("i am here")
    print(get_abbreviations())
    # with open("abbreviations_t.json", "w") as f:
    #     json.dump(get_abbreviations(), f, indent=4)

    # with open("ignore_t.json", "w") as f:
    #     json.dump(ignore, f, indent=4)
