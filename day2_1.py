my_file = open("day2.txt", "r")
  
# reading the file
data = my_file.read()
resultList=[]

data_into_list = data.split("\n")
sum = 0



for entry in data_into_list:
	entry = entry.lower()
	if entry == "a x":
		sum = sum + 4
	elif entry == "a y":
		sum = sum + 8
	elif entry == "a z":
		sum = sum + 3
	elif entry == "b x":
		sum = sum + 1
	elif entry == "b y":
		sum = sum + 5
	elif entry == "b z":
		sum = sum + 9		
	elif entry == "c x":
		sum = sum + 7
	elif entry == "c y":
		sum = sum + 2
	elif entry == "c z":
		sum = sum + 6		
	else: print(entry)
# printing the data
print(sum)
my_file.close()
