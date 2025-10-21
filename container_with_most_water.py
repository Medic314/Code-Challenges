"""
Container with Most Water Challenge
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
-    eg. in the example below, the coordinates of the two red lines are (1,0) to (1, 8) and (8,0) and (8,7)

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
"""

while True:
    heights = [1,8,6,2,5,4,8,3,7]
    while True:
        num = input("Enter Num (Q to stop): ")
        try:
            num = int(num)
            heights.append(num)
        except ValueError:
            if num.strip().lower() == "q":
                break
            else:
                print("Not an Int")

    highest_num = 0
    for i in heights:
        if i > highest_num:
            highest_num = i
    point1 = [highest_num, heights.index(highest_num)+1]
    
    heights.remove(highest_num)

    print(heights)
    highest_num = 0
    for i in heights:
        if i > highest_num:
            highest_num = i
    point2 = [highest_num, heights.index(highest_num)+2]
    print(point1)
    print(point2)