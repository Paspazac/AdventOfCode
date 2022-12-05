my_file = open("day4.txt", "r")
  
# reading the file
data = my_file.read()
resultList=[]

data_into_list = data.split("\n")

sum=0

def CompareNumbers(x,y,a,b, tmpList):
	if (x<=a and b<=y):
		print("A " + str(tmpList))
		return 1
	elif (a<=x and y<=b):
		print("b " + str(tmpList))
		return 1
	elif (a>=x and y<=b and y>=a):
		print("c " + str(tmpList))
		return 1
	elif (a<=x and y>=b and b>=x):
		print("d " + str(tmpList))
		return 1
	return 0

def GetNumbers(value):
	newList=[]
	myList= value.split(",")
	for item in myList:
		newList.append(item.split("-"))
	x=int(newList[0][0])
	y=int(newList[0][1])
	a=int(newList[1][0])
	b=int(newList[1][1])
	return CompareNumbers(x,y,a,b, newList)
				

for entry in data_into_list[:-1:]:
	sum=sum+GetNumbers(entry)
# printing the data
print(sum)
my_file.close()
