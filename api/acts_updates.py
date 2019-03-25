import json
import re
"""makes a dictionary with
    ACT names as keys and the list
        of all its "updated versions with year" tuples as values"""

ACT_TO_ALL_YEARS = dict()
primary = dict() #temporary funny dictonary
rem  = dict()
i = 1
with open('actlist.txt') as f:

    for line in f.readlines():
        line = line.strip()
        Act_name, year = line[:-4], line[-4:]
        Act_name = Act_name.strip()
        removed = ''
        if "," in Act_name:
            Act_name = Act_name[:Act_name.index(
                ",")] + Act_name[Act_name.index(",")+1:]

        if 'Act' in Act_name:
            removed = 'Act'
            Act_name = Act_name[:Act_name.rindex('Act')]

        if 'act' in Act_name:
            removed = 'act'
            Act_name = Act_name[:Act_name.rindex('act')]

        Act_name = Act_name.strip()

        rem[Act_name] = removed
        # print(Act_name)

        if Act_name in ACT_TO_ALL_YEARS:
            ACT_TO_ALL_YEARS[Act_name].append((year, Act_name,))
        else:
            ACT_TO_ALL_YEARS[Act_name] = []
            ACT_TO_ALL_YEARS[Act_name].append((year, Act_name,))

        # return rem

ACT_RECENT_YEARS = {}

for act in ACT_TO_ALL_YEARS:
    ACT_RECENT_YEARS[act + ' ' +  rem[act]] = []
    for another_act in ACT_TO_ALL_YEARS:
        print(another_act)
        if another_act.find(act) == 0:
            print(another_act)
            print(act)
            [ACT_RECENT_YEARS[act + ' ' +  rem[act]].append(x + ' ' + rem[x])for x in ACT_TO_ALL_YEARS[another_act]] 
            print(another_act)
# print(json.dumps(ACT_TO_ALL_YEARS, indent=4, sort_keys=True))
# print(ACT_RECENT_YEARS["Andhra Pradesh General Sales Tax (Second Amendment)"])
# print((ACT_RECENT_YEARS["Andhra Pradesh General Sales Tax"]))




with open('ACTS_TO_ALL_YEARS.json','w') as f:
    json.dump(ACT_RECENT_YEARS,f,indent=4)