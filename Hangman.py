import random
word_list=["mathmatics","mechanics","science","technology","electronics"]

a1= random.choice(word_list)
print("Pssst,Solution is",a1)

l2=[]
for letters in a1:
    l2.append("_")
print(l2)
lives=6    
for i4 in range(len(a1)+6):
    i1= input("enter Any letter:").lower()
    i3=0
    live_1=False
    for i in a1:
        
        if i==i1:
            print("you guessed right")
            l2[i3]=i1
            i3+=1
            live_1=True
        else:
            #print("wrong")
    
            i3+=1
    print(l2)
    if "_" not in l2:
        print("Congratulation,you won the game")
        break
        
    if live_1==True:
        print("Lives Left",lives)
        continue
        
    else:
        lives -=1    
        
        print("Lives left:",lives)
    
    if lives==6:
        continue
    
    if lives == 5:
        print("""
  +---+
  |   |
      |
      |
      |
      |
=========""") 
        
    if lives==4:
        print(""" 
  +---+
  |   |
  O   |
      |
      |
      |
=========""")   
    if lives==3:
        print("""  
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""")
    if lives==2:
        print("""  
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""")  
    if lives==1:
        print("""  
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""")  
    if lives==0:
        print("""  
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
              
You Loose as you lost all of your lives          """)  
        break               
    

  


