#maximum of 3 numbers

#using function
a = int(input("Enter The First Number : "))
b = int(input("Enter the Second Number : "))
c = int(input("Enter the Third Number : "))

def maximum(a,b,c):
    if a>=b and a>=c:  
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(f"Maximum = {maximum(a,b,c)}")

#using lists and max function
l = []
n = int(input(f"Enter how many elements you want : "))
for i in range(n):
    num = int(input(f"Enter The Number {i+1} : "))
    l.append(num)
print(f"List = {l}")
max_l = max(l)
print(max_l)