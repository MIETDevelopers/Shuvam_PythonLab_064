#Write a program that inputs a text file. The program should print all of the unique words in the file in alphabetical order
#creating a text file - myfile
f = open("myfile.txt","w")
#writing into the file
text = f.write("This is an apple.\nApple is good for health.\nAn apple a day, keeps the doctor away.")
#closing the file
f.close()
#opening the file in read mode
f = open("myfile.txt","r")
#reading the contents of file
text = f.read()
print(text)
#converting all the text into lower case
text = text.lower()
#converting the string into list
aplhabet = text.split()
#removes all the punctuation
alhabet = [alhabet.strip('.,!;()[]') for alhabet in aplhabet]
#removes all the apostrophes and white spaces
alhabet = [alhabet.replace("'s", '') for alhabet in aplhabet]
#creating an empty list
l = []
#iterating over the list
for alhabet in alhabet:
    #using if and membership operator to check the unique words
    if alhabet not in l:
        l.append(alhabet) #appending the list
l.sort() #sorting the list
print(l) #printing the list