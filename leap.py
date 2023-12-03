inp=int(input("enter the year:"))
i1=inp/4
i2=inp//4
if i1-i2==0:
    print("year is leap year")
else:
    print("Not leap year")    