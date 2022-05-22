a1 = ' '
b1 = ' '
c1 = ' '
a2 = ' '
b2 = ' '
c2 = ' '
a3 = ' '
b3 = ' '
c3 = ' '

board = '\n  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3 + '\n'
print(board) 

moves = []

round = 1
while round < 10:
    if round % 2 == 0:
        active_player = "O"
    else:
        active_player = "X"
    cell = input("Player " + active_player + " chose your cell: ")
    if cell in moves:
        print('\nCell is already taken. Chose another cell.\n')
        continue
    if cell not in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']:
        print('\nInvalid cell. Chose another cell.\n')
        continue
    else:
        globals()[cell] = active_player
        
        # Game is declaring a winner if any move is in the below cells.

        if active_player in (a1 and b1 and c1) or active_player in (a2 and b2 and c2) or active_player in (a3 and b3 and c3) or active_player in (a1 and a2 and a3) or active_player in (b1 and b2 and b3) or active_player in (c1 and c2 and c3) or active_player in (a1 and b2 and c3) or active_player in (a3 and b2 and c1):
            board = '\n  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3 + '\n'
            print(board) 
            print("Player " + active_player + " wins!")
            break
        else:
            board = '\n  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3 + '\n'
            print(board)
            round += 1
            moves.append(cell)
            continue

