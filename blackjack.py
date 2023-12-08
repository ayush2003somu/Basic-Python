import random
numbers=[11,2,3,4,5,6,7,8,9,10,10,10,10]

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
        a2=0
        a1=0
        for i in l1:
            if i==11:
                t1=0
                t1=+11
                
            elif i==1:
                t1=0
                t1=+1
                
        def repeat():    
            s5=random.choice(numbers)
            l1.append(s5)
            
            for i in l1:
                a1=+i

            print("Your card:",l1,"final score:",a1)
            s6=random.choice(numbers)
            l2.append(s6)
            
            for i5 in l2:
                a2=+i5

            print("Computers final hand:",l2,"Final score",a2)
        for i in range(0,2):
            i2=input("Type 'y' to get another card, type 'n' to pass:")    
            if i2=="y":
                repeat()    
                if a2==a1:
                    print("Game Tied")
                elif a1>21 and a2>21:
                    if a1>a2:
                        print("computer wins")
                    else:
                        print("you wins")

                elif a1>21 or a2>21:
                    if a1>21 and a2<21 :
                        print("computer win")
                    elif a2>21 and a1<21:
                        print("You wins")
                elif a1<21 and a2<21:
                    if a1>a2:
                        print("you wins")
                    else:
                        print("Computer wins")                
                 
            else:
                s6=random.choice(numbers)
                l2.append(s6)
                a1=0
                for i in l1:
                    a1=+i
                a2=0
                for i5 in l2:
                    a2=+i5    
                
                print("Your card:",l1,"final score:",a1)
                print("Computers final hand:",l2,"Final score",a2)
                if a2==a1:
                    print("Game Tied")
                elif a1>21 and a2>21:
                    if a1>a2:
                        print("computer wins")
                    else:
                        print("you wins")

                elif a1>21 or a2>21:
                    if a1>21 and a2<21 :
                        print("computer win")
                    elif a2>21 and a1<21:
                        print("You wins")
                elif a1<21 and a2<21:
                    if a1>a2:
                        print("you wins")
                    else:
                        print("Computer wins")

                
                break
                        