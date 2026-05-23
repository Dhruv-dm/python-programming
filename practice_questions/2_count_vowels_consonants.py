'''
Write a program to count:
Total vowels and Total consonants in a given string.
Example
Input: "DataEngineer"

Output:
Vowels = 6
Consonants = 6
'''

input_str = "DataEngineer"

def cnt_vowle_consonent(strg):

    vowel = 0
    consonent = 0

    for char in strg:
        if char.lower() in ('a','e','i','o','u'):
            vowel += 1
        elif char.isalpha() :  # character must be alphabet not spaces, numbers, special characters
            consonent += 1
    
    print(f'Vowels = {vowel}')
    print(f'Consonants = {consonent}')

cnt_vowle_consonent(input_str)

st = '@5T ime$'
cnt_vowle_consonent(st)