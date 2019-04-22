import bm
import kmp
import regex
import sys

def main(query):
	
	x = int(sys.argv[1])
	if(x==1):
		kmp.kmp(sys.argv[2])
	elif(x==2):
		bm.bm(sys.argv[2])
	elif(x==3):
		regex.regex(sys.argv[2])

main(sys.argv[1])
