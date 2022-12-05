my_file = open("day3.txt", "r")
  
# reading the file
data = my_file.read()
resultList=[]

data_into_list = data.split("\n")

sum=0



def CompareString(s1,s2):
	for i in s1:
		if i in s2:
			if i.islower()==1:
				print(i)
				return ord(i)-96
			return ord(i)-38
	return 0		
				
def splitstring(value):
    s1, s2 = value[:len(value)//2], value[len(value)//2:]
    return CompareString(s1,s2)	
		

for entry in data_into_list:
	sum=sum+splitstring(entry)

# printing the data
print(sum)
my_file.close()
