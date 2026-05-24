'''
Given an array arr[]. The task is to find the largest element and return it.
'''
arr = [1, 8, 7, 56, 90]
arr2= [100,25,96,78,9]

def greatest_num(lst):

    num = 0

    for digit in lst:
        if digit > num:
            num = digit
        else:
            continue
    return num

print(greatest_num(arr))
print(greatest_num(arr2))