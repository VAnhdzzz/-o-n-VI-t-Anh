character_in_text_adventure ={
    "Name" : "Light",
    "Age" : 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield","Bread Loaf"],
    "Gold": 100,
    "Level": 2
}
character_in_text_adventure["Gold"] += 50
character_in_text_adventure["Backpack"].append("Flintstones")
character_in_text_adventure["Pocket"] = ["MonsterDex","Flashlight"]
skill_character =[
    {
        "Name" : "Tackle",
        "Minimum level": 2,
        "Damage" : 3,
        "Hit rate": 0.5,
    },
    {
        "Name" : "Quick attack",
        "Minimum level": 2,
        "Damage" : 3,
        "Hit rate" : 0.5,
    },
    {
        "Name" : "Strong Kick",
        "Minimum level": 4,
        "Damage": 7,
        "Hit rate": 0.2
    }
]
skill_tackle = skill_character[0]
skill_quick = skill_character[1]
skill_strong = skill_character[2] 
# for p in skill_character:
#     print (p,sep= "\n")
for i in range(0,3):
    print (i+1,".   ",skill_character[i]["Name"])

loop = True
i = 0
from random import randint
x = randint
while loop:
    from random import randint
    x = randint(0,10)
    i +=1
    n = int (input("choose a number to start the combat: "))
    if n >3:
        print ("you are not choosing any skills")
        continue
    if character_in_text_adventure["Level"] < skill_character[n-1]["Minimum level"]:
        print ("your level is not high enough to use this skill")
    else:
        print (x)
        x  = float(x/10)
        print ("x ",x)
        print ( "Damage: ",skill_character[n-1]["Damage"])
        if skill_character[n-1]["Hit rate"]>x:
            print ("you miss the target")
        else :
            print ("Enemy has been attacked")
    if i >5:
        print ("your turn is over")
        loop = False

    

