import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("guess the number"))
    if user == number:
        print("Hurray!!")
        print("you guessed the number right it's {number}".format())
        break
    elif user != number:
        print(" reenter")
if user != number:
    print("Your guess is incorrect the number is {number}".format())
