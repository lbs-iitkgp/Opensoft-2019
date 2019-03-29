import re
import json
import spacy
import string
import datetime
from scipy import spatial
from dateparser.search import search_dates

cosine_similarity = lambda x, y: 1 - spatial.distance.cosine(x, y)
depunctuate = lambda x: x.translate(str.maketrans('', '', string.punctuation))

################################################################################################
# Pipeline :- 

# Get query from user, Pass it through subject matcher to get subject matches
# pass it through dateparser to get dates,
# then tokenize and pass it through ES to get matches of judges, acts, case titles
################################################################################################

nlp = spacy.load('en_core_web_lg')
with open("nlp/topic/subjects_to_cases.json", 'r') as f:
	SUBJECTS_TO_CASE = json.load(f)

subjects = list(SUBJECTS_TO_CASE.keys())
SUBJECTS_TO_TOKENS = {}

for subject in subjects:
	if subject == '':
		continue
	tokens = []
	for word in subject.split(" "):
		if depunctuate(word).lower() == '':
			continue
		tokens.append(depunctuate(word).lower())
	SUBJECTS_TO_TOKENS[subject] = tokens

subject_tokens =  {}
nlp.Defaults.stop_words |= {"judge","cases","case",}

for i, tokens in SUBJECTS_TO_TOKENS.items():
	token_sum = 0
	for token in tokens:
		token_sum += nlp.vocab[token].vector
	subject_tokens[i] = token_sum

def get_subject_matches(query, top=5):
	query = nlp(query)
	cleaned_query_tokens = []
	for token in query:
		if token.ent_type_ == "DATE" or token.text in nlp.Defaults.stop_words or token.ent_type_ == "PERSON":
			continue
		cleaned_query_tokens.append(token.text.lower())
	matches = []
	query_token_sum = 0
	for token in cleaned_query_tokens:
		query_token_sum += nlp.vocab[token].vector

	for subject, vector in subject_tokens.items():
		similarity = cosine_similarity(query_token_sum, vector)
		if similarity > 0.3:
			matches.append((subject, similarity))

	matches = sorted(matches, key=lambda k: k[1], reverse=True)
	return matches[:top]

def get_date_parser(query):
	query = nlp(query)
	dates = []
	index = 0
	while index != len(query):
		date, ind = get_next(query[index], [], query, index)
		index = ind
		# print(date)
		if date != []:
			dates.append(date)
	return dates

def get_next(next, current, query, index):
	# print(next.text)
	if next.ent_type_ != "DATE":
		return current, index+1
	else:
		try:
			current.append(next.text)
			return get_next(query[index+1], current, query, index+1)
		except IndexError:
			return current, index+1

def get_years(query):
	re_year = r'[0-9]{4}'
	years = re.findall(re_year, query)
	return sorted(list(map(lambda x: int(x), years)))


def search_years(query):
	re_year = r'[0-9]{4}'
	parsed_query = search_dates(query)

	if parsed_query is None:
		return get_years(query)

	if len(parsed_query) < 2:
		return sorted([v.year for i,v in parsed_query])
	definite = 0
	relative = 0
	try:
		for text, date in parsed_query:
			print(text, date)
			matches = re.findall(re_year, text)
			try:
				if matches[0] == text:
					definite = date
			except IndexError:
				relative = date
		now = datetime.datetime.now()
		relative = relative - (now - definite)
		return sorted([relative.year,definite.year])
	except Exception as e:
		print(e)
		return get_years(query)

if __name__ == '__main__':


	example_sentences = [
		'cases of murder handled by Chandrauchad of last 10 years from 2018',
		'environmental and criminal cases of 2004',
		'service tax handled by judge Vaidya',
		'health related cases between 2003 and 2008'
		]

	for i in example_sentences:
		print(get_subject_matches(i))
		print(search_years(i))
