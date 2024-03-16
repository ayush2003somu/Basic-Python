# write a python code to print prime 

num=int(input("Enter any no for range:"))
for i in range(2,num+1):
   a1=0
   a1=True
   if num>1:
      for k in range(2,i):
         if i%k==0:
            a1=False
            break
               
         else:
            a1=True    
   else:
      print("1 is not a prime number")
      break
   if a1==True:
      print(i)