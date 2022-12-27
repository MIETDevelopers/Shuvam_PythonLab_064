#single Inheritance
class parent:  #parent class
    def show(self):
        print("Inside Parent !")
class child(parent):  #child class
    def get(self):
        print("\nInside Child !")
b1 = child()  #creating object
b1.show()  #calling of functions
b1.get()