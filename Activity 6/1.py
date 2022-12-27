#a program to create a list of student’s records and search a student record using a dictionary.

n = int(input('Enter the number of students : '))     #getting the of students form user
dict = {} #creating an empty dictionary to store name and marks
for i in range(1,n+1):   #using for loop for getting name and marks from user
    name = input(f'\nName for student {i} : ')
    marks = []  #creating an empty list to store marks of a student
    for j in range(3):
        markss = int(input(f'Marks for subject {j+1} :'))
        marks.append(markss)  #it will add the marks entered for a particular student in the list
    dict[name] = marks  #this will store the values in dictionary
print(f'\nDictionary : \n{dict}')

name = input("\nEnter the name whose record to be searched: ")

#get() function
for items in dict: #iteratiing over the dictionary
    if items == name:  #using if else to get the particular students name
        print(dict.get(items))  #using get function to get the name of student present in list
        break
else:
    print("Data not Exists")

#.keys() method
if name in dict.keys():  #searches over the particular key is present or not
    print(dict[name])
else:
    print('No Data Found')