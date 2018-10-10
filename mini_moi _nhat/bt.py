kho = {
    "HP" : 20,
    "DELL": 50,
    "MACBOOK":12,
    "ASUS":30,
}
# print (kho)
# print (kho["MACBOOK"])
# print (kho[input("tra cai gi ")])
# kho["TOSHIBA"] = 10
# kho[input("them")] = int(input("so luong"))
kho["DELL"] +=10
kho["MACBOOK"] -= 2

for k,v in kho.items():
    print(k,v,sep =":")
tong = []
for v in kho.values():
    tong.append(v)
print (sum(tong))
kho["FUJISU"] = 15
kho["ALIENWARE"] = 5

