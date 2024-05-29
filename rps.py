import random

userscore = 0
compscore = 0
rpslist = ["r", "p", "s"]
print("Try to beat the computer! First to five wins...\n")

while userscore < 5 and compscore < 5:
    userguess = input("Enter r for rock, p for paper, s for scissors: ").lower()
    if userguess not in rpslist:
        print("\nYou must enter r, p, or s...\n")
        continue
    randnum = random.randint(0, 2)
    compguess = rpslist[randnum]
    if compguess == userguess:
        print(f"\nYou and the computer both picked {userguess}...\n")
    elif userguess == "r" and compguess == "s":
        print(f"\nYou won that round! Computer chose {compguess}\n")
        userscore += 1
    elif userguess == "p" and compguess == "r":
        print(f"\nYou won that round! Computer chose {compguess}\n")
        userscore += 1
    elif userguess == "s" and compguess == "p":
        print(f"\nYou won that round! Computer chose {compguess}\n")
        userscore += 1
    else:
        print(f"\nYou lost that round... Computer chose {compguess} \n")
        compscore += 1

print("\n-------------------------")
print("\nThat's game!\n")

if userscore > compscore:
    print(f"You won that game {userscore} to {compscore}!")
else: 
    print(f"You lost that game {compscore} to {userscore}...")

