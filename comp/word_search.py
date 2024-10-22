from operator import truediv

search_size=input()
search_size = search_size.split()
search_x=int(search_size[0])
search_y=int(search_size[1])

search_array = []
for i in range(search_y):
    search_array.append(str(input()))

whole_size=input()
whole_size=whole_size.split()
whole_x=int(whole_size[0])
whole_y=int(whole_size[1])

whole_array = []
for i in range(whole_y):
    whole_array.append(str(input()))

y=0
temp_y=y
cont= True

