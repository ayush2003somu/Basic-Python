#x=int(input("Write the no. limit:"))
y=int(input("Write the no. to be checked:"))
x=2
x1=False
if y==1:
    print("Number is not prime")

else:
    while x < y:

        if y % x == 0:

            x1 = True
            break
        else:
            x1=False
        x = x + 1

    if x1 == True:
        print("Number is not prime")
    elif x1 == False:
        print("Number is prime")
