'''a python program that accepts the length of three sides of a triangle
as inputs. The program should indicate whether or not the triangle is a
right-angled triangle. Also find out its area using Heron's formula.'''

#taking sides through user
s1 = int(input('Enter the length for side 1 : '))
s2 = int(input('Enter the length for side 2 : '))
s3 = int(input('Enter the length for side 3 : '))
if(s3*s3 == s1*s1 + s2*s2): #using pythagores theorem 
    print("Triangle is RIGHT-ANGLED")
else:
    print("Triangle is not Right-Angled")
s_peri = (s1 + s2 + s3) / 2  #area using heron's formula
area = ((s_peri)*(s_peri-s1)*(s_peri-s2)*(s_peri-s3))**0.5
print("Area = ",area)