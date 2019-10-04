#!/usr/bin/Python3

import zipfile
from threading import Thread

def extract(file, password):
	
	try:
		file.extractall(path=None, members=None, pwd=password)
		print("[+] Zip file extracted. \nPassword = "+ str(password).strip("b'"))
		exit()

	except RuntimeError:
		pass
		#print("Trying password: "+ str(password).strip("b'"))
		

def main():
	
	file = zipfile.ZipFile("test.zip")

	f = open("wordlist.txt", "r")
	for i in f.readlines():
		password = (i.strip()).encode()
		#print(password)

		t = Thread(target=extract, args=(file, password))
		t.start()
		#extract(file, password)
	

		
		

if __name__ == '__main__':
	main()
