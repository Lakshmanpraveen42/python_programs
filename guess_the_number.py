from random import randint

print("guess the number that number lies between 0 to 10 ") 
random_num = randint(0,10)
##print(random_num)

x=-1
while x != random_num:
    if x != -1:
        print("Your guess is incorrect the number is ")

    x = input("enter the number : ")
    x= int(x)
print("Your guess is correct the number is")
