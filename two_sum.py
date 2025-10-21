"""
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

while True:
    nums = []
    while True:
        num = input("Enter Num (Q to stop): ")
        try:
            num = int(num)
            nums.append(num)
        except ValueError:
            if num.strip().lower() == "q":
                break
            else:
                print("Not an Int")
    while True: 
        try:
            print(nums)
            target = int(input("Enter a Target: "))
            break
        except ValueError:
            print("Not an Int")

    for n1 in nums:
        for n2 in nums:
            if n1 + n2 == target:
                results = [n1, n2]
                break
            else:
                pass
    num1 = nums.index(results[1])
    if num1 == nums.index(results[0]):
        nums.remove(n2)
        num2 = nums.index(results[0]) + 1
    else:
        num2 = nums.index(results[0])

    print([num1, num2])
    print("")
