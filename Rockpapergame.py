import random
s1=int(input("Enter your choice:1.rock ; 2.Paper ; 3.Scissor"))
s2=random.randint(1,3)
s4="you win"
s5="you loose"

if s1==1:
    print('''you choose Rock:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          ''')
    
elif s1==2:
    print('''you choose Paper
   
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

          ''')   

elif s1==3:
    print('''you choose scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          ''')     
    
else:
    print("Wrong selection")
    


if s2==1:
    print('''computer choose Rock:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          ''')
    
elif s2==2:
    print('''computer choose Paper
   
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

          ''')   

elif s2==3:
    print('''computer choose scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          ''')     
    
else:
    print("Wrong selection")
    


if (s1==2 and s2==1) or (s1==3 and s2==2) or (s1==1 and s2==3):
    print(s4)

elif (s1==3 and s2==1) or (s1==2 and s2==3) or (s1==1 and s2==2):
    print(s5)

else:
    print("Game tied")