#1
x =[] 
print (x)
#2
thich = ["da bong"]
print (thich)
#3
sothich =["da bong","co tuong","vainglory"]
print (sothich)
#4
sothich.append("an")
print (sothich)
#5
nhap = input("them so thich")
sothich.append(nhap)
print (sothich)
#6
print (*sothich)
#7
print (*sothich, sep = ",")
#8
print(*sothich, sep = "|")
#9
print (sothich[0],sothich[3],sothich[4])
#10
print (sothich[0].upper())
print (sothich[3].upper())
print (sothich[4].upper())
#11
sothich [0] = "co chu nha va ong tho sua ong nuoc"
print (sothich)
#12
sothich [4] = "toi thay hoa vang tren co xanh"
#13
sua = input("sua phan tu 0")
sothich [0] = sua
print (sothich)
#14
sothich.pop(1)
#15
if "lol" not in sothich:
    print ("phan tu lol khong ton tai")
else:
     sothich.remove("LOL")
#16
i = int(input ("xoa phan tu thu "))
sothich.pop(i)
print(sothich)
#17
loop =True
while loop:
    a = input("xoa phan tu ")
    if a not in sothich:
        print("khong co phan tu nay trong list") 
    else:
        sothich.remove(a)
        loop = False
print (sothich)
#18
sothich.extend(("da bong","ngu","code"))
print (sothich)
i=-1
for i in range (4):
    i+=1 
    print (sothich[i])
#19
i=-1
for i in range (4):
    i+=1 
    print (sothich[i].upper())
#20
i=-1
for i in range (4):
    i+=1 
    print (".  ",sothich[i].upper())
#21
a =-1
for i in range(4):
    i+=1
    if "e" in sothich[i] or "E" in sothich[i]:
        print(sothich[i].upper(),)
    else:
        print("",end="")
#22
guess_list = []
loop = True
while loop:
    guess_answer = input("Choose 1 in 4 options(C,R,U,D)")
    if guess_answer == "C":
        ask_c = input("what do you like to create")
        guess_list.append(ask_c)
        print (guess_list)
    if guess_answer == "R":
        if len(guess_list) ==0 :
            print ("your list is empty")
        else:
            print (guess_list[0])
    if guess_answer == "U":
        ask_where= int(input("where do you want to update"))
        ask_update = input("what do you want to update")
        guess_list[ask_where] = ask_update
        print (guess_list)
    if guess_answer == "D":
        ask_lo = int(input("where do you want to delete"))
        guess_list.pop(ask_lo)
        print (guess_list)
#23
ml = []
ml_ask =input("name your things")
ml.extend(ml_ask)
loop = True
while loop:
    if "," in ml:
        ml.remove(",")
    else:
        print (ml)
        a =len(ml)
        i=-1
        b = True
        while b:
            i+=1
            print(ml[i])
            if i == len(ml)-1:
                b = False
        loop = False
#24
from random import shuffle
s = input("enter a word: ")
l = list(s)
shuffle (l)
for i in range (len(l)):
    print (l[i].upper())

#25
from random import randint
from random import shuffle
danhsach=["hien","du","ba la sat","diem vuong","hien nhu tien","doc ac","khong co"]
i = randint(0,4)
chon = danhsach[i]
print (chon)
l = list(chon)
loop = True
while loop:
    if " " in l:
        l.remove(" ")
    else:
        shuffle (l)
        loop = False
print (*l,sep=",")
lap = True
while lap:
    doan = input("sap xep tu de biet bo mat that vo tl cua ban:")
    if doan ==chon:
        print ("ban da doan dung")
        lap = False
    if doan != chon:
        print ("sai roi, doan lai di")







    

    
    


