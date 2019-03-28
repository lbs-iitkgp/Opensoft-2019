import spacy
import json 

nlp = spacy.load('en_core_web_lg')
with open("name.json", 'r') as f:
	judges = json.load(f)

def remove_words(name):
	existing = [i for i in name.splits(' ')]
	new_name = []
	for i in existing:
		if nlp.vocab[i].vector.all() == False:
			continue
		new_name.append(i)
	return ' '.join(new_name)


sanit_judges = []
for index, judge in judges:
	print(index)
	new_judge = remove_words(judge)
	print(new_judge)
	sanit_judges.append(new_judge)

with open('sanit_judges.json', 'w') as f:
	json.dump(sanit_judges, f)