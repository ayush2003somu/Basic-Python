#basic of opening,creating and writing on file.

file=open("file.txt" , "r") #command to read a existing a text file
file2=open("file2.txt","w")  #command to make a new text file
x1=file2.write("Ayush Srivastava""  "
               "\n" "Btech CSE")   #command to write in the text file
file2=open("file2.txt","r")  #command to read new made file

x=file.read()       #read command
x1=file2.read()

print(x)
print("  \n   ")            #print
print(x1)

file.close()
file2.close()