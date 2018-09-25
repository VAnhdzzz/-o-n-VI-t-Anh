from random import randint
loop = True
i=0
while loop:
    x= randint(0,100)
    y= randint (0,100)
    print (x,"+",y,"=")
    guess_number = int(input("answer:"))
    if x+y == guess_number:
        print ("True")
        i+=1
    if x+y != guess_number:
        print ("False, you lose")
        loop = False
    if i == 2:
        print("you win")
        loop = False