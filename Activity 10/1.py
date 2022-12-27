#class to add and subtract two numbers
class A:   #defining a class called A
    def __init__(self):    #constructor
        self.a = int(input("Enter the first number : "))
        self.b = int(input("Enter the second number : "))
    def show(self):  
        print("First Number = ",self.a)
        print("Second Number = ",self.b)
    def cal(self):   #function to calculate 
        self.c = self.a + self.b
        self.d = self.a - self.b
    def output(self):
        print("Addition = ",self.c)
        print("Subtraction = ",self.d)
abc = A()  #creation of object
abc.show()  #calling of function
abc.cal()
abc.output()