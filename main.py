import bm
import kmp
import regex

def main():
	print("Main program")
	print("Pilihan input pencarian")
	print("1. kmp")
	print("2. bm")
	print("3. regex")
	x = int(input())
	if(x==1):
		kmp.kmp()
	elif(x==2):
		bm.bm()
	elif(x==3):
		regex.regex()

main()
