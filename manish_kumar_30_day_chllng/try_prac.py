s = 1004 
p = str(s)
res = ''
for i in range(len(p)):
    if p[i] != '0':
        res += p[i]
    else:
        res += '5'
print(res)