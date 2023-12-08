import random
print("Welcome to Number guessing game!\nI'm Thinking of a number Between 1 to 100.")
i1=input("Choose Difficulty. Type 'Easy' or 'hard':").lower()
i2=0

if i1=="hard":
    print("You have 5 Attempts to guess.")
    i2=5
elif i1=="easy":
    print("You have 10 attempts to guess the number.")
    i2=10
else:
    print("You have entered wrong value.Please re-run the code.")
i3=random.randint(1,100)
#print("For code check",i3)

while i2>0:
    i4=int(input("Guess the number:"))
    if i3==i4:
        print("You have guessed correct Number\nYou Won the game!!")
        break
    elif i3>i4:
        i2-=1
        print("Guess is too low.\nyou have only",i2,"Chance left.")
        
    else:
        i2-=1
        print("Guess is to high.\nyou have only",i2,"Chance left")
               