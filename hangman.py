import json
import random
data = json.load(open("data.json"))
n = random.randint(1,100)
l = list(data.keys())
word= l[n]

attempt = 10
name = input("Enter your name :")
print("WELCOME "+name.upper()+"\n___________________")
print("You have 10 attempts to guess the word")
x = ""
for i in word:
    x = x + "_"

while attempt>0 and x != word:
    s=""
    print("Guess the character " + x)
    ch = input()
    if ch in word:
        print("YEAH, You get that right keep it up")
        j=0
        for i in word:
            if x[j] == "_":
                if i == ch:
                    s = s + ch
                else:
                    s = s + "_"
            else:
                s = s + x[j]
            j = j + 1
        x = s
    else:
        print("OH! NO You are wrong this time")
        attempt = attempt - 1
        print("Now you have only %d attempts left"%attempt)
        print("Don't let the good man get killed")
        print("_____________")
        if attempt==9:
            print("   O     ")
            print("    \n      ")
        elif attempt==8:
            print("  \O     ")
            print("    \n      ")
        elif attempt==7:
            print("  \O/    ")
            print("    \n      ")
        elif attempt==6:
            print("  \O/    ")
            print("   |\n      ")
        elif attempt==5:
            print("  \O/    ")
            print("   |\n  /   ")
        elif attempt==4:
            print("  \O/    ")
            print("   |\n  / \ ")
        elif attempt==3:
            print("  \O/  |")
            print("   |\n  / \ ")
        elif attempt==2:
            print("  \O/ _|")
            print("   |\n  / \ ")
        elif attempt==1:
            print("  \O/__|")
            print("   |\n  / \ ")
        elif attempt==0:
            print("   O___|\n  /|\ ")
            print("  / \ ")
            print("YOU LOSE THE GOOD MAN GET KILLED \n the word is "+word)
