import PyPDF2 
import re 
from nltk import word_tokenize
import json
import os
import math
from collections import Counter
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
from nltk import word_tokenize
import numpy as np
from scipy import spatial
from nltk.corpus import stopwords

stop_words = stopwords.words('english')


model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin',binary = True,limit=50000)
print("server:model loaded!")
model_words = list(model.wv.vocab)


tfidf = {}

sent_list = []
doc_dict = {}

def givepdfcontents(filename):
	try:
		file = open(filename, "r")
		pdf_contents = file.read()

	except:
		pdf_contents = ""
	return pdf_contents



def idf():
    idf = {}

    files = []
    for filename in os.listdir('All_FT'):
            if filename[-4:] == '.txt':
            	files.append(filename)

    print(len(files))
    progress = 0
    #for fil in files:
    #	print(fil)

    for fil in files:
        pdf_contents=givepdfcontents(fil)
        terms = list(set(word_tokenize(pdf_contents)))
        non_repeated_lowercase = []
        for term in terms:
            non_repeated_lowercase.append(term.lower())
        
        non_repeated_lowercase = list(set(non_repeated_lowercase))

        progress +=1
        for term in non_repeated_lowercase:
            
            try:
                idf[term] +=1
                # print(idf[term])
            except:
                idf[term] = 1
        print(str(progress) + "/" + str(len(files)) + " Done")


    for key,value in idf.items():

        idf[key] = math.log(len(files)/idf[key])

    print(len(files))

    jsonFile = open("idf.json", "w")
    jsonFile.write(json.dumps(idf,sort_keys=True,indent=4))
    jsonFile.close()



def tf_idf(pdf_contents):
	jsonFile = open("idf.json", "r")
	idf_values = json.load(jsonFile)
	jsonFile.close()
	pdf_contents = (pdf_contents.lower()).replace(':'," ").replace('"',' ')
	terms = pdf_contents.replace('/',' ').replace(';',' ').split()
	no_of_terms = len(terms)
	tf = Counter(terms)
	for key in tf:
		tf[key] /=no_of_terms
		idf_val = 0
		try:
			idf_val = idf_values[key]
		except:
			print(key)
			idf_val = 0
		tfidf[key] = tf[key] * idf_val
	print("")
	print(tfidf)




def sent2vector(text):
    x = np.array([0]*300)
    tf_idf(text)
    count = 0
    for words in word_tokenize(text):
        if words in model_words and words not in stop_words:
            temp = model[words];
            try:
                temp = temp*tfidf[words]
            except:
                temp = temp*1
            x = x + temp
            count = count + 1
            print(words)
    if(count>0):
        x = x/count
    return x


def cos_similarity(content):
    current_score = -10
    result = ""
    temp_quer_vec = sent2vector(content)
    for key,value in doc_dict.items():
        if not np.any(value):
            continue
        score = 1 - spatial.distance.cosine(temp_quer_vec, value)
        print(score)
        if(score > current_score):
            current_score = score
            result = key
    print(result)


"""file = open("1953_A_1.txt", "r")
a = file.read()
print(a)
while(a):
    print(a)
    sent_list.append(a)
    a = file.readline()"""
    

for i in  range(0,5):
    print(i)
    file = open("1953_A_"+str(i+1)+".txt", "r")
    a = file.read()
    sent_list.append(a)

for text in sent_list:
    doc_dict[text] = sent2vector(text)




cos_similarity("Raja Prafulla Nath Tagore, a Hindu governed by the Dayabhaga School of Hindu Law, died on 2-7-1938, leaving him surviving his widow and five sons. Kumar Purnendu Nath Tagore, the appellant, is his eldest son. On 14-3-1927, the late Raja executed his last will and testament. Cl. 82 of the will is in these terms")



"""
if __name__ == '__main__':
    pdf_contents = givepdfcontents("1953_A_1.txt")
    tf_idf(pdf_contents)"""