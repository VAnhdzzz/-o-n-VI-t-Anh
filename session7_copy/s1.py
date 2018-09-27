x =[]
print (x)
thich = ["da bong"]
print (thich)
sothich =["da bong","co tuong","vainglory"]
print (sothich)
sothich.append("an")
print (sothich)
nhap = input("them so thich")
sothich.append(nhap)
print (sothich)
print (*sothich)
print (*sothich, sep = ",")
print(*sothich, sep = "|")
print (sothich[0],sothich[3],sothich[4])
a = [sothich[0].upper(),sothich[3].upper(),sothich[4].upper()]
print (a)
print (sothich[0].upper())
print (sothich[3].upper())
print (sothich[4].upper())
sothich [0] = "co chu nha va ong tho sua ong nuoc"
print (sothich)
sothich [4] = "toi thay hoa vang tren co xanh"
sua = input("sua phan tu 0")
sothich [0] = sua
print (sothich)
sothich.pop(1)

if "lol" not in sothich:
    print ("phan tu lol khong ton tai")

i = int(input ("xoa phan tu thu "))
sothich.pop(i)
print(sothich)
a = input("xoa phan tu ")
sothich.renove(a)
print (a)


