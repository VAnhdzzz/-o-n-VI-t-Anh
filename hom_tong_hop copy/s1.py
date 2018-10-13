# for i in range (20):
#     print ("*",end = " ")
# n = int(input("nhap so"))
# for i in range (n):
#     print ("*", end = " ")
# for i in range(9):
#     print ("x *", end = " ")
# nhap = int(input("nhap so"))
# if nhap %2 ==0:
#     for i in range(int(nhap/2)):
#         print ("x","*", end = " ")
# else:
#     print ("*", end = " " )
#     for i in range (int(nhap/2)):
#         print ("x","*", end = " ")
    

# for i in range(3):
#     print ("* " * 7)
# m = int(input())
# n = int (input())
# for i in range (m):
#     print ("*" *n)

for i in range (5):
    for j in range(6):
        if i ==4 and j ==2:
            print ("x ", end="")
        else:
            print ("- ", end = "")
    print()
x = int(input())
y = int (input())
h = int (input())
w = int (input())
for i in range (h):
    for j in range(w):
        if i == x and j == y:
            print ("x ",end = "")
        else:
            print ("- ", end ="")
    print()
        
