#Opening the file
#open(filename, mode)
'''
Three modes:
- read: Reads the file
- write: Create a new file / overwrite an existing file
- append: Adds the content to a file
- r+: Read & Write 
'''
studentFile = open('information.txt', 'w')

#Making any changes to the file
studentList = [1, "ABC", "Python", 45]

for x in studentList:
    studentFile.write(str(x) + "\n")

#Closing the file
studentFile.close()

studentFile = open('information.txt', 'r')

#Reading file line by line
for line in studentFile:
    print(line)

#print(studentFile.read()) #Reads the entire file in one go
studentFile.close()

with open('information.txt', 'r') as studentFile:
    print(studentFile.read())