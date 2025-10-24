"""
Container with Most Water Challenge
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
-    eg. in the example below, the coordinates of the two red lines are (1,0) to (1, 8) and (8,0) and (8,7)

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
"""

while True:
    heights = []
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
    max_area = 0
    for h1 in range(len(heights)):
        for h2 in range(len(heights)):
            if heights[h1] > heights[h2]:
                lowest_point = heights[h2]
                highest_index = h1 +1
                lowest_index = h2 +1
            if heights[h1] < heights[h2]:
                lowest_point = heights[h1]
                highest_index = h2 +1
                lowest_index = h1 +1
            if heights[h1] == heights[h2]:
                lowest_point = heights[h1]
                highest_index = h2 +1
                lowest_index = h1 +1

            index_range = abs(highest_index - lowest_index)

            area = lowest_point * index_range
            if  area > max_area:
                max_area = area
                max_lowest_point = lowest_point
                max_highest_index = highest_index
                max_lowest_index = lowest_index
                max_index_range = index_range
    print(max_area)

            
            
            