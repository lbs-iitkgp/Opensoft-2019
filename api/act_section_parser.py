from __future__ import unicode_literals
import spacy
import os
import json
import editdistance
import difflib

all_files = os.listdir("./All_FT")
all_cases = filter(lambda x: x[-4:] == ".txt", all_files)

ch = 'A'
all_acts = []
while ch < 'Z':
	if ch == 'Q' or ch == 'X':
		ch = chr(ord(ch) + 1)
		continue
	all_acts_in_alpha = os.listdir("./Acts/Central_Text/" + ch)
	acts = filter(lambda x: x[-4:] == ".txt", all_acts_in_alpha)
	acts = [x[:-4] for x in acts]
	all_acts.extend(acts)
	ch = chr(ord(ch) + 1)


nlp = spacy.load('en_core_web_sm')

case_dict = {}
act_cases = {}
for j in range(200):
	file = open("./All_FT/" + all_cases[j], 'r')
	text = ""
	line_num = 1
	print(all_cases[j])
	case_dict[all_cases[j]] = {}
	act_cases[all_cases[j]] = set()
	prev_act_name = ""
	year = ""
	for line in file:
		if "u/s." in line :
			line = line.replace("u/s.", "Section")
		if "s." in line:
			line = line.replace("s.", "Section")
		if "S." in line:
			line = line.replace("S.", "Section")
		if "section" in line:
			line = line.replace("section", "Section")
		if "the Act" in line:
			line = line.replace("the Act", prev_act_name)
		if "this Act" in line:
			line = line.replace("this Act", prev_act_name)
		if "that Act" in line:
			line = line.replace("that Act", prev_act_name)
		text += line
		doc = nlp(text)
		line_words = line.split(" ")
		for entity in doc.ents:
			act_bool = 0
			words = entity.text.split(" ")
			if entity.label_ == u"LAW" :
				if "Act" in words or "Act," in words or "Act." in words:
					act_bool = 1
					if words[0] == "the" or words[0] == "The" or words[0] == "that" or words[0] == "That" or words[0] == "this" or words[0] == "This" or words[0] == "under" or words[0] == "Under":
						words = words[1:]

					act_name = ""
					for word in words:
						if act_name == "":
							act_name = act_name + word
						else:
							act_name = act_name + " " + word 
					
					parts = act_name.split(" ")
					
					sect_flag = 0
					sect_num = -1
					if parts[0] == "Section" or parts[0] == "S." or parts[0] == "section" or parts[0] == "s." or parts[0] == "u/s." or parts[0] == "Article":
						i = 0
						sect_flag = 1
						a = 0
						while a < len(parts):
							if parts[a][0] >= '0' and parts[a][0] <= '9':
								sect_num = parts[a]
								break
							a = a + 1
						while parts[i] != "the":
							i = i + 1
							if i >= len(parts):
								break
						parts = parts[i + 1:]
						act_name = ""
						for part in parts:
							if act_name == "":
								act_name = act_name + part
							else:
								act_name = act_name +" " + part

					if len(parts) <= 1:
						continue

					minima = 1000000
					# if act_name != "" and act_name not in case_dict[all_cases[j]]:
					# 	prev_act_name = act_name
					# 	for actual_act in all_acts:
					# 		if(editdistance.eval(prev_act_name, actual_act) < minima):
					# 			minima = editdistance.eval(prev_act_name, actual_act)
					# 	case_dict[all_cases[j]][prev_act_name] = []
					# 	act_cases[all_cases[j]].add(prev_act_name)
					# if sect_flag and prev_act_name != "":
					# 	case_dict[all_cases[j]][prev_act_name].append(sect_num)
					# 	act_cases[all_cases[j]].add(prev_act_name)
					# print(prev_act_name)

					prev_act_name = act_name
					if prev_act_name == "":
						continue
					if len(difflib.get_close_matches(prev_act_name, all_acts)) > 0:
						prev_act_name = difflib.get_close_matches(prev_act_name, all_acts)[0]

					if prev_act_name not in case_dict[all_cases[j]]:
						case_dict[all_cases[j]][prev_act_name] = []
						act_cases[all_cases[j]].add(prev_act_name)
					if sect_flag and prev_act_name != "":
						case_dict[all_cases[j]][prev_act_name].append(sect_num)
						act_cases[all_cases[j]].add(prev_act_name)
					print(prev_act_name)
					# if parts[0] in line_words:
					# 	ind = line_words.index(parts[0])
					# 	while ind > 0:
					# 		if line_words[ind] == "u/s." or line_words[ind] == "s." or line_words[ind] == "section" or line_words[ind] == "Section" or line_words[ind] == "S.":
								
					# 			case_dict[all_cases[j]][prev_act_name].append(sect_num)
					# 			break
					# 		ind = ind - 1
					ind = 0
					if " u/s. " in line:
						ind = line_words.index("u/s.")
					if " s. " in line:
						ind = line_words.index("s.")
					if " section " in line:
						ind = line_words.index("section")
					if " Section " in line:
						ind = line_words.index("Section")
					if " S. " in line:
						ind = line_words.index("S.")
					while ind < len(line_words):
						pot_num = line_words[ind]
						if pot_num[0] >= '0' and pot_num[0] <= '9':
							sect_num = pot_num
							case_dict[all_cases[j]][prev_act_name].append(sect_num)
							break
						ind = ind + 1
			
		text = ""

for case_id in act_cases:
	act_cases[case_id] = list(act_cases[case_id])

with open("just_acts_and_cases.json", "w") as write_file:
	json.dump(act_cases, write_file, indent = 4)


