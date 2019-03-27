from __future__ import unicode_literals
import spacy
import os
import json
import editdistance
import difflib
import regex as re

from env import ENV

all_files = os.listdir("{}/All_FT".format(ENV["DATASET_PATH"]))
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

word_to_replace_dict = {"u/s." : "Section", " s. ":"Section", "S. ":"Section", "section":"Section",\
						"subSection":"Section", "subsection":"Section"}

act_replacement = ["the Act", "this Act", "that Act", "the said Act", "the act", "this act", "that act", "the said act"]
def fetch_all_acts():
	with open("ACTS_BY_STATES.json") as f:
	 	acts_dict = json.load(f)

	all_acts = acts_dict.keys()
	return all_acts


def fetch_all_acts_from_txt():
	file = open("{}/Acts/all_acts_central_state.txt".format(ENV["DATASET_PATH"]), "r")
	acts_list = []
	for line in file:
		line = line[:-1]
		acts_list.append(line)
	return acts_list

def fetch_acts_from_cases(all_acts):
	nlp = spacy.load('en_core_web_sm')
	case_dict = {}
	act_cases = {}
	total_num_cases = len(all_cases)
	for j in range(total_num_cases):
		file = open("{}/All_FT/{}".format(ENV["DATASET_PATH"], all_cases[j]), 'r')
		#file = open("./All_FT/2003_C_16.txt", 'r')
		text = ""
		line_num = 1
		#print(all_cases[j])
		case_dict[all_cases[j]] = {}
		act_cases[all_cases[j]] = set()
		prev_act_name = ""
		year = ""
		dada_act_name = ""
		acts_so_far = {}
		for line in file:
			for wrong in word_to_replace_dict:
				if wrong in line:
					line = line.replace(wrong, word_to_replace_dict[wrong])
			for pronoun in act_replacement:
				if pronoun in line:
					line = line.replace(pronoun, prev_act_name)
			actual_line = line
			line = re.sub(r"[-()\"#/'@;<>{}`+=~|!?]", '', line)
			text += line
			doc = nlp(text)
			line_words = line.split(" ")
			actual_line_words = actual_line.split(" ")
			for entity in doc.ents:
				act_bool = 0
				words = entity.text.split(" ")
				if "Act" in words or "Act," in words or "Act." in words:
					act_bool = 1
					if words[0] in BAD_WORDS_TYPE1:
						words = words[1:]
					year = ""
					ent_ind = line.index(entity.text)
					ent_ind = ent_ind + len(entity.text)
					while ent_ind < len(line):
						if line[ent_ind] >= '0' and line[ent_ind] <= '9':
							year += line[ent_ind]
						ent_ind += 1
					if len(year) != 4:
						year = ""

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

					dada_act_name = prev_act_name
					prev_act_name = act_name
					if year != "":
						prev_act_name = prev_act_name + " " + year
					parsed_by_spacy = prev_act_name

					print("Yo, ", prev_act_name)
					if prev_act_name == "":
						continue
					
					if parsed_by_spacy in acts_so_far:
						prev_act_name = acts_so_far[parsed_by_spacy]
					else:
						possible = difflib.get_close_matches(prev_act_name, all_acts, 5)
						if len(possible) > 0:
							max_count = 0
							#print(possible)
							for i in range(len(possible)):
								match_count = 0
								bas = possible[i]
								w = possible[i].split(" ")
								for a in w:
									if a.lower() in [f.lower() for f in line_words]:
										match_count += 1
								if match_count >= max_count:
									max_count = match_count
									prev_act_name = possible[i]
							checker = prev_act_name.split(" ")
							if checker[0].lower() not in [v.lower() for v in line_words]:
								if dada_act_name != "":
									prev_act_name = dada_act_name
					print(prev_act_name)
					if parsed_by_spacy not in acts_so_far:
						acts_so_far[parsed_by_spacy] = prev_act_name
					line_of_act = 0
					loc_of_act = 0
					line_of_act = line_num
					for each_word in prev_act_name.split(" "):
						if each_word in line_words:
							loc_of_act = line_words.index(each_word)

					
					if prev_act_name != "":
						act_cases[all_cases[j]].add(prev_act_name)
								
			text = ""
	for case in act_cases:
		act_cases[case] = list(act_cases[case])
	# with open("acts_from_cases.json", "w") as write_file:
	# 	json.dump(act_cases, write_file, indent = 4)

	return act_cases

def fetch_section_act_mapping_from_case(all_acts):
	nlp = spacy.load('en_core_web_sm')

	case_dict = {}
	total_num_cases = len(all_cases)
	for j in range(total_num_cases):
		file = open("{}/All_FT/{}".format(ENV["DATASET_PATH"], all_cases[j]), 'r')
		text = ""
		line_num = 0
		print(all_cases[j])
		case_dict[all_cases[j]] = {}
		prev_act_name = ""
		dada_act_name = ""
		year = ""
		acts_so_far = {}
		sect_num = {}
		for line in file:
			for wrong in word_to_replace_dict:
				if wrong in line:
					line = line.replace(wrong, word_to_replace_dict[wrong])
			for pronoun in act_replacement:
				if pronoun in line:
					line = line.replace(pronoun, prev_act_name)
			actual_line = line
			line = re.sub(r"[-()\"#/'@;<>{}`+=~|!?]", '', line)
			text += line
			doc = nlp(text)
			line_num += 1
			line_words = line.split(" ")
			actual_line_words = actual_line.split(" ")
			for entity in doc.ents:
				act_bool = 0
				words = entity.text.split(" ")
				if "Act" in words or "Act," in words or "Act." in words:
					act_bool = 1
					if words[0] in BAD_WORDS_TYPE1:
						words = words[1:]
					year = ""
					ent_ind = line.index(entity.text)
					ent_ind = ent_ind + len(entity.text)
					while ent_ind < len(line):
						if line[ent_ind] >= '0' and line[ent_ind] <= '9':
							year += line[ent_ind]
						ent_ind += 1
					if len(year) != 4:
						year = ""

					act_name = ""
					for word in words:
						if act_name == "":
							act_name = act_name + word
						else:
							act_name = act_name + " " + word 
					
					parts = act_name.split(" ")
					
					sect_flag = 0
					if parts[0] in BAD_WORDS_TYPE2:
						i = 0
						sect_flag = 1
						a = 0
						parts_len = len(parts)
						while a < parts_len:
							if parts[a][0] >= '0' and parts[a][0] <= '9':
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
					
					dada_act_name = prev_act_name
					prev_act_name = act_name
					if year != "":
						prev_act_name = prev_act_name + " " + year
					print("Yo, ", prev_act_name)
					if prev_act_name == "":
						continue

					parsed_by_spacy = prev_act_name
					if parsed_by_spacy in acts_so_far:
						prev_act_name = acts_so_far[parsed_by_spacy]
					else:
						possible = difflib.get_close_matches(prev_act_name, all_acts, 5)
						if len(possible) > 0:
							max_count = 0
							#print(possible)
							for i in range(len(possible)):
								match_count = 0
								bas = possible[i]
								w = possible[i].split(" ")
								for a in w:
									if a.lower() in [f.lower() for f in line_words]:
										match_count += 1
								if match_count >= max_count:
									max_count = match_count
									prev_act_name = possible[i]
							checker = prev_act_name.split(" ")
							if checker[0].lower() not in [v.lower() for v in line_words]:
								if dada_act_name != "":
									prev_act_name = dada_act_name
					print(prev_act_name)
					if parsed_by_spacy not in acts_so_far:
						acts_so_far[parsed_by_spacy] = prev_act_name
					line_of_act = 0
					loc_of_act = 0
					line_of_act = line_num
					for each_word in prev_act_name.split(" "):
						if each_word in line_words:
							loc_of_act = line_words.index(each_word)

					ind = 0
					
					while ind < len(actual_line_words):
						if actual_line_words[ind] == "Section":
							if actual_line_words[ind + 1][0] >= '0' and actual_line_words[ind + 1][0] <= '9':
								if actual_line_words[ind + 1] in sect_num:
									sect_num[actual_line_words[ind + 1]].add(str(line_num) + ',' + str(ind + 1))
								else:
									sect_num[actual_line_words[ind + 1]] = set()
									sect_num[actual_line_words[ind + 1]].add(str(line_num) + ',' + str(ind + 1))
						ind = ind + 1
					if prev_act_name not in case_dict[all_cases[j]] and prev_act_name != "":
						case_dict[all_cases[j]][prev_act_name] = {}
						case_dict[all_cases[j]][prev_act_name]["Section"] = sect_num
						case_dict[all_cases[j]][prev_act_name]["Location"] = set()
						case_dict[all_cases[j]][prev_act_name]["Location"].add(str(line_num) + ',' + str(loc_of_act))
					if prev_act_name in case_dict[all_cases[j]]:
						case_dict[all_cases[j]][prev_act_name]["Location"].add(str(line_num) + ',' + str(loc_of_act))
	
				if "Section" in words:
					#t = words.index("Section") + 1
					e = 0
					while e < len(actual_line_words):
						if actual_line_words[e] == "Section":
							if actual_line_words[e + 1][0] >= '0' and actual_line_words[e + 1] <= '9': 
								if actual_line_words[e + 1] in sect_num:
									sect_num[actual_line_words[e + 1]].add(str(line_num) + ',' +  str(e + 1))
								else:
									sect_num[actual_line_words[e + 1]] = set()
									sect_num[actual_line_words[e + 1]].add(str(line_num) + ',' + str(e + 1))
						e = e + 1
					if prev_act_name != "":
						case_dict[all_cases[j]][prev_act_name]["Section"] = sect_num

				
			text = ""
	# for case_id in case_dict:
	# 	for act in case_dict[case_id]:
	# 		case_dict[case_id][act]["Section"] = list(case_dict[case_id][act]["Section"])
	for case_id in case_dict:
		for act in case_dict[case_id]:
			case_dict[case_id][act]["Location"] = list(case_dict[case_id][act]["Location"])
			for section in case_dict[case_id][act]["Section"]:
				case_dict[case_id][act]["Section"][section] = list(case_dict[case_id][act]["Section"][section])
	# with open("section_act_mapping_from_case.json", "w") as write_file:
	# 	json.dump(case_dict, write_file, indent = 4)
	return case_dict

def fetch_mappings_of_given_case(case_id):
	# case_dict = fetch_section_act_mapping_from_case(fetch_all_acts())
	# # with open("mappings_of_given_case.json", "w") as write_file:
	# # 	json.dump(case_dict[case_id], write_file, indent = 4)
	# return case_dict[case_id]
	nlp = spacy.load('en_core_web_sm')
	case_dict = {}
	file = open("{}/All_FT/{}".format(ENV["DATASET_PATH"], case_id), 'r')
	all_acts = fetch_all_acts_from_txt()
	text = ""
	line_num = 0
	print(case_id)
	case_dict[case_id] = {}
	prev_act_name = ""
	dada_act_name = ""
	year = ""
	acts_so_far = {}
	sect_num = {}
	for line in file:
		for wrong in word_to_replace_dict:
			if wrong in line:
				line = line.replace(wrong, word_to_replace_dict[wrong])
		for pronoun in act_replacement:
			if pronoun in line:
				line = line.replace(pronoun, prev_act_name)
		actual_line = line
		line = re.sub(r"[-()\"#/'@;<>{}`+=~|!?]", '', line)
		text += line
		doc = nlp(text)
		line_num += 1
		line_words = line.split(" ")
		actual_line_words = actual_line.split(" ")
		for entity in doc.ents:
			act_bool = 0
			words = entity.text.split(" ")
			if "Act" in words or "Act," in words or "Act." in words:
				act_bool = 1
				if words[0] in BAD_WORDS_TYPE1:
					words = words[1:]
				year = ""
				ent_ind = line.index(entity.text)
				ent_ind = ent_ind + len(entity.text)
				while ent_ind < len(line):
					if line[ent_ind] >= '0' and line[ent_ind] <= '9':
						year += line[ent_ind]
					ent_ind += 1
				if len(year) != 4:
					year = ""

				act_name = ""
				for word in words:
					if act_name == "":
						act_name = act_name + word
					else:
						act_name = act_name + " " + word 
				
				parts = act_name.split(" ")
				
				sect_flag = 0
				if parts[0] in BAD_WORDS_TYPE2:
					i = 0
					sect_flag = 1
					a = 0
					parts_len = len(parts)
					while a < parts_len:
						if parts[a][0] >= '0' and parts[a][0] <= '9':
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
				
				dada_act_name = prev_act_name
				prev_act_name = act_name
				if year != "":
					prev_act_name = prev_act_name + " " + year
				print("Yo, ", prev_act_name)
				if prev_act_name == "":
					continue

				parsed_by_spacy = prev_act_name
				if parsed_by_spacy in acts_so_far:
					prev_act_name = acts_so_far[parsed_by_spacy]
				else:
					possible = difflib.get_close_matches(prev_act_name, all_acts, 5)
					if len(possible) > 0:
						max_count = 0
						#print(possible)
						for i in range(len(possible)):
							match_count = 0
							bas = possible[i]
							w = possible[i].split(" ")
							for a in w:
								if a.lower() in [f.lower() for f in line_words]:
									match_count += 1
							if match_count >= max_count:
								max_count = match_count
								prev_act_name = possible[i]
						checker = prev_act_name.split(" ")
						if checker[0].lower() not in [v.lower() for v in line_words]:
							if dada_act_name != "":
								prev_act_name = dada_act_name
				print(prev_act_name)
				if parsed_by_spacy not in acts_so_far:
					acts_so_far[parsed_by_spacy] = prev_act_name
				line_of_act = 0
				loc_of_act = 0
				line_of_act = line_num
				for each_word in prev_act_name.split(" "):
					if each_word in line_words:
						loc_of_act = line_words.index(each_word)

				ind = 0
				
				while ind < len(actual_line_words):
					if actual_line_words[ind] == "Section":
						if actual_line_words[ind + 1][0] >= '0' and actual_line_words[ind + 1][0] <= '9':
							if actual_line_words[ind + 1] in sect_num:
								sect_num[actual_line_words[ind + 1]].add(str(line_num) + ',' + str(ind + 1))
							else:
								sect_num[actual_line_words[ind + 1]] = set()
								sect_num[actual_line_words[ind + 1]].add(str(line_num) + ',' + str(ind + 1))
					ind = ind + 1
				if prev_act_name not in case_dict[case_id] and prev_act_name != "":
					case_dict[case_id][prev_act_name] = {}
					case_dict[case_id][prev_act_name]["Section"] = sect_num
					case_dict[case_id][prev_act_name]["Location"] = set()
					case_dict[case_id][prev_act_name]["Location"].add(str(line_num) + ',' + str(loc_of_act))
				if prev_act_name in case_dict[case_id]:
					case_dict[case_id][prev_act_name]["Location"].add(str(line_num) + ',' + str(loc_of_act))

			if "Section" in words:
				#t = words.index("Section") + 1
				e = 0
				while e < len(actual_line_words):
					if actual_line_words[e] == "Section":
						if actual_line_words[e + 1][0] >= '0' and actual_line_words[e + 1] <= '9': 
							if actual_line_words[e + 1] in sect_num:
								sect_num[actual_line_words[e + 1]].add(str(line_num) + ',' +  str(e + 1))
							else:
								sect_num[actual_line_words[e + 1]] = set()
								sect_num[actual_line_words[e + 1]].add(str(line_num) + ',' + str(e + 1))
					e = e + 1
				if prev_act_name != "":
					case_dict[case_id][prev_act_name]["Section"] = sect_num

			
		text = ""
	# for case_id in case_dict:
	# 	for act in case_dict[case_id]:
	# 		case_dict[case_id][act]["Section"] = list(case_dict[case_id][act]["Section"])
	for case_id in case_dict:
		for act in case_dict[case_id]:
			case_dict[case_id][act]["Location"] = list(case_dict[case_id][act]["Location"])
			for section in case_dict[case_id][act]["Section"]:
				case_dict[case_id][act]["Section"][section] = list(case_dict[case_id][act]["Section"][section])
	# with open("section_act_mapping_from_case.json", "w") as write_file:
	# 	json.dump(case_dict, write_file, indent = 4)
	return case_dict



def fetch_all_acts_in_a_case(case_id):
	#act_cases = fetch_acts_from_cases(fetch_all_acts())
	#return act_cases[case_id]
	file = open("{}/All_FT/{}".format(ENV["DATASET_PATH"], case_id), 'r')
	nlp = spacy.load('en_core_web_sm')
	case_dict = {}
	all_acts = fetch_all_acts_from_txt()
	#file = open("./All_FT/2003_C_16.txt", 'r')
	text = ""
	line_num = 1
	#print(case_id)
	act_cases = set()
	prev_act_name = ""
	year = ""
	dada_act_name = ""
	acts_so_far = {}
	for line in file:
		for wrong in word_to_replace_dict:
			if wrong in line:
				line = line.replace(wrong, word_to_replace_dict[wrong])
		for pronoun in act_replacement:
			if pronoun in line:
				line = line.replace(pronoun, prev_act_name)
		actual_line = line
		line = re.sub(r"[-()\"#/'@;<>{}`+=~|!?]", '', line)
		text += line
		doc = nlp(text)
		line_words = line.split(" ")
		actual_line_words = actual_line.split(" ")
		for entity in doc.ents:
			act_bool = 0
			words = entity.text.split(" ")
			if "Act" in words or "Act," in words or "Act." in words:
				act_bool = 1
				if words[0] in BAD_WORDS_TYPE1:
					words = words[1:]
				year = ""
				ent_ind = line.index(entity.text)
				ent_ind = ent_ind + len(entity.text)
				while ent_ind < len(line):
					if line[ent_ind] >= '0' and line[ent_ind] <= '9':
						year += line[ent_ind]
					ent_ind += 1
				if len(year) != 4:
					year = ""

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

				dada_act_name = prev_act_name
				prev_act_name = act_name
				if year != "":
					prev_act_name = prev_act_name + " " + year
				parsed_by_spacy = prev_act_name

				# print("Yo, ", prev_act_name)
				if prev_act_name == "":
					continue
				if parsed_by_spacy in acts_so_far:
					prev_act_name = acts_so_far[parsed_by_spacy]
				else:
					possible = difflib.get_close_matches(prev_act_name, all_acts, 5)
					if len(possible) > 0:
						max_count = 0
						#print(possible)
						for i in range(len(possible)):
							match_count = 0
							bas = possible[i]
							w = possible[i].split(" ")
							for a in w:
								if a.lower() in [f.lower() for f in line_words]:
									match_count += 1
							if match_count >= max_count:
								max_count = match_count
								prev_act_name = possible[i]
						checker = prev_act_name.split(" ")
						if checker[0].lower() not in [v.lower() for v in line_words]:
							if dada_act_name != "":
								prev_act_name = dada_act_name
				# print(prev_act_name)
				if parsed_by_spacy not in acts_so_far:
					acts_so_far[parsed_by_spacy] = prev_act_name
				line_of_act = 0
				loc_of_act = 0
				line_of_act = line_num
				for each_word in prev_act_name.split(" "):
					if each_word in line_words:
						loc_of_act = line_words.index(each_word)

				
				if prev_act_name != "":
					act_cases.add(prev_act_name)
							
		text = ""
	# with open("acts_from_cases.json", "w") as write_file:
	# 	json.dump(act_cases, write_file, indent = 4)

	return act_cases

def closest_actual_act(act_str):
	all_acts = fetch_all_acts_from_txt()
	if len(difflib.get_close_matches(act_str, all_acts, 5)) > 0:
		possible = difflib.get_close_matches(act_str, all_acts, 5)
		max_count = 0
		act_str = possible[0]	
	return act_str

if __name__ == "__main__":
	print("################################################################")
	print("Hey There!")
	print("If you want act to case mapping in a json, press 1")
	print("If you want section to act to case mapping in a json, press 2")
	print("If you want all mappings in a given case , press 3 and enter case ID")
	act_case = fetch_mappings_of_given_case("1953_A_1.txt")
	choice = input()
	if choice == 1:
		act_to_case = fetch_acts_from_cases(fetch_all_acts())

	if choice == 2:
		sect_to_act_to_case = fetch_section_act_mapping_from_case(fetch_all_acts())

	if choice == 3:
		print("Enter Case ID:")
		particular_case = raw_input()
		all_cases_dict = fetch_section_act_mapping_from_case(fetch_all_acts())
		case_mappings = fetch_mappings_of_given_case(particular_case, all_cases_dict)
