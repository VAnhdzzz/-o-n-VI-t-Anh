kho = {
    "HP" : 20,
    "DELL": 50,
    "MACBOOK":12,
    "ASUS":30,
    "ACER" : 10,
    "TOSIBA" : 17,
    "FUSISU" : 15,
    "ALIENWARE" : 5
}
gia = {
    "HP" : 600,
    "DELL": 650,
    "MACBOOK": 12000,
    "ASUS": 400,
    "ACER": 350,
    "TOSHIBA": 600,
    "FUJISU": 900,
    "ALIENWARE": 1000,
}
# print (gia["ASUS"])
# print (gia[input("xem cgi")])
# print ("tong gia tri don hang ",gia["ASUS"]*5)
hang = input(" hang may la gi")
so = int(input("so luong la bao nhieu"))
# print (gia[hang]*so)
kho[hang]  -= so
nhap = input("nhap hang va so luong")
nhap = nhap.split(":")
# print (nhap)
nhap[1] = int(nhap[1])
# print(kho["HP"])
kho[nhap[0]] -= nhap[1]
# print(kho)
day_kho = []
day_gia = []
for v in kho.values():
    day_kho.append(v)
for val in gia.values():
    day_gia.append(val)
print (day_kho)
print (day_gia)
a = 0
for i in range(0,8):
    a+=day_kho[i]*day_gia[i]
print (a)

    


