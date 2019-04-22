from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

factory = StemmerFactory()
stemmer = factory.create_stemmer()
question = open("ask_data.txt","r")
answer = open("ans.txt","r")
stopword = open("stopword.txt","r")
synonimfile = open("synonim.txt","r")
sw = []
pertanyaan = []
jawaban = []
synonim = []
for s in stopword:
	sw.append(s.rstrip())
for s in question:
	pertanyaan.append(s.rstrip())
for s in answer:
	jawaban.append(s.rstrip())
for s in synonimfile:
	synonim.append(s.rstrip())



def cekRegex(query,ask):
	kata = len(query)
	c = 0
	for q in query:
		#print(q)
		if (re.search(r'%s' % (q), ask,re.IGNORECASE)):
			c += 1
		else :
			for sy in synonim:
				if (re.search(r'%s' % (q), sy,re.IGNORECASE)):
					word = sy.split()
					for w in word:
						#print(w)
						
						if (re.search(r'%s' % (stemmer.stem(w)), ask,re.IGNORECASE)):
							c += 1
							break
					break
	return (c == kata)

def regex(query):
	query.replace("?","")
	query = stemmer.stem(query)
	query = query.split()
	qtemp = query.copy()
	

	for q in (query):
		# print(q)
		for s in (sw):
			if(q == s):
				qtemp.remove(q)
				break

	#print (qtemp)
	c = 0
	found = False
	#print(pertanyaan)
	for s in pertanyaan:
		#print(s)
		if (cekRegex(qtemp,stemmer.stem(s))):
			found = True
			#print("hore")
			break
		else :
			#print("ga ketemu")
			c += 1
	#print(c)
	if (found):
		print(jawaban[c])	
	else :
		print("Saya tidak mengerti maksud anda")
		print("Tuliskan kembali pertanyaan yang menurut Anda paling cocok")		
