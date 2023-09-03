'''
#bill generator

s1=int(input("total bill:"))
s2=int(input("How many people:"))
s3=int(input("How much % tip you have to pay :"))
s4=s1+(s1*s3/100)
print("each people have to pay:",s4/s2,("(including  tip)"))
'''

'''
# finding average of list
list_1=input("enter a list with spacing:").split()

for i in range(0,len(list_1)):
    list_1[i]=int(list_1[i])

th=0
for i in list_1:
    th=i+th
print(th)
print("average of list is:",th//len(list_1))

'''
'''
#finding highest no. in list(user input)

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
'''
#Divisibility test fizz(3) buzz(5)  fizzbuzz(3 and 5)

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
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

i2=int(input("Write no. of alphabet: "))
i4=int(input("Write no. of special char: "))
i3=int(input("Write no. of digit: "))
i1=(i2+i3+i4)


for i in range(0,i1):
    if i<i2:

        s1=random.choice(letters)
        password+=s1

    elif i<(i3+i2):
        s2=random.choice(numbers)
        password+=s2
        
    else:
        s3=random.choice(symbols)
        password+=s3

print("Total character in your password is:",i1)
print("Your password is :",password)        


