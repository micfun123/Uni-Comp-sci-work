
f = open("01.in", "r")
line = f.readline().split()
cards=[]
cardstotal = []
for i in range(int(line[1])): 
    cards.append([])
    cardstotal.append(0)
    

print(cards)


lines = f.readlines()
for i in lines:
    i = i.lstrip("\n")
    i = i.split()
    cards[int(i[1]) -1 ].append(i[0])

cardnum = 0
for i in cards:
    for j in range(0,len(i),2):
        try:
            print(f"{i[j]} and {i[j+1]}")
            if int(i[j]) == int(i[j+1]):
                cardstotal[cardnum] = cardstotal[cardnum] + 100
            else:
                cardstotal[cardnum] = cardstotal[cardnum] + abs(int(i[j])-int(i[j+1]))
        except:
            print(f"{i[j]} There is only 1")
            cardstotal[cardnum] = cardstotal[cardnum] + 100
    cardnum = cardnum + 1
print(cardstotal)


