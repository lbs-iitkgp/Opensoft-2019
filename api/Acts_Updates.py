ACT_to_ALL_YEARS = dict()


with open('actlist.txt') as f:
    for line in f.readlines():
        line = line.strip()
        Act_name, year = line[:-4], line[-4:]
        if "," in Act_name:
            Act_name = Act_name[:Act_name.index(",")] + Act_name[Act_name.index(",")+1:]
        if "act" in Act_name:
            Act_name = Act_name[:Act_name.index("act")] + Act_name[Act_name.index("act")+3:]
        if "Act" in Act_name:
            Act_name = Act_name[:Act_name.index("Act")] + Act_name[Act_name.index("Act")+3:]

            
        Act_name = Act_name.strip()

        # #if '(Amendment)' in Act_name:
        #     Act_name = Act_name[:Act_name.index('(Amendment)')] + 
        #     Act_name[Act_name.index('(Amendment)')+12:]
        # if 'Amendment)' in Act_name:
        #     ind = (Act_name[:Act_name.index('Amendment)')]).rindex('(')
        #     Act_name = Act_name[:ind] + Act_name[Act_name.index('Amendment)')+11:]

        if Act_name in ACT_to_ALL_YEARS:
            ACT_to_ALL_YEARS[Act_name].append((year, Act_name,))
        else:
            ACT_to_ALL_YEARS[Act_name] = []
            ACT_to_ALL_YEARS[Act_name].append((year, Act_name,))


act_recent_years = {}

for act in ACT_to_ALL_YEARS:
    act_recent_years[act] = []
    for another_act in ACT_to_ALL_YEARS:
        if another_act.find(act) == 0:

            [act_recent_years[act].append(x)
             for x in ACT_to_ALL_YEARS[another_act]]

    # act_recent_years[act].append(ACT_to_ALL_YEARS[act])
casecame = "Code of Criminal Procedure"
print(act_recent_years[casecame])

print(max(act_recent_years[casecame]))
print(len(act_recent_years[casecame]))


# print((ACT_to_ALL_YEARS))
# print(len(ACT_to_ALL_YEARS))

#ACT_to_ALL_YEARS_sorted = ACT_to_ALL_YEARS_sorted
