#Hierarchical Inheritance
class parent:  # class parent
    def get(self):
        print("HELLO, I am Parent.")
class child1(parent):  # class child 1
    def input(self):  
        print("HELLO, I am Child 1.")
class child2(parent):  #child class 2
    def abc(self): 
        print("HELLO, I am Child 2.")
c1 = child1()   #creating object for child 1
c1.get()   #calling functions
c1.input()
print("\n")
c2 = child2()  #creating object for child 2
c2.get()
c2.abc()