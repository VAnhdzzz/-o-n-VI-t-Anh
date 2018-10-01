highscore = [45,100,37,78]
highscore.sort()
print (highscore)
a = len(highscore)
b = 0
for i in range (len(highscore)):
    a-=1
    b +=1
    print (b,".",highscore[a])
    if a <0 and b>len(highscore):
        break
# them diem luon
new = int(input("enter your new highscore: "))
highscore.append (new)
highscore.sort()
print (highscore)
a = len(highscore)
b = 0
for i in range (len(highscore)):
    a-=1
    b +=1
    print (b,".",highscore[a])
    if a <0 and b>len(highscore):
        break

new = int(input("enter your new highscore: "))
highscore.append (new)
highscore.sort()
print (highscore)
a = len(highscore)
b = 0
for i in range (5):
    a-=1
    b +=1
    print (b,".",highscore[a])
    if a <5 and b>5:
        break

