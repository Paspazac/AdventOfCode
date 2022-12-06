my_file = open("day5.txt", "r")
  
# reading the file
tempFile = my_file.read()

data = tempFile.split("\n")

crates=[]
spot=1000
def makeListOfList(creates):
	return list(map(lambda el:[el.strip()], creates))


def popCrates(crates, spot, data):
	for item in crates:
		tmpItem = item[0]
		tmpVar = data[spot-1].find(tmpItem)
		for entry in data[spot-2::-1]:
			if entry[tmpVar] > ' ':
				item.append(entry[tmpVar])
		
def moveItems(entry, crates):
	tmpList = entry.split(" ")
	amount = int(tmpList[1])
	ffrom = int(tmpList[3]) - 1
	to = int(tmpList[5]) - 1
	l1 = crates[ffrom][-amount:]
	print(tmpList[1] + " " +tmpList[3] + " "+tmpList[5]) 
	del crates[ffrom][-amount:]
	crates[to]=crates[to]+l1
	
	
for entry in data[:-1]:
	if entry=='':
		spot=data.index(entry)
		crates=data[spot-1].split("   ")
		crates = makeListOfList(crates)
		popCrates(crates, spot, data)
		print(crates)
	elif data.index(entry) > spot:
		moveItems(entry, crates)
print("last:")
print(crates)

for entry in crates:
	print(entry[-1])


# printing the data

my_file.close()
