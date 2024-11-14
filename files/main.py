arr = [
    ['xoooxxooooxxoxxo']
]
divided = []

for i in arr:
    for j in str(*i):
        divided.append(j)


for i in range(len(divided)-1):
    try:
        if str(divided[i]) == (divided[i+1]):
            divided.pop(i)

    except:pass

print(divided)