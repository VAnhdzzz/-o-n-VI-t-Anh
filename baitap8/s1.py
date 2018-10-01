mau = ["yellow","red","green"]
print ("our color list",mau)
nhap = input("nhap them mau")
mau.append(nhap)
print (mau)
loop = True
vitri = int(input ("xem vi tri"))
if vitri>3:
    print("sai") 
    vitri = int(input ("xem vi tri"))
print (mau[vitri-1])
hoi = (input("nhap so hay nhap chu :"))\

if hoi == "chu":
    nhapchu = input ("xoa cai gi")
    mau.remove(nhapchu)
if hoi == "so":
    nhapso = int(input("xoa cai gi"))
    if nhapso > 2:
        print("doan xem")
        nhapso = int(input("xoa cai gi"))
    mau.pop(nhapso)
print (mau)
#6
from turtle import*
shape("turtle")
i=-1
for i in range(3):
    forward(90)
    color(mau[i-1])
mainloop()