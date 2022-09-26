#activity2

# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
# Using for loop
for i in list:
    print(i)
    

# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
 # getting length of list
length = len(list)
 # Iterating the index
# same as 'for i in range(len(list))'
for i in range(length):
  print(list[i])
  
# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
# Getting length of list
length = len(list)
i = 0
 # Iterating using while loop
while i < length:
    print(list[i])
    i += 1
    
# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
# Using list comprehension
[print(i) for i in list]

# Python code to iterate through all values in a dictionary
statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
 
keys = statesAndCapitals.keys()
print(keys)

#Python code to iterate through all keys in a dictionary
statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
 
print('List Of given states:\n')
 
# Iterating over keys
for state in statesAndCapitals:
    print(state)
    
# Python code to iterate through all values in a dictionary
statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
 
print('List Of given capitals:\n')
 
# Iterating over values
for capital in statesAndCapitals.values():
    print(capital)
    
# Python code to iterate through all key, value
# pairs in a dictionary
statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
 
print('List Of given states and their capitals:\n')
 
# Iterating over values
for state, capital in statesAndCapitals.items():
    print(state, ":", capital)

## Python code to iterate through all values in a dictionary
 
statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
 
for i in statesAndCapitals:
    print(i, '->', statesAndCapitals[i])

# Python code to iterate through all values in a dictionary
statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
 
keys = statesAndCapitals.items()
print(keys)