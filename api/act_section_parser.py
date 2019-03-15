from __future__ import unicode_literals
import spacy
import os
import json

all_files = os.listdir("./All_FT")
all_cases = filter(lambda x: x[-4:] == ".txt", all_files)

nlp = spacy.load('en_core_web_sm')

case_dict = {}
for i in range(len(all_cases)):
	file = open("./All_FT/" + all_cases[i], 'r')
	text = ""
	line_num = 1
	#print(all_cases[i])
	case_dict[all_cases[i]] = {}
	prev_act_name = ""
	for line in file:
		text += line
		doc = nlp(text)
		line_words = line.split(" ")

		for entity in doc.ents:
			act_bool = 0
			words = entity.text.split(" ")

			if entity.label_ == u"LAW" :
				if "Act" in words or "Act," in words or "Act." in words:
					act_bool = 1
					if words[0] == "the" or words[0] == "The":
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
						sect_num = parts[1]
						
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

					if act_name != "" and act_name not in case_dict[all_cases[i]]:
						prev_act_name = act_name
						case_dict[all_cases[i]][prev_act_name] = set()
					
					if sect_flag and prev_act_name != "":
						case_dict[all_cases[i]][prev_act_name].add(sect_num)
					#print(prev_act_name)
					if parts[0] in line_words:
						ind = line_words.index(parts[0])
						
						while ind > 0:
							if line_words[ind] == "u/s." or line_words[ind] == "s." or line_words[ind] == "section" or line_words[ind] == "Section" or line_words[ind] == "S.":
								sect_num = line_words[ind + 1]
								case_dict[all_cases[i]][prev_act_name].add(sect_num)
								break
							ind = ind - 1
	
		text = ""

with open("case_acts_sections.json", "w") as write_file:
	json.dump(case_dict, write_file, indent = 4)


