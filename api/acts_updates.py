"""makes a dictonary with
    ACT names as keys and the list
        of all its "updated versions with year" tuples as values"""

ACT_TO_ALL_YEARS = dict()


with open('actlist.txt') as f:
    for line in f.readlines():
        line = line.strip()
        Act_name, year = line[:-4], line[-4:]
        if "," in Act_name:
            Act_name = Act_name[:Act_name.index(
                ",")] + Act_name[Act_name.index(",")+1:]
        if "act" in Act_name:
            Act_name = Act_name[:Act_name.index(
                "act")] + Act_name[Act_name.index("act")+3:]
        if "Act" in Act_name:
            Act_name = Act_name[:Act_name.index(
                "Act")] + Act_name[Act_name.index("Act")+3:]

        Act_name = Act_name.strip()

        if Act_name in ACT_TO_ALL_YEARS:
            ACT_TO_ALL_YEARS[Act_name].append((year, Act_name,))
        else:
            ACT_TO_ALL_YEARS[Act_name] = []
            ACT_TO_ALL_YEARS[Act_name].append((year, Act_name,))


ACT_RECENT_YEARS = {}

for act in ACT_TO_ALL_YEARS:
    ACT_RECENT_YEARS[act] = []
    for another_act in ACT_TO_ALL_YEARS:
        if another_act.find(act) == 0:

            [ACT_RECENT_YEARS[act].append(x)
             for x in ACT_TO_ALL_YEARS[another_act]]
