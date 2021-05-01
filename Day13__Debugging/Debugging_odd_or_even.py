number = int(input("Wich number do you want to check? "))

if number % 2 == 0:  # the bug was with the = sign for compare number you have to use "=="
    print("This is an even number.")
else:
    print("This is an odd number.")
