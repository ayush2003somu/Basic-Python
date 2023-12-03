import random
numbers=[2,3,4,5,6,7,8,9,10,10,10,10]

while 1>0:
    l1=[]
    l2=[]
    i1=input("Do you want to play game of Blackjack? Type 'y' or 'n':")
    if i1=="y":
        s1=random.choice(numbers)
        s2=random.choice(numbers)
        s3=random.choice(numbers)
        s4=random.choice(numbers)
        l1.append(s1)
        l1.append(s2)
        l2.append(s3)
        l2.append(s4)
        print("your card are:",l1,"Current score:",s1+s2)
        print("Computer's First card",s3)
        i2=input("Type 'y' to get another card, type 'n' to pass:")
        if i2=="y":
            s5=random.choice(numbers)
            l1.append(s5)
            a1=s1+s2+s5
            print("Your card:",l1,"final score:",a1)
            s6=random.choice(numbers)
            l2.append(s6)
            a2=s3+s4+s6
            print("Computers final hand:",l2,"Final score",a2)
            if a2==a1:
                print("Game Tied")
            elif a2>21:
                print("Computer wins")
            
            elif a1>21:
                print("You wins")
            else:
                if a1>a2:
                    print("You wins")
                else:
                    print("Computer wins")    