try:
    #Normal execution of the program
    myList = [1, 2, 3, 4, 5]
    print(myList[1])
    print(myList[10])

except IndexError:
    print("Index does not exist")

except KeyError:
    print("Key does not exist")

except:
    #In case any error occurs
    print("Error")
