my_file = open("day6.txt", "r")
  
# reading the file
tempFile = my_file.read()
fourChars = ""
k=14

def isUnique(word):
	for letter in word:
		if word.count(letter) > 1:
			return 0
	return 1

for entry in tempFile[k:]:
	fourChars = tempFile[k-14:k]
	if isUnique(fourChars) == 1:
		print(k)
		break
	k=k+1
	




my_file.close()
