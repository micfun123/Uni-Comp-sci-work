x = int(input())
lines = []
for i in range(x):
    word = input()
    if "leg" in word:
        lines.append("🦵")
    elif "rest" in word:
        lines.append("😁")
    else:
        lines.append("💪")

monthly = lines * (31 // x)
try:
    remainder = 31 - (31 // x) * 4
    for i in range(remainder):
        monthly.append(lines[i])
except:
    pass

day1 = ""
day2= ""
day3 = ""
day4 = ""
day5 = ""

counter = 0

for i in range(0,7):
    day1 = day1 + str(monthly[i])

for i in range(7,14):
    day2 = day2 + str(monthly[i])

for i in range(14,21):
    day3 = day3 + str(monthly[i])

for i in range(21,28):
    day4 = day4 + str(monthly[i])

for i in range(28,31):
    day5 = day5 + str(monthly[i])

print("1" + day1)
print("2" + day2)
print("3" + day3)
print("4" + day4)
print("5" + day5)
