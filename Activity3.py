import string
# ACTIVITY NO. 3
# A. count the no. of alphabets in the given string
#  method 1:
test_str = 'geeksforgeeks!!$isbest4allGeeks10-0'
print("The original string is:" + str(test_str))
res = len([ele for ele in test_str if ele.isalpha()])
print("Count of Alphabets:" + str(res))

# method 2:


test_str = 'geeksforgeeks!!$isbest4allGeeks10-0'
print("The original string is:" + str(test_str))
res = len([ele for ele in test_str if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
print("Count of Alphabets:" + str(res))

# b. check if the string is alphanumeric or not
# example 1
string = "abc123"
print(string.isalnum())

# example 2 : isalnum() in if..else statement
password = "user123456"
if password.isalnum():
    print("password is alphanumric.")
else:
    print("password is not alphanumeric.")