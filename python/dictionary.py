myDict = {'name':'ABC', 'rollno':35, 0:100, 'pass':True}

#Getting the values 
print(myDict['name'])
print(myDict[0])

#Overwriting
myDict['pass'] = 100
print(myDict)

#Adding a new key to the dictionary
myDict['gender'] = 'female'
print(myDict)

studentInfo = {}
keys = ['name', 'rollno', 'gender', 'marks']

for k in keys:
    studentInfo[k] = input("Enter the value: ")

print(studentInfo)

for x in myDict:
    print(x)

print(myDict.keys())
print(myDict.values())
print(myDict.items())

for x in myDict.items():
    print(x)

#Dictionary unpacking
for (x, y) in myDict.items():
    print("Key:", x, "Value:", y)