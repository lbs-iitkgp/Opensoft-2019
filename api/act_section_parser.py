from __future__ import unicode_literals
import spacy
import os
import json
import editdistance
import difflib

all_files = os.listdir("./All_FT")
all_cases = filter(lambda x: x[-4:] == ".txt", all_files)

# ch = 'A'
# all_acts = []
# while ch < 'Z':
# 	if ch == 'Q' or ch == 'X':
# 		ch = chr(ord(ch) + 1)
# 		continue
# 	all_acts_in_alpha = os.listdir("./Acts/Central_Text/" + ch)
# 	acts = filter(lambda x: x[-4:] == ".txt", all_acts_in_alpha)
# 	acts = [x[:-4] for x in acts]
# 	all_acts.extend(acts)
# 	ch = chr(ord(ch) + 1)

BAD_WORDS_TYPE1 = ["the", "The", "that", "That", "This", "this", "under", "Under"]

BAD_WORDS_TYPE2 = ["Section", "S.", "s.", "u/s.", "section", "Article", "article"]

def fetch_all_acts():
	with open("ACTS_BY_STATES.json") as f:
	 	acts_dict = json.load(f)

	all_acts = acts_dict.keys()
	return all_acts

def fetch_acts_from_cases(all_acts):
	nlp = spacy.load('en_core_web_sm')
	case_dict = {}
	act_cases = {}
	total_num_cases = len(all_cases)
	for j in range(total_num_cases):
		file = open("./All_FT/" + all_cases[j], 'r')
		text = ""
		line_num = 1
		#print(all_cases[j])
		case_dict[all_cases[j]] = {}
		act_cases[all_cases[j]] = set()
		prev_act_name = ""
		year = ""
		for line in file:
			if "u/s." in line :
				line = line.replace("u/s.", "Section")
			if " s." in line:
				line = line.replace(" s.", " Section")
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
					#print("Spacey : ", entity.text)
					if "Act" in words or "Act," in words or "Act." in words:
						act_bool = 1
						if words[0] in BAD_WORDS_TYPE1:
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
						if parts[0] in BAD_WORDS_TYPE2:
							i = 0
							sect_flag = 1
							a = 0
							parts_len = len(parts)
							while a < parts_len:
								if parts[a][0] >= '0' and parts[a][0] <= '9':
									sect_num = parts[a]
									break
								a = a + 1
							while parts[i] not in BAD_WORDS_TYPE1:
								i = i + 1
								if i >= parts_len:
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

						prev_act_name = act_name
						#print("Yo, ", prev_act_name)
						if prev_act_name == "":
							continue
						if len(difflib.get_close_matches(prev_act_name, all_acts)) > 0:
							prev_act_name = difflib.get_close_matches(prev_act_name, all_acts)[0]
						#else:
						#	print(prev_act_name)

						ind = 0
						sect_num = ""
						line_length = len(line)
						if "Section" in line:
							ind = line.index("Section")
							ind = ind + 7
						while(line[ind] == " "):
							ind = ind + 1
							if ind >= line_length:
								break
						if ind < line_length:
							while(line[ind] != " "):
								sect_num += line[ind]
								ind += 1
								if ind >= line_length:
									break
						if prev_act_name not in case_dict[all_cases[j]]:
							act_cases[all_cases[j]].add(prev_act_name)
						if sect_flag and prev_act_name != "":
							act_cases[all_cases[j]].add(prev_act_name)
								
			text = ""
	for case in act_cases:
		act_cases[case] = list(act_cases[case])
	with open("acts_from_cases.json", "w") as write_file:
		json.dump(act_cases, write_file, indent = 4)

	return act_cases

def fetch_section_act_mapping_from_case(all_acts):
	nlp = spacy.load('en_core_web_sm')

	case_dict = {}
	total_num_cases = len(all_cases)
	for j in range(total_num_cases):
		file = open("./All_FT/" + all_cases[j], 'r')
		text = ""
		line_num = 1
		print(all_cases[j])
		case_dict[all_cases[j]] = {}
		prev_act_name = ""
		year = ""
		for line in file:
			if "u/s." in line :
				line = line.replace("u/s.", "Section")
			if " s." in line:
				line = line.replace(" s.", " Section")
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
					#print("Spacey : ", entity.text)
					if "Act" in words or "Act," in words or "Act." in words:
						act_bool = 1
						if words[0] in BAD_WORDS_TYPE1:
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
						if parts[0] in BAD_WORDS_TYPE2:
							i = 0
							sect_flag = 1
							a = 0
							parts_len = len(parts)
							while a < parts_len:
								if parts[a][0] >= '0' and parts[a][0] <= '9':
									sect_num = parts[a]
									break
								a = a + 1
							while parts[i] not in BAD_WORDS_TYPE1:
								i = i + 1
								if i >= parts_len:
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

						prev_act_name = act_name
						#print("Yo, ", prev_act_name)
						if prev_act_name == "":
							continue
						if len(difflib.get_close_matches(prev_act_name, all_acts)) > 0:
							prev_act_name = difflib.get_close_matches(prev_act_name, all_acts)[0]
						#else:
						#	print(prev_act_name)
						print(prev_act_name)
						ind = 0
						sect_num = ""
						line_length = len(line)
						if "Section" in line:
							ind = line.index("Section")
							ind = ind + 7
						while(line[ind] == " "):
							ind = ind + 1
							if ind >= line_length:
								break
						if ind < line_length:
							while(line[ind] != " "):
								sect_num += line[ind]
								ind += 1
								if ind >= line_length:
									break
						if prev_act_name not in case_dict[all_cases[j]]:
							case_dict[all_cases[j]][prev_act_name] = set()

						if sect_flag and prev_act_name != "":
							case_dict[all_cases[j]][prev_act_name].add(sect_num)
						
					elif "Section" in words:
						t = words.index("Section") + 1
						if t < len(words):
							sect_num = words[t]
							if prev_act_name != "":
								case_dict[all_cases[j]][prev_act_name].add(sect_num)

				
			text = ""
	for case_id in case_dict:
		for act in case_dict[case_id]:
			case_dict[case_id][act] = list(case_dict[case_id][act])
	with open("section_act_mapping_from_case.json", "w") as write_file:
		json.dump(case_dict, write_file, indent = 4)
	return case_dict

print("################################################################")
print("Hey There!")
print("If you want act to case mapping in a json, press 1")
print("If you want section to act to case mapping in a json, press 2")
choice = input()
if choice == 1:
	act_to_case = fetch_acts_from_cases(fetch_all_acts())

if choice == 2:
	sect_to_act_to_case = fetch_section_act_mapping_from_case(fetch_all_acts())

