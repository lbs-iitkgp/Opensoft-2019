from __future__ import unicode_literals
import os
import json
all_central_acts = os.listdir("./Acts/Central_Text")
 
# This function returns all the sections in a given act. The input has 
# to be the path of the act file.
def get_sections_in_act(act_path):
	file = open(act_path)
	all_sections = []
	for line in file:
		sect_num = ""
		if "Section" in line:
			ind = line.index("Section")
			ind = ind + 8
			while(line[ind] != "-"):
				sect_num += line[ind]
				ind += 1;
				if ind > len(line):
					break
			all_sections.append(sect_num)
	return all_sections
# This functions returns the text in the section of a given act.
# The input has to be path of the act file and section number.
def get_text_in_section(act_path, section_num):
	sect_num = "Section "
	number = ""
	for i in range(len(section_num)):
		if not (section_num[i] >= '0' and section_num[i] <= '9'):
			break
		number += section_num[i]
	sect_num += number

	file = open(act_path)
	for line in file:
		if sect_num in line:
			return line
# Sample usage of the functions.
# sect_list = get_sections_in_act("/home/manjunath/Downloads/OpenSoft-Data/Acts/State_Text/gujrat/8_1.txt")
# line = get_text_in_section("/home/manjunath/Downloads/OpenSoft-Data/Acts/State_Text/gujrat/8_1.txt","10(")
# print(sect_list)
# print("*********")
# print(line)