'''
You are given an integer n. You need to convert all zeroes of n to 5. 
Input: n = 1004
Output: 1554
Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.
'''

n = 1004
st = str(n)
lst= []

for i in st:
    lst.append(i)

for k in range(len(lst)):
    if lst[k] == '0':
        lst[k] = '5'

res = ''.join(lst)
result = int(res)
print(result)