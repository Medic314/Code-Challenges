"""
Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
"""
# ----------------------------------------------------------------
"""
With Str():
"""

"""
while True:
    while True:
        try:
            num = int(input("Enter an integer: "))
            break
        except ValueError:
            print("Not an Integer")
    num_letters = list(str(num))
    num_letters2 = list(str(num))
    num_letters2.reverse()
    if num_letters == num_letters2:
        print(True)
    else:
        print(False)
"""
# ----------------------------------------------------------------
"""
Without str():
"""

def number_list(num):
    if num < 0:
        is_negative = True
    else:
        is_negative = False
    
while True:
    while True:
        try:
            num = int(input("Enter an integer: "))
            break
        except ValueError:
            print("Not an Integer")



            