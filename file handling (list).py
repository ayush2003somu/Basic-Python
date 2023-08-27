
#Code To write a list in text file.
x=[ "Hello Guys ","My Info:-","Ayush Srivastava","B.tech 'CSE'","GNDU","AMRITSAR"]
file=open("file3.txt","w")# this line is for creating the text file
#we will use 'for' loop for writing list
for i in x:
    file.write(i+ "\n") #command for writing in text file.

file=open("file3.txt","r")
x1=file.read()
print(x1)
file.close()
#Always close the file.

