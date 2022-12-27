'''Sum of number digits in List'''
l = []  #creating an empty list
n = int(input(f"Enter how many elements you want : "))
for i in range(n):  #using for loop for entering the number
    num = int(input(f"Enter The Number {i+1} : "))
    l.append(num) #it will add the numbers entered by user in the list l
print(f"List = {l}")

temp = []  #creating a temporary list
for ele in l: #iterating over the elemnts in the list l
    sum = 0 #intiliazing the sum of digits to zero
    for digit in str(ele): #using for loop 
        sum = sum + int(digit)
    temp.append(sum)
     
print ("Sum of digits of List : ",temp)