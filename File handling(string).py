x11=("Ayush Srivastava""\n""Btech CSE" "\n" "Guru" " " "Nanak" " " "Dev" " " "University")

file=open("file2.txt","w")
file.write(x11)
file=open("file2.txt","r")
x=file.read()
print(x)
file.close()