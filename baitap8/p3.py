district = ["ST","BĐ","BTl","CG","ĐĐ","HBT"]
pop = [150300,247100,333300,266800,420900,318000]
print (min(pop))
print (max(pop))
print ("ĐĐ dong nhat")
print ("ST it nhat")
km2 = [117.43,9.224,43.35,12.04,9.96,10.09]
pop_density = []
a=-1
for i in range (6):
    a+=1
    pop_density.append(pop[i]/km2[i])
print (pop_density)

print ("mat do dan cu trung binh ",sum(pop_density)/6)