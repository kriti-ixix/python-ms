'''
Every loop needs three things:
1. Iterator
2, Condition
3. Increment or decrement 
'''

i = 1

while i < 11:
    print(i)
    i += 1 #i = i + 1

#range(start=0, stop, step=1)
for i in range(1, 11):
    print(i)


myString = "Hello how are you"

for i in myString:
    print(i)