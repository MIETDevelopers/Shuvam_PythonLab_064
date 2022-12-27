f = open("exp.txt","w")   #opening of file
a = input("Enter the line : \n")   #taking user input
b = input("Enter the line : \n")
c = input("Enter the line : \n")
new_line = "\n"   #printing new line 
f.write(a)   #writing into file
f.write(new_line)
f.write(b)
f.write(new_line)
f.write(c)
print("\n")

f = open("exp.txt","r")   #opeining the file in read mode
print(f.read())  #printing what is written into file
