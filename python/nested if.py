number = 33

if number % 6 == 0:
    print("Divisible by six")
else:
    if number % 2 == 0:
        print("Divisible by two")
    elif number % 3 == 0:
        print("Divisible by three")
    else:
        print("Divisible by none")