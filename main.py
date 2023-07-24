'''
import datetime
#dx1=int(input("Enter your Birth day:"))
yx1=int(input("Enter your Birth Year:"))

#mx1=int(input("Enter your Birth month:"))
#dx= int(datetime.datetime.now().day)
#mx=(datetime.datetime.now().month)
yx=(datetime.datetime.now().year)

y=yx-yx1

print('your age is :',y)
#print(x)
''''''
ayu=['ayush','ansil','aditya','abhinav']
print(type(ayu))

ayu.append('akriti')
print(ayu)
'''
''''
i1=int(input("write any no.:"))
l1=[]
x=0
while x<i1:
    l1.append(x+1)
    print(l1)
    x=x+1
    '''
'''
s1 = input("Write any charcter:")
# i1=int(input("Write the term to remove from string"))
a = len(s1)
i = 0
while i < a:
    if i % 2 == 0:
        a3 = s1[i]
        a1 = s1.replace(a3, "")
        print(a1)
        i = i + 1
        continue

    else:
        i = i + 1
        continue

print(a1)
'''
'''
i1=int(input("Enter any no."))
i=i1
while i<=i1:
     print(i*"x")
     i=i-1
     if i==0:
          break
     else:
          continue
   '''       '''
def temp(c):
    f=c+273.15
    return print(f)
c=float(input("write temp in c:"))
temp(c)
'''
