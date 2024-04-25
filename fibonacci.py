n1=int(input("Enter any number:"))
t1,t2=0,1
if n1 == 0:
    print(0)
elif n1 == 1:
    print(1)
elif n1<0:
    print("please enter postiive")
else:
    print (t1,t2,end=",")
    n2=0
    for i in range(2,n1):
        n2=t1+t2
        print(n2,end=",")
        t1=t2
        t2=n2

        

