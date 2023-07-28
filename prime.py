i1=int(input("Write any no.:"))
flag= False
if i1==1:
    print("Not prime")
elif i1>1:
    for i in range(2,i1):
        if (i1%i)==0:
            flag=True
            break
if flag== False:
    print("Prime")
elif flag== True:
    print("Not prime")