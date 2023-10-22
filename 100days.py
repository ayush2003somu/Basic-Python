
#bill generator
'''
s1=int(input("total bill:"))
s2=int(input("How many people:"))
s3=int(input("How much % tip you have to pay :"))
s4=s1+(s1*s3/100)
print("each people have to pay:",s4/s2,("(including  tip)"))
'''


# finding average of list
'''
list_1=input("enter a list with spacing:").split()

for i in range(0,len(list_1)):
    list_1[i]=int(list_1[i])

th=0
for i in list_1:
    th=i+th
print(th)
print("average of list is:",th//len(list_1))

'''

#finding highest no. in list(user input)
'''
list_1=input("enter a list with spacing:").split()

for i in range(0,len(list_1)):
    list_1[i]=int(list_1[i])

th=0
for i2 in list_1:
    if i2>th:
        th=i2
    else:
        continue
print("highest no, is:",th)            
'''
'''
th=0
for i in range(0,101):
    if i%2==0:
        th+=i
    else:
        continue

print(th)        
'''

#Divisibility test fizz(3) buzz(5)  fizzbuzz(3 and 5)
'''
i1=int(input("Write a max no.:"))
for i in range(1,i1+1):
    if i%15==0:
       print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("Buzz")
    
    else :
        print(i)

'''

# Random Password generator
'''
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

i2=int(input("Write no. of alphabet: "))
i4=int(input("Write no. of special char: "))
i3=int(input("Write no. of digit: "))
i1=(i2+i3+i4)

password=[]
for i in range(0,i1):
    if i<i2:

        s1=random.choice(letters)
        password.append(s1)

    elif i<(i3+i2):
        s2=random.choice(numbers)
        password.append(s2)
        
    else:
        s3=random.choice(symbols)
        password.append(s3)

random.shuffle(password)       ##this function can be used to suffle the passcode but this can only be used in python thats why we will choose another method to shuffle our passcode.
print("Total character in your password is:",i1)
print("Your password is :",password)
'''
'''
s7=[]
for i3 in range(0,i1):
     for i4 in range(0,i1):
         
         s7.append(i4)

         password[i3]=password[i4]
print(password)
'''
#learning def
'''
i1=int(input("Enter the no. to so how many times the list should be shown.:"))
def ayush():
    print("ayush Srivastava")
    print("Ansil Srivastava")
    print("Abhinav Srivastava")
    print("Aditya srivastava")
    print("Aditi Srivastava")
    print("Akriti Srivastava")

for i in range(1,i1+1):
    print("This is the list of Gen Z :-")
    ayush()
    '''

#learning the hangman project
'''
l1= ("h","e","l","l","o","w","o","r","l","d")
l2=0
l3=0
while l2<10 and l3<15:
    i1=input("guess the letter:")
    if i1=="h"or:
        l2+=1
        print("you guessed right word")
    else:
            
        l3= l3+1
        print("wrong selection you got only",(15-l3) ,"chance left.")

if l3==15:
    print("you are hunged")
elif l2==10 :
     print("You won")
     '''

# Programm to guess a letter and replace it on the second list.(Part of project hangman Game)
'''
import random
word_list=["ayusah","aditaya","ansail"]

a1= random.choice(word_list)


i1= input("enter Any letter:")
l2=[]
for letters in a1:
    l2.append("_")
print(l2)
for i in a1:
    
    if i==i1:
        print("right")
        
    else:
        print("wrong")
i3=0
for i5 in a1:
    if i1==i5:

        l2[i3]=i1
    else:
        i3+=1
print(i3) 
print(l2)           
'''

#Painting a wall with cans
'''
h1=int(input("Enter height of the wall:"))
w1=int(input("Enter width of the wall:"))
cover=int(input("Enter the coverage area per can:"))
area=h1*w1
cans=area//cover
cans2=area/cover
if (cans2-cans)==0:
    print("No. of cans required to paint the wall is:",cans)
else:
    cans3= cans + (cans%cover)
    print("No. of cans required to paint the wall is:",cans3)
    
    '''

#Learning Some Dictionaries
'''
i1=int(input("Enter the score of rahul:"))
i2=int(input("Enter the score of arpit:"))
i3=int(input("Enter the score of ashish:"))
i4=int (input("Enter the score of rishabh:"))
d1={"rahul":i1,
    "arpit":i2,
    "Ashish":i3,
    "Rishabh":i4
}

d3={}

for key in d1:
    if d1[key]>90 :
        d3[key]="outstanding"
    elif d1[key]>80:
        d3[key]="Exceeds Expecation"
    elif d1[key]>70:
        d3[key]="Acceptable"
    else:
        d3[key]="Fail"

for keys in d3:
    print(keys,"=",d3[keys])

'''