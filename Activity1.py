# python numbers
a=5
print(a,"is of type",type(a))
a=2.0
print(a,"is of type",type(a))
a=1+2j
print(a,"is complex",isinstance(1+2j,complex))

#python list

a=[1,2.2,'python']
print(a)

a=[5,10,15,20,25,30,35,40]
print("a[2] is ",a[2])
print("a[0:3] is",a[0:3])
print("a[5:]",a[5:])


a=[1,2,3]
a[2]=4
print(a)

#python strings
s="this is a string"
print(s)
s='''this is a multiline
  string'''
print(s)

s='hello world'
print("s[4]",s[4])
print("s[6:11]",s[6:11])

#python set

a={5,2,3,1,4}
print("a = ",a)
print(type(a))

#python dictonary
a={1,1,2,2,3,3}
print(a)
d={1:'value','key':2}
print(type(d))

print("d[1]",d[1])
print("d['key']=",d['key'])

#conversion between data types
a=float(5)
print(a)
a=int(10.6)
print(a)
a=int(-10.6)
print(a)

a=set([1,2,3])
print(a)

a=tuple({5,6,7})
print(a)

a=list('hello')
print(a)

a=dict([[1,2],[3,4]])
print(a)
a=dict([(3,26),(4,44)])
print(a)

# get absolute value of a number
n=-20
print(abs(n))

n=-30.55
print(abs(n))

#len function
languages=['python','java','javascript']
length=len(languages)
print(length)

testlist=[]
print(testlist,'lenght is',len(testlist))

testtuple=(1,2,3)
print(testtuple,'lenght is',len(testtuple))

testrange=range(1,10)
print('lenght of',testrange,'is',len(testrange))

teststring=''
print('lenght of',teststring,'is',len(teststring))

testlist=[1,2,3]
testbyte=bytes(testlist)
print('lenght of',testbyte,'is',len(testbyte))

testdict={}
print(testdict,'length is',len(testdict))

testset=set()
print(testset,'length is',len(testset))

number=[2,4,5,44,55,66]
min_number=min(number)
print(min_number)

number=[3,4,56,78,99]
smallest_number=min(number)
print(smallest_number)

print(round(25))
print(round(23.5))
print(round(51.6))
print(round(2.665,2))
print(round(2.675,2))
print(round(2.765,2))

name1="python3"
print(name1.isalnum())
name2="python 3"
print(name2.isalnum())

string1="m2345onica"
print(string1.isalnum())
string2="m2345onica Gell22er"
print(string2.isalnum())
string3="@Monica"
print(string3.isalnum())