import hashlib

flag = 0

in_hash = input("Enter md5 hash: ")

wordlist = input("File name: ")

try:
	in_file = open(wordlist, "r")
except:
	print("No File")
	quit()

for word in in_file:
	enco_word = pass.encode('utf-8')
	final = hashlib.md5(enco_word.strip()).hexdigest()
	
	if final == in_hash:
		print("Password found")
		print("PASSWORD FOUND. PASSWORD CONCLUDED TO BE " + pass)
		flag = 1
		break

if flag == 0:
	print("PASSWORD NOT FOUND NOT IN LIST")