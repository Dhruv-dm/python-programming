'''
Write a function to check whether a string is a palindrome or not.
Ignore:
Spaces, Uppercase/lowercase differences

Example
Input: "Madam"
Output: True
'''

input_stng = 'Madam'

def palindrome_chk(stng):
    chars = stng.replace(" ","").lower()

    left = 0
    right = len(chars) - 1

    while left < right:

        if chars[left] != chars[right]:
            return False  # used return as return stops the entire function immediately

        left += 1
        right -= 1

    return True

print(palindrome_chk(input_stng))
print(palindrome_chk('Okauii dookkeiiee'))
print(palindrome_chk('1221'))