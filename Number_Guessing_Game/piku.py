def guess():
    import random
    a = random.randint(1, 100)
    while True:
        b = input("What is your guess?" + "\n")
        if int(a) < int(b):
            print("Your number was too high, try again.." + "\n")
        elif int(a) > int(b):
            print("Your number was too low, try again.." + "\n")
        elif int(a) == int(b):
            print("Correct! Nice job.")
guess()
