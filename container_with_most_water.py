height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
highest_num = 0
for i in height:
    if i > highest_num:
        last_num = highest_num
        highest_num = i
print(highest_num)
print(last_num)