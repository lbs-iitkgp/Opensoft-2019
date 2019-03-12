import os
import json
import networkx as nx

j = nx.DiGraph()

judge_names_dict_final = {}

all_files = os.listdir("./All_FT")
all_cases = list(filter(lambda x: x[-4:] == ".txt", all_files))
print(len(all_cases))
judge_names = {}

judge_names_as_set = []
case_without_judge = 0
flag = 0
first_line = 1
for case in all_cases:
    file = open("./All_FT/" + case, 'r')
    flag = 0
    first_line = 1
    for line in file:
        line = line[0: -1]

        if first_line:
            title = line
            first_line = 0

        words = line.split(" ")

        search_str1 = "Judgement"
        search_str2 = "Judgment"
        search_str3 = "judgement"
        search_str4 = "judgment"
        search_str5 = "delivered"

        year = case[0:4]

        if year in words and len(words) <= 4:
            date_line = line

        if (search_str1 in words or search_str2 in words or search_str3 in words or search_str4 in words) and search_str5 in words:
            flag = 1
            for i in range(len(words)):
                if words[i] == "by:" or words[i] == ":":
                    name = ""
                    i = i + 1

                    while i < len(words):
                        name = name + " " + words[i]
                        i = i + 1

                    if ':' in name:
                        name = name[: name.index(':')] + name[name.index(':') + 1:]

                    if ',' in name:
                        name = name[: name.index(',')] + name[name.index(',') + 1:]

                    if name != "":
                        if name in judge_names:
                            judge_names[name].append({"Case": case, "Date": date_line, "Title": title})
                        else:
                            judge_names[name] = []
                            judge_names[name].append({"Case": case, "Date": date_line, "Title": title})
                        break

                elif words[i] == "by":
                    name = ""
                    i = i + 1

                    while i < len(words):
                        name = name + " " + words[i]
                        i = i + 1

                    if ':' in name:
                        name = name[: name.index(':')] + name[name.index(':') + 1:]

                    if ',' in name:
                        name = name[: name.index(',')] + name[name.index(',') + 1:]
                    name = name.strip()
                    if name != "":
                        if name in judge_names:
                            judge_names[name].append({"Case": case, "Date": date_line, "Title": title})
                        else:
                            judge_names[name] = []
                            judge_names[name].append({"Case": case, "Date": date_line, "Title": title})
                        break
            break
print(len(judge_names))

judge_names_as_list = []


for judge in judge_names:
    s = set()
    [s.add(k) for k in judge.split()]
    if s not in judge_names_as_set:
        judge_names_dict_final[judge] = []
        judge_names_dict_final[judge].append(judge_names[judge])
        judge_names_as_set.append(s)
        judge_names_as_list.append(judge)
    else:
        judge_names_dict_final[judge_names_as_list[judge_names_as_set.index(s)]].append(judge_names[judge])


CASE_FILE_TO_ID = dict()


with open('doc_path_ttl_id.txt') as f:
    for line in f.readlines():
        line = line.strip()
        file_name, title, case_id = line.split("-->")
        CASE_FILE_TO_ID[file_name] = case_id

for k in judge_names_as_list:
    for diction in judge_names_dict_final[k]:
        for x in range(len(diction)):
            if diction[x]["Case"][:-4] in CASE_FILE_TO_ID:
                j.add_edge(k, CASE_FILE_TO_ID[diction[x]["Case"][:-4]])

print(len(j.nodes()))

print(j[judge_names_as_list[0]])
