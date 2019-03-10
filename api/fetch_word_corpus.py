import os
directory = '/home/vinay/Documents/OpenSoft-Data/CaseDocuments/All_FT'
BLOCK_CHARS=list('''.()"',-:;''')
di = dict()
for filename in os.listdir(directory):
	if filename.endswith(".txt"):
		with open("CaseDocuments/All_FT/"+filename) as f:
			print(filename)
			c=0
			for line in f.readlines():
				for char in BLOCK_CHARS:
					line=line.replace(char,' ')
				line=line.lower()
				wds=line.split()
				for w in wds:
					w=w.strip()
					if(len(w)>3):
						if w in di:
							di[w]=di[w]+1
						else:
							di[w]=1
							c=c+1
		f.close()
		continue
for key, value in sorted(di.items(), key=lambda k : k[1], reverse=True):
	print("%s: %s" % (key, value))
print('Total new words = ')
#				print(c)
f1.close()