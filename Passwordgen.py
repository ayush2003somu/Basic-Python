import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

i2=int(input("Write no. of alphabet: "))
i4=int(input("Write no. of special char: "))
i3=int(input("Write no. of digit: "))
i1=(i2+i3+i4)

password=""
for i in range(0,i1):
    if i<i2:

        s1=random.choice(letters)
        password +=s1

    elif i<(i3+i2):
        s2=random.choice(numbers)
        password += s2
        
    else:
        s3=random.choice(symbols)
        password +=s3

print("Total character in your password is:",i1)
print("Your password is :",password)