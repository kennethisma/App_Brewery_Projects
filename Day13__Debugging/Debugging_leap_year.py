year = int(input("Wich year do you want to check? "))


if year % 4 == 0:  # The bug was that year wasn't a int it was a string
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")
