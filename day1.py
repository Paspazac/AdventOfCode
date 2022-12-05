# opening the file in read mode
my_file = open("day1.txt", "r")
  
# reading the file
data = my_file.read()
tmp = 0
maxRes = 0
resultList=[]
# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.split("\n")
for entry in data_into_list:
	if entry == '':
		resultList.append(tmp)
		tmp = 0
	else: 
		tmp += int(entry)

resultList=sorted(resultList, reverse=True)
# printing the data
print(sum(resultList[:3]))
my_file.close()

        	
        	
