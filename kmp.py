def readfile(array, namafile):
    f = open(namafile, "r")
    f1 = f.readlines()
    i = 0
    for x in f1:
        array[i] = x.rstrip()
        i += 1
        
def inputdatabase(ask, ans, stop):
    readfile(ask, "ask_data.txt")
    readfile(ans, "ans.txt")
    readfile(stop, "stopword.txt")
    readfile(daftar, "ask.txt")
    readfile(synonim, "synonim.txt")
    
    
# Python program for KMP Algorithm 
def KMPSearch(pat, txt): 
    m = len(pat) 
    n = len(txt) 
  
    b = [0]*m 
    
    computerFail(pat, b, m) 
  
    i = 0 
    j = 0
    while i < n: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
        else:
        	if j!=0 :
        		j = b[j-1]
        	else:
        		i += 1
                
        if j == m: 
            return 1 
            j = b[j-1]
    return 0
  
def computerFail(pat, b, m): 
    len = 0 
  
    b[0] = 0
    i = 1
    while i < m: 
        if pat[i]== pat[len]: 
            len += 1
            b[i] = len
            i += 1
        else: 
            if len != 0: 
                len = b[len-1] 
            else: 
                b[i] = 0
                i += 1


def kmp(pattern):
    inputdatabase(ask, ans, stop)
    pattern = pattern.translate({ord(i): None for i in '?!.,'}) #hapus tanda baca
    pattern = pattern.rstrip()
    pattern = pattern.lower()
    kata = pattern.split(" ")

    #hapus stopword dari input
    for x in kata[:]:
        for y in stop:
            if x == y :
                kata.remove(x)
                break
    
    #cari pertanyaan yang cocok     
    max1 = 0.0
    max2 = 0.0
    max3 = 0.0
    indeks1 = -1
    indeks2 = -1
    indeks3 = -1
    for x in ask:
        le = len(x) - x.count(" ")
        bag = 0
        for y in kata:
            if(KMPSearch(y, x)):
                bag += len(y)
            else:
                for j in synonim:
                    word = j.split(" ")
                    if(KMPSearch(y, j)) and (KMPSearch(word[0], x)):
                        bag += len(word[0])

        #biar bisa ngasih sugestion
        if (bag/le) > max1:
            max3 = max2
            max2 = max1
            max1 = bag/le
            indeks1 = ask.index(x)
        elif (bag/le) > max2:
            max3 = max2
            max2 = bag/le
            indeks2 = ask.index(x)
        elif (bag/le) > max3:
            max3 = bag/le
            indeks3 = ask.index(x)
            
    if max1>0.9:
        print("Confident score : " + str(int(max1*100)) + "%")
        print(ans[indeks1])
    else :
        print("Petanyaan Anda tidak memenuhi confident level yang telah ditentukan")
        print("Terdapat beberapa sugesti pertanyaan yang mungkin")
        c = 0
        if(indeks1 != -1):
            print(str(c)+" " + daftar[indeks1])
            c += 1
        if(indeks2 != -1):
            print(str(c)+ " " + daftar[indeks2])
            c += 1
        if(indeks3 != -1):
            print(str(c)+" " + daftar[indeks3])
            c += 1
        if(c==0):
            print("Saya tidak mengerti maksud anda")
        print("Tuliskan kembali pertanyaan yang menurut Anda paling cocok")
        
  
ask = ["" for x in range(63)]
ans = ["" for x in range(63)]
daftar = ["" for x in range(63)]
synonim = ["" for x in range(27)]
stop = ["" for x in range(758)]