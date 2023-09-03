#Code To write a list in text file.
i1=input("What is your name:")
print("Hello,",i1,"You are proceeding to write and read in a text file.\n Please input the sentences you want to add \n in the list in four coloumn. ")
i2=input("Here, Goes The First Coloumn:")
i3=input("Second one here:")
i4=input("Third coloumn")
i5=input("And the last one:")
x=[i2, i3, i4 , i5]
file=open("file4.txt","w")# this line is for creating the text file
#we will use 'for' loop for writing list
for i in x:
    
    file.write(i+ "\n") #command for writing in text file.
    
file=open("file4.txt","r")
x1=file.read()
print(x1)    
file.close()
#Always close the file.