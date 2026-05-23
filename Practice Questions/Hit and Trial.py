arr = [1,2,3,4,5]
lst = []
def alternate_num(arry):
    for i in range(len(arry)):
        if i%2 == 0:
            lst.append(arry[i])
    print(lst)

alternate_num(arr)