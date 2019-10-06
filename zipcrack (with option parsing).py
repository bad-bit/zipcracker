import zipfile
import optparse
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
	

	parser = optparse.OptionParser("Usage - zipcrack.py "+"-f <zipfile> -d <dictionary>")
	parser.add_option('-f', dest='zname', type='string', help="Specify zip file")
	parser.add_option('-d', dest='dname', type='string', help="Specify dictionary file")

	(options, args) = parser.parse_args()

	if (options.zname == None) | (options.dname == None):
		print(parser.usage)
		exit(0)
	else:
		zname = options.zname
		dname = options.dname

	file = zipfile.ZipFile(zname)

	f = open(dname, "r")
	for i in f.readlines():
		password = (i.strip()).encode()
		#print(password)

		t = Thread(target=extract, args=(file, password))
		t.start()
		#extract(file, password)
	

		
		

if __name__ == '__main__':
	main()