arr = [
    'xoooxxooox', 'xooooooooo', 'xooxxxooox', 'xoooxxoxox',
]

ships = 0


for i in range(len(arr)):
    print(arr[i])
    # arr[i] == 'xoooxxooox'
    # arr [i][j] == 'x'

    for j in range(len(arr[i])):
        #    i = rows     , j = columns
        #    i = [0, 3]   , j = [0, 9]

        if arr[i][j] == 'x':

            if i == (len(arr)-1) and j == (len(arr[0])-1):  # i and j max
                ships +=1

            elif i == (len(arr)-1):   # i max (last row)
                if arr[i][j+1] == 'x':
                    pass
                elif arr[i][j+1] != 'x':
                    ships +=1

            elif j == (len(arr[0])-1):   # j max (last column)
                if arr[i+1][j] == 'x':
                    pass
                elif arr[i+1][j] != 'x':
                    ships += 1

            elif i != (len(arr)-1) and j != (len(arr[0])-1):
                if arr[i][j+1] == 'x' or arr[i+1][j] == 'x':
                    pass


                elif arr[i][j+1] != 'x' and arr[i+1][j] != 'x':
                    ships += 1



print(ships)