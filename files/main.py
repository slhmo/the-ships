try:
    rows, columns = map(int, input('enter rows and columns').split())
except ValueError:
    print('wrong input try again.')
except NameError:
    print('wrong input try again.')

ships = 0
game_plain = []

def get_game_plain():
    row, column = 0, 0

    while row in range(rows):
        game_plain.append('')

        while column in range(columns):
            value = (input(': '))

            if value == 'x' or value == 'o':
                game_plain[row] += value
                column +=1

            else:
                print('wrong input, try again')

        row +=1
        column = 0


get_game_plain()


for i in range(len(game_plain)):
    print(game_plain[i])
    # arr[i] == 'xoooxxooox'
    # arr [i][j] == 'x'

    for j in range(len(game_plain[i])):
        #    i = rows     , j = columns
        #    i = [0, 3]   , j = [0, 9]

        if game_plain[i][j] == 'x':

            if i == (len(game_plain)-1) and j == (len(game_plain[0])-1):  # i and j max
                ships +=1

            elif i == (len(game_plain)-1):   # i max (last row)
                if game_plain[i][j+1] == 'x':
                    pass
                elif game_plain[i][j+1] != 'x':
                    ships +=1

            elif j == (len(game_plain[0])-1):   # j max (last column)
                if game_plain[i+1][j] == 'x':
                    pass
                elif game_plain[i+1][j] != 'x':
                    ships += 1

            elif i != (len(game_plain)-1) and j != (len(game_plain[0])-1):
                if game_plain[i][j+1] == 'x' and game_plain[i+1][j] == 'x':
                    print('wrong input.'
                          ' a ship can only be vertical or horizontal.')

                if game_plain[i][j+1] == 'x' or game_plain[i+1][j] == 'x':
                    pass


                elif game_plain[i][j+1] != 'x' and game_plain[i+1][j] != 'x':
                    ships += 1



print(ships)
