bang = [
    {
    "name" : "Huy",
    "role" : "waiter",
    "hours" : 12,
    "salary per hour" : 0.8
    },
    {
        "name" : "Tung",
        "role" : "cook",
        "hours" : 24,
        "salary per hour" : 1.5
    },
    {
        "name" : "Minh Duc",
        "role": "Manger",
        "hours" : 20,
        "salary per hour" : 2
    }
]
#print (bang)
a = {
    "name" : "Don",
    "Role" : "waiter",
    "hours" : 12,
    "salary per hour" :0.9

}
b = {
    "name" : "H.Duc",
    "role" : "Waiter",
    "hours": 14,
    "salary per hour": 0.7
}
bang.append(a)
bang.append(b)
#print (bang,end= "\n")

#print (bang[2]["salary per hour"])
c = {
    "name" : "Huyen",
    "Role" : "Waitress",
    "hours" : 14,
    "salary per hour" : 1,

}
bang[0] = c
#print (bang[0])
del (bang[4]["salary per hour"])
#print (bang[4])
a = -1
for i in range (4):
    a +=1
    if "salary per hour" in bang[i]:
        print (bang[i]["salary per hour"])
    else:
        pass
print ("---------------")
for i in range (4):
    a +=1
    if "salary per hour" in bang[i]:
        print (bang[i]["salary per hour"]*720)
    else:
        pass


bang[4]["salary per hour"] = 0.7
moi_gio = []
for i in range(0,5):
    moi_gio.append(bang[i]["salary per hour"])
print (moi_gio)
so_gio = []
for i in range (0,5):
    so_gio.append(bang[i]["hours"])
print (so_gio)
tong =[]
for i in range(5):
    moi_gio[i] *= so_gio[i]
    tong.append(moi_gio[i])
print (tong)
print ("tong so tien ma chi nhanh phai tra theo tuan la ",sum(tong))
