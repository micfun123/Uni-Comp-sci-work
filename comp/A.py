word1 = input()
word2 = input()
word1_dict = dict()
word2_dict = dict()

for i in word1:
    if i not in word1_dict:
        word1_dict[i] = 1
    else:
        word1_dict[i] = word1_dict[i] + 1

for i in word2:
    if i not in word2_dict:
        word2_dict[i] = 1
    else:
        word2_dict[i] = word2_dict[i] + 1

word1_pops = []

for key, value in word1_dict.items():
    if key in word2:
        if value < word2_dict[key]:
            word1_pops.append(key)
        elif word2_dict[key] < value:
            word2_dict.pop(key)
        else:
            word2_dict.pop(key)


for i in word1_pops:
    word1_dict.pop(i)

word = ""
for key, value in word1_dict.items():
    word = word + key * value

for key, value in word2_dict.items():
    word = word + key * value

print(word)

