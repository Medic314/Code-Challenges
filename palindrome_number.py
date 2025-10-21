"""
Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
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
