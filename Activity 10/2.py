#CLASS ATTRIBUTES AND INSTANCE ATTRIBUTES
class Cylinder:
# class attribute
    pi = 3.14

    def __init__(self, radius, height):  #constructor
    # instance variables
        self.radius = radius
        self.height = height

if __name__ == '__main__':   #MAIN FUNCTION

    c1 = Cylinder(4, 20)
    c2 = Cylinder(10, 50)

    print(f'Pi for c1:{c1.pi} and c2:{c2.pi}')
    print(f'Radius for c1:{c1.radius} and c2:{c2.radius}')
    print(f'Height for c1:{c1.height} and c2:{c2.height}')
    print(f'Pi for both c1 and c2 is: {Cylinder.pi}')

print("\n")

#CLASS METHOD AND INSTANCE METHOD

class Cylinder:
# class attribute
    pi = 3.14
    def __init__(self, radius, height):
# instance variables
        self.radius = radius
        self.height = height
# instance method
    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height
# class method
    @classmethod
    def description(cls):
        return f'This is a Cylinder class that computes the volume using Pi={cls.pi}'

if __name__ == '__main__':

    c1 = Cylinder(4, 2) # create an instance/object
    print(f'Volume of Cylinder: {c1.volume()}') # access instance method
    print(Cylinder.description()) # access class method via class

    print(c1.description()) # access class method via instance