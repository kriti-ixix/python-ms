print("Welcome to the note taking app!")
filename = input("Enter the file name: ") + ".txt"
choice = int(input("Choose an option: 1. Read 2. Write 3. Append\n"))

if choice == 1:
    #Reading the file
    try:
        noteFile = open(filename, 'r')
        print(noteFile.read())
        noteFile.close()
    except:
        print("File does not exist")

elif choice == 2:
    #Writing to the file
    noteFile = open(filename, 'w')
    number = int(input("How many notes do you want to write? "))

    for n in range(number):
        noteFile.write(input("Enter note: ") + "\n")

    noteFile.close()

elif choice == 3:
    #Appending to the file
    noteFile = open(filename, 'a')
    number = int(input("How many notes do you want to append? "))

    for n in range(number):
        noteFile.write(input("Enter note: ") + "\n")

    noteFile.close()

else:
    print("Invalid input")