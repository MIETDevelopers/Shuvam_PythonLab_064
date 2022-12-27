'''Python program to print all positive numbers in a range'''
n = int(input('Enter the Range : '))
for i in range(1,n+1):#using for loop to iterate over numbers 
    if(i>0):
        print(i,end = " ")