from random import randint
print ("chon so tu nhien tu 0 den 100")
guest_number = int(input("nhap so cua ban: ")) 
i=0
loop = True
a=50
computer_number= randint(0,100)
while loop:
    i+=1
    if computer_number == guest_number:
        print ("may tinh doan la: ",computer_number) 
        print ("may da doan dung")
        loop = False
    elif computer_number < guest_number:
        print ("may tinh doan la: ",computer_number)
        print ("so ban lon hon") 
        computer_number = randint(a,100)
    else:
        print ("may tinh doan la: ",computer_number) 
        print ("so ban be hon ")
        computer_number = randint (0,a)
    if i>8:
        print("may tinh da het luot doan\nGame over\nban thang")
        loop = False
