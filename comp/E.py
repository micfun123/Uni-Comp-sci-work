
num_of_people = 11
heights = "3 6 12 7 7 7 6 8 10 5 5"
heights_str = heights.split()
height = []
for i in heights_str:
    height.append(int(i))

i = 1
counter = 1
cost_modifier = 0
cost = 0
temp = len(height)
while i < temp:
    print(height)
    print(height[i], height[i-1])
    if height[i] < height[i-1]:
        print("a")
        height.remove(i)
        cost_modifier +=1
    else:
        cost_modifier = 0
    cost += cost_modifier ** 2
    i += 1
    temp = len(height)
    print(cost)


print(cost)


# cost = 0
# remaining = []
# counter = 0
# index_to_remove = []
#
# i = 1
# while i < num_of_people:
#     if height[i] > height[i-1]:
#         remaining.append(height[i-1])
#         cost = cost + (counter ** 2)
#     else:
#         index_to_remove.append(i-1)
#         counter =+ 1
#     i = i +1

# print(remaining)
# print(index_to_remove)

