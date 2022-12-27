#binary search
def binarySearch(l,num):
    low = 0   #starting index
    upper = len(l)-1   #ending index
    mid = 0   #intializing the middle to zero
    while low <= upper:   #iterating over the array
        mid = (upper + low) // 2   #finding the middle value
        if l[mid] < num:
            low = mid + 1

        elif l[mid] > num:
            upper = mid - 1

        else:
            return mid

#l = [6,20,30,40,50,60,70]    #sorted list
l = [22,43,16,89,6,40,70,1]   #unsorted list
l.sort()
num = 40

result = binarySearch(l,num)   #storing the number in reult
if (result != -1):
    print(f"{num} is present in list at index {result}")
else:
    print(f"{num} is not in the list")