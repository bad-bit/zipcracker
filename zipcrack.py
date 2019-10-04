#!/usr/bin/Python3

import zipfile
from threading import Thread

#function to brute force zip file with the provided dictionary
def extract(file, password):
	
	try:
		file.extractall(path=None, members=None, pwd=password)
		print("[+] Zip file extracted. \nPassword = "+ str(password).strip("b'"))
		exit()

	except RuntimeError:
		pass
		#print("Trying password: "+ str(password).strip("b'"))
		

def main():
	
	#open zipfile
	file = zipfile.ZipFile("test.zip")

	f = open("wordlist.txt", "r")
	for i in f.readlines():
		password = (i.strip()).encode()
		#encoding because "extractall" method only takes byte like object and not string
		#print(password)
		
		#thread execution
		t = Thread(target=extract, args=(file, password))
		t.start()
		#extract(file, password)
		

if __name__ == '__main__':
	main()
