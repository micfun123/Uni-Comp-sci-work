import random

#take in inputes
line1 = "10 6 3"
already_done = 4
line3 = "4 1 6 4"

### The creating the scarf that all ready exists
line1 = line1.split()
scarf_let = line3.split()
scarf = []
for i in scarf_let:
    scarf.append(int(i))


stripes_to_create = int(line1[0])
colors_available = int(line1[1])
spacing = int(line1[2])


if colors_available <= spacing:
    print("impossible")
    exit(0)

if stripes_to_create > colors_available * 2:
    print("impossible")
    exit(0)

#Create the colour avalable and the used dictionary
colors = []
colors_used = dict()
for i in range(1, colors_available+1):
    colors.append(i)
    colors_used[i] = 2


#remove the colours we have all ready used
for i in scarf:
    if i in colors_used:
        colors_used[i] = colors_used[i] - 1

for i in range(stripes_to_create):
    colours_seen = []
    for fuck in range(len(scarf)-1, len(scarf) - spacing - 1, -1):
        colours_seen.append(scarf[fuck])

    available = []
    for key,value in colors_used.items():
        if value >0:
            available.append(key)

    for j in available:
        if j in colours_seen:
            available.pop(j)

    print(available)



#
# for i in range(stripes_to_create):
#     colors_seen = []
#     for j in range(len(scarf) - 1, len(scarf) - spacing - 1, -1):
#         colors_seen.append(scarf[j])
#
#
#     correct = 0
#     while not correct:
#         x = list(colors_used.values())
#         correct = random.choice(x)
#         if correct in colors_seen:
#             correct = 0
#     scarf.append(correct)
#     colors_used[correct] = colors_used[correct] - 1
#
# print(scarf)
#


