alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
encrypt=input("Type'encode' to encrpyt or 'decode' to decrypt:").lower()
msg=input("Enter the message:").lower()
shift=int(input("Enter the no. of shift:"))
l4=[]
for i4 in msg:
    l4.append(i4)
l1=len(l4)
l3= -1
s1=(26-shift)
if encrypt=="encode":
        
    for i in range(0,l1):
        
        l2=l4[i]
        for i1 in alphabet:
            l3+=1
        
            if l2==i1:
                if l3<s1:
                    l4[i]=alphabet[l3+shift]
                    l3= -1
                    break
                else:
                    l3=(s1-1)-l3
                    l4[i]=alphabet[l3+shift]
                    l3= -1
                    break
            else:
                continue
       
    code=""
    for i2 in l4:
        code+=i2
    print("Your new code is:",code)     
elif encrypt=="decode":

    s1=25+shift
    for i in range(0,l1):
        l2=l4[i]
        for i1 in alphabet:
            l3+=1
        
            if l2==i1:
                if l3<shift:
                    l3=s1-l3
                    l4[i]=alphabet[l3-shift]
                    l3= -1
                    break
                else:
                
                    l4[i]=alphabet[l3-shift]
                    l3= -1
                    break
            else:
                continue
    code=""
    for i2 in l4:
        code+=i2
    print("your decoded code is:",code)        
else:

    print("You have entered wrong value")   