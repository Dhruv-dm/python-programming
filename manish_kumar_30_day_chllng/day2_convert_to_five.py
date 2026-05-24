'''
You are given an integer n. You need to convert all zeroes of n to 5. 
Input: n = 1004
Output: 1554
Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.
'''

n = 1004
st = str(n)

# ---------- approach 1 -----------


# Strings are immutable and do not allow character assignment
# so converting the string to lst for character assignment

lst = list(st)

for k in range(len(lst)): 
    if lst[k] == '0':
        lst[k] = '5'

res = ''.join(lst) # converting the list into string
result = int(res)
print(result)


# ---------- approach 2 -----------
# Concatinating the string

res = ''
for k in range(len(st)):
    if st[k] == '0':
       res += '5'
    else:
        res += st[k]

print(int(res))