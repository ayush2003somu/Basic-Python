#Write a Python program to find the factorial of a number. ##
# n1=int(input("Enter the number:"))
 
# for i in range(1,n1+1):
#     a2=a2*i
# print(a2) 


##  Write a Python program to print the Fibonacci sequence up to n terms.  ##

# f0=0
# f1=1

# for i in range(0,n1+1):
#     if i==0:
#         print(f0,f1, end=" ")
#     else:
#         a3=f0+f1
#         print(a3, end=" ")
#         f0=f1
#         f1=a3

## program to find sum of digit ##
# n1=input("Enter the digit")
# a3=0
# for i in n1:
#     i=int(i)
#     a3=a3+i
# print(a3)

## program to convert celsius to fahrenheit ##

# far=(n1*9/5)+32
# print(far)
# Write a Python program to count the number of vowels in a string
# i1=input("Enter the string:").lower()
# vowels="a,e,i,o,u"
# count=0
# for i in i1:
#     for j in vowels:
#         if i==j:
#             count+=1

#         else:
#             continue    

# print(count)
    
## 8. Write a Python program to find the largest element in a list.

# i1=input("Enter any string:")
# s1=i1[::-1]
# print(s1)

# 13. Write a Python program to find the second largest element in a list

# str=input("enter 1st string")
# str2=input("ENter 2nd string")
# str1=sorted(str)
# str3=sorted(str2)
# if str1==str3:
#     print("Strings are anagram ")
# else:
#     print("Not anagram")        


#program to find the highest and the lowest marks in give 5 subjext with name

n1=int(input("MAths"))
n2=int(input("hindi"))
n3=int(input("english"))
n4=int(input("IT"))
n5=int(input("physics"))  

s1=(n1,n2,n3,n4,n5)

a1=0

for i in s1:
    if i>a1:
        a1=i
    else:
        continue
a2=a1
for i in s1:
    if i<a2:
        a2=i   
    else:
        continue

for i in range(0,5):
    if s1[i]==a1:
        if i==0:
            print("higest is maths",a1)
        elif i==1:
            print("hindi is highest",a1)
        elif i==2:
            print("English is highest",a1)  
        elif i==3:
            print("IT is highest",a1)
        elif i==4:
            print("physics is highest",a1)
    else:
        continue                  
for i in range(0,5):
    if s1[i]==a2:
        if i==0:
            print("lowest is maths",a1)
        elif i==1:
            print("hindi is lowest",a1)
        elif i==2:
            print("English is lowest",a1)  
        elif i==3:
            print("IT is lowest",a1)
        elif i==4:
            print("phy is low",a1)
    else:
        continue            

print(a1)    # higest marks
print(a2)    # lowest marks       