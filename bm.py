

def bm():
	
	question = open("ask_indo.txt","r")
	answer = open("ans_indo.txt","r")
	stopword = open("stopword.txt","r")
	pertanyaan = []
	jawaban = []
	sw = []
	for s in stopword:
		sw.append(s.rstrip())
	for s in question:
		pertanyaan.append(s.rstrip())
	for s in answer:
		jawaban.append(s.rstrip())
	query = input()
	query = query.replace("?","")
	query = query.split()
	qtemp = query.copy()

	for q in (query):
		# print(q)
		for s in (sw):
			if(q == s):
				qtemp.remove(q)
				break
	print(qtemp)
	confindence = 0
	c = 0
	found = False
	# array tuple (index,confindence)
	suggestion = [(-1,-1),(-1,-1),(-1,-1)]

	for s in pertanyaan:				
		confindence = boyermoore(qtemp,s)
		if(confindence > 90):
			found = True
			break
		else :
			for i in range(3):
				if(suggestion[i][1] < confindence):
					suggestion[i][0] = c
					suggestion[i][1] = confindence
					break

	if (found):
		print (answer[c])
		print ("with confindence",confindence)
	else :
		for s in suggestion:
			if(s >= 0):
				print (answer[s])
bm()