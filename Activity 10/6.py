#multi level Inheritance
class parent:  # class parent
    def get(self):
        print("HELLO, I am Parent.")
class child(parent):  # class child
    def input(self):  
        print("HELLO, I am Child.")
class grandchild(child):  #child grandclass
    def abc(self): 
        print("HELLO, I am GrandChild.")
c1 = grandchild()   #creating object 
c1.get()   #calling functions
c1.input()
c1.abc()