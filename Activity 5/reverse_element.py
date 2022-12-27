#program to reverse every kth row in a list

#using for loop and enumerate function
list_7= [[1,2],[3,4],[4,5],
            [6,7],[7,8],[9,10]]
print(f"List = {list_7}")
k = 3   #number of the row to be reversed
res = []
for i,n in enumerate(list_7):  # i = index , n = elements
    if (i+1) % k == 0:   # checking for K multiple
        res.append(list(reversed(n)))    # reversing using reversed
    else:
        res.append(n)
print("After reversing 3rd row, List =",res)


#using list comprehension and enumerate function
list_7= [[1,2],[3,4],[4,5],
            [6,7],[7,8],[9,10]]
print(f"List = {list_7}")
k = 3   #number of the row to be reversed
res = [n[::-1] if (i + 1) % k == 0 else n for i,n in enumerate(list_7)]
print("After reversing 3rd row, List =",res)