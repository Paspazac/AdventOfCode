my_file = open("day3.txt", "r")
  
# reading the file
tmpFile = my_file.read()
resultList=[]

data = tmpFile.split("\n")

sum=0

    

def compareString(s1, s2, s3):
	for i in s1:
		if i in s2:
			if i in s3:
				if i.islower()==1:
					return ord(i)-96
				return ord(i)-38
	return 0		
		

for entry in data[::3]: 
	print(data.index(entry))
	if data.index(entry) +1== len(data):
		break
	sum = sum + compareString(entry, data[data.index(entry)+1], data[data.index(entry) + 2])

# printing the data
print(sum)
my_file.close()
