'''
Given a string S, write a program to count the occurrence of Lowercase characters, 
Uppercase characters, Special characters and Numeric values in the string.
'''
s = "#GeeKs01fOr@gEE ks07"

def count(st):

    upper_cnt = 0
    lower_cnt = 0
    special_cnt = 0
    numeric_cnt = 0

    for char in st:
        if char == ' ':
            pass
        elif ord(char)>=65 and ord(char)<=90:
            upper_cnt += 1
        elif ord(char)>=97 and ord(char)<=122:
            lower_cnt += 1
        elif ord(char)>=48 and ord(char)<=57:
            numeric_cnt += 1
        else:
            special_cnt += 1

    return upper_cnt, lower_cnt, numeric_cnt, special_cnt
    
print(count(s))