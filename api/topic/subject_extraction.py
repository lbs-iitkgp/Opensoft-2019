from scipy import spatial
import spacy
import json
import string

cosine_similarity = lambda x, y: 1 - spatial.distance.cosine(x, y)
depunctuate = lambda x: x.translate(str.maketrans('', '', string.punctuation))

def get_subject_matches(query, top=5):
	query = nlp(query)
	cleaned_query_tokens = []
	for token in query:
		if token.ent_type_ == "DATE" or token.text in nlp.Defaults.stop_words or token.ent_type_ == "PERSON":
			continue
		cleaned_query_tokens.append(token.text.lower())

	# print("Cleaned :- ", cleaned_query_tokens)
	matches = []
	query_token_sum = 0
	for token in cleaned_query_tokens:
		query_token_sum += nlp.vocab[token].vector

	for subject, vector in subject_tokens.items():
		similarity = cosine_similarity(query_token_sum, vector)
		if similarity > 0.6:
			matches.append((subject, similarity))

	matches = sorted(matches, key=lambda k: k[1], reverse=True)
	# print(matches[:5])
	# print()
	return matches[:top]


if __name__ == '__main__':
	nlp = spacy.load('en_core_web_lg')
	# print("model loaded")
	with open("subjects_to_cases.json", 'r') as f:
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


	example_sentences = [
		'cases of murder handled by Chandrauchad of last 10 years',
		'environmental and criminal cases of 2004',
		'service tax handled by judge Vaidya'
		]

	subject_tokens =  {}
	nlp.Defaults.stop_words |= {"judge","cases","case",}

	for i, tokens in SUBJECTS_TO_TOKENS.items():
		token_sum = 0
		for token in tokens:
			token_sum += nlp.vocab[token].vector
		subject_tokens[i] = token_sum