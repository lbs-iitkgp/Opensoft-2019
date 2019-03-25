from scipy import spatial
import spacy
import json
import string

cosine_similarity = lambda x, y: 1 - spatial.distance.cosine(x, y)
depunctuate = lambda x: x.translate(str.maketrans('', '', string.punctuation))

nlp = spacy.load('en_core_web_lg')

print("model loaded")
with open("subjects_to_cases.json", 'r') as f:
	SUBJECTS_TO_CASE = json.load(f)

subjects = list(SUBJECTS_TO_CASE.keys())

SUBJECTS_TO_TOKENS = {}

for subject in subjects:
	tokens = []
	for word in subject.split(" "):
		if depunctuate(word).lower() == '':
			continue
		tokens.append(depunctuate(word).lower())
	SUBJECTS_TO_TOKENS[subject] = tokens


example_sentences = [
'cases of murder handled by chandrauchad of last 10 years',
'environmental and criminal cases of 2004',
'service tax handled by judge vaidya'
]



for query in example_sentences:
	query = nlp(query)
	cleaned_query_tokens = []
	for token in query:
		if token.ent_type_ == "DATE" or nlp.vocab[token.text].is_stop:
			continue
		cleaned_query_tokens.append(token.text.lower())

	print("Cleaned :- ", cleaned_query_tokens)

	matches = []

	## need to improve the logic of this part
	for token in cleaned_query_tokens:
		for subject, sub_tokens in SUBJECTS_TO_TOKENS.items():
			sub_match_count = 0
			for sub_token in sub_tokens:
				sub_token_vector = nlp.vocab[sub_token].vector
				query_token_vector = nlp.vocab[token].vector
				similarity = cosine_similarity(query_token_vector, sub_token_vector)
				if similarity > 0.7:
					sub_match_count += 1
					# matches.add(subject)
			matches.append((subject, sub_match_count))   
	matches = sorted(matches, key=lambda k: k[1], reverse=True)[:4] 
	print(matches)
	print()

# for i in subjects:
# 	for word in i.split(" "):
# 		word = depunctuate(word)
# 		if nlp.vocab[word.lower()].vector.all() == 0:
# 			print(word)
