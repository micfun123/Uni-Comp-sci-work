
x = input()
x = x.split()
row = int(x[0])
col = int(x[1])

words = []
for i in range(col):
    words.append(input())

y = input()
y = y.split()
row_pad = int(y[0])
col_pad = int(y[1])

lines = []
lines.append((row_pad * "."))

