#multiple Inheritance
class parent1:  # class parent 1
    def get(self):
        print("HELLO, I am Parent 1.")
class parent2:  # class parent 2
    def input(self):  
        print("HELLO, I am Parent 2.")
class child(parent1,parent2):  #child class
    def abc(self): 
        print("HELLO, I am Child.")
c1 = child()   #creating object 
c1.get()   #calling functions
c1.input()
c1.abc()