from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

def cekRegex(query,ask):
	kata = len(query)
	c = 0
	for q in query:
		#print(q)
		if (re.search(r'%s' % (q), ask,re.IGNORECASE)):
			c += 1
	return (c == kata)

def regex():
	factory = StemmerFactory()
	stemmer = factory.create_stemmer()
	question = open("ask_indo.txt","r")
	answer = open("ans_indo.txt","r")
	stopword = open("stopword.txt","r")
	sw = []
	pertanyaan = []
	jawaban = []
	for s in stopword:
		sw.append(s.rstrip())
	for s in question:
		pertanyaan.append(s.rstrip())
	for s in answer:
		jawaban.append(s.rstrip())

	query = input()
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
		if (cekRegex(qtemp,s)):
			found = True
			#print("hore")
			break
		else :
			#print("ga ketemu")
			c += 1
	#print(c)
	if (found):
		print(jawaban[c])	

regex()