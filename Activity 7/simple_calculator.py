# a program to create a Simple Calculator using a switch case and function for every operation.
def get():
    a = int(input('\nEnter the Number 1 : '))
    b = int(input('Enter the Number 2 : '))
    return a,b

def add():   #addition function
    a, b = get()
    return a + b

def sub():   #subtraction function
    a, b = get()
    return a - b

def mul():  #multiplication function
    a, b = get()
    return a * b

def div():   #division function
    a, b = get()
    return a / b

def error():  #error  function
    return "Invalid Choice"

switcher = {      #creation of dictionary
        1 : add,
        2 : sub,
        3 : mul,
        4 : div
}

print('\n\t\tOperations')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

choice = int(input("\nEnter the Required Choice : "))

result = switcher.get(choice,error)()   #using get function to get result
print(result)