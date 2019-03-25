import re
import sys,traceback
import json

with open("subject_keywords.txt") as f:
	content = f.readlines()

subjects = set()
catchwords = set()

SUBJECTS_TO_CASE = {}
CATCHWORDS_TO_CASE = {}

for index,case in enumerate(content):
	try:
		poten = case.split("-->")[2].strip()
		try:
			poten_subj = poten.split("$$$")[0]
			for subs in poten_subj.split(";"):
				san_sub = subs.strip().replace("\n",'')
				subjects.add(san_sub)
				try:
					SUBJECTS_TO_CASE[san_sub].append(case.split("-->")[0].strip())
				except KeyError:
					SUBJECTS_TO_CASE[san_sub] = [case.split("-->")[0].strip()]
		except Exception:
			pass

		try:
			poten_catch = poten.split("$$$")[1]
			for cats in poten_catch.split(","):
				san_cat = cats.strip().replace("\n",'')
				if san_cat in [""," "]:
					continue
				catchwords.add(san_cat)
				try:
					CATCHWORDS_TO_CASE[san_cat].append(case.split("-->")[0].strip())
				except KeyError:
					CATCHWORDS_TO_CASE[san_cat] = [case.split("-->")[0].strip()]
		except Exception as e:
			print("imp", index, case)
			print(poten_catch)
			exc_type, exc_value, exc_traceback = sys.exc_info()
			traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
			
	except Exception as e:
		print(e)
		print(index, case)
		continue

with open("subjects_to_cases.json", 'w') as f:
	json.dump(SUBJECTS_TO_CASE, f)

with open("catchwords_to_cases.json", 'w') as f:
	json.dump(CATCHWORDS_TO_CASE, f)