'''
stdNames = ['abc', 'xyz', 'pqr']
print(stdNames)

# adding a element in list
stdNames.append('fgh')
print(stdNames)

# Acessing a element
print(stdNames[2])


# Searching a element

if 'x' in stdNames:
    print('Fount it')
else:
    print('Not found')
    
    
# CHanging a value

stdNames[1] = 456
print(stdNames)

# inseting a value
stdNames.insert(3, 'std')
print(stdNames)

#Removing a element
stdNames.remove('abc')
print(stdNames)


#task for now: print your list in reverse order
# append 6 different items in list using for loop

# task 1:
print(stdNames[::-1])

#task2

list = []

for i in range(6):
    list.append(i)
    
print(list)


list2 = []

for i in range(6):
    user = input()
    list2.append(user)
    
print(list2)
'''

# LIst comprehension

myList = []

for i in range(1,11):
    if i%2==0:
        myList.append(i)
        
print(myList)


myList1 = [x for x in range(1,11) if i%2==0]
myList1

#Make a list of any elemets(eg: fruits) and store only those elemets in 
# new list which consist "a" letter in it.

#Hint: 1. Make a list in which you have to use first for loop and then use if 
# statement to check "a" letter in it.


#Saturday task

user = input('Enter your name: ')
print(user +" "+  "Welcome here!!")
list = []
n = int(input('Please enter number of students: '))

for i in range(n):
    name = input("Enter student name: ")
    Age = input('Enter student age: ')
    list.append("student name is "+ " " + name + 'and age is '+ " " + Age)
    
print(list)






    
    
    
    
    
    
    






































