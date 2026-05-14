#  Reverse a String
# Write a function to reverse a string without using slicing ([::-1]).
# Example
# Input: "python"
# Output: "nohtyp"

input_string = "python"


# --------using the slicing logic-----------
output = input_string[::-1]
print(output)

# ----------using loop logic---------------
def reverse_string(input_string):
    reversed_string = ''

    for i in range(len(input_string)-1,-1,-1):
        reversed_string += input_string[i]  #concatenation
    
    print(reversed_string)

reverse_string(input_string)

'''Concept-> Understand the Range Function
             range(start, stop, step)
             range(5, -1, -1)
               - Start from 5
               - Go till before -1
               - Move backward by -1
 '''

# --------using Two Pointer Swapping Approach--------

def reverser_two_pointer_swapping(input_string):
    chars = list(input_string)

    # Defining Two points
    left = 0
    right = len(input_string) - 1

    while left < right:

        # Swapping the characters in the list
        chars[left],chars[right] = chars[right],chars[left]

        left += 1
        right -= 1

    result = "".join(chars)
    print(result)
    
reverser_two_pointer_swapping(input_string)