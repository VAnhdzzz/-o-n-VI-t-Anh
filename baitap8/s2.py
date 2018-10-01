#2
#danhsachso = [1,0,3,6,5]
# print (danhsachso)
# n = int(input("nhap vao 1 so:"))
# if n  not in danhsachso:
#     print("khong co trong danh sach")
# else:
#     print("co ")
#     i=-1
#     l = True
#     while l:
#         i+=1
#         if i>4:
#             loop =False
#         elif danhsachso[i]== n:
#             print ("vi tri",i+1)
#             loop =False
#         else:
#             pass

            

# 3 dung list bai 1
# loop = True
# i=-1
# a=0
# while loop:
#     i+=1
#     if i>3:
#         print ("het roi")
#         loop = False
#     else:
#       a += danhsachso[i]
# print (a, end=" ")
# cach2
# print (sum(danhsachso))
# danhsachso= []
# nhapso = (input("nhap them bao so cung duoc "))
# danhsachso = nhapso.split(",")
# print (danhsachso)
# danhsachso = list(map(int,danhsachso))
# print (danhsachso)
# loop = True
# i=-1
# a=0
# while loop:
#     i+=1
#     if i>len(danhsachso)-1:
#         print ("het roi")
#         loop = False
#     else:
#         a += danhsachso[i]
#print (a)
#cach 2
#print (sum (danhsachso))


# chan = [1,3,6,8]
# a = True
# i =-1
# for i in range (4):
#     if chan[i] % 2 ==0:
#         print (chan[i],end = ",")
#     else:
#         pass

# so = []
# n = (input ("enter a list of number"))
# so = n.split(",")
# so =list(map(int,so))
# print (so)
# i =0
# for i in range (0,len(so)-1):
#     i+=1
#     if so[i] % 2 == 0:
#         print (so[i])
#     else:
#         pass 
danhsach = []
nhap = input ("nhap nhieu so bat ki: ")
danhsach.extend([nhap])
print (danhsach)