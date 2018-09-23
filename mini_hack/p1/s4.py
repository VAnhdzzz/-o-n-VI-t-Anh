from turtle import*
shape("turtle")
speed(0)
n = int(input("nhap ban kinh cua hinh tron "))
forward(n)
for i in range(360):
    forward(5)
    left(1)
mainloop()