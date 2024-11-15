arr = [
    ['xoooxxooo'], ['xoooxxooo'], ['xoooxxooo'], ['xoooxxooo'], ['xoxoxxooo'],
]


def ship_counter(a_list):
    divided = []
    ships = 0
    for i in a_list:
        for j in str(*i):
            divided.append(j)


    for i in range(len(divided)-1):
        try:
            if str(divided[i]) == (divided[i+1]):
                divided.pop(i)

        except IndexError:
            pass


    for i in divided:
        if i == 'x':
            ships += 1
    return ships



print(ship_counter(arr))