a1 = ' '
b1 = ' '
c1 = ' '
a2 = ' '
b2 = ' '
c2 = ' '
a3 = ' '
b3 = ' '
c3 = ' '

winning_moves = [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3], [a1, a2, a3], [b1, b2, b3], [c1, c2, c3], [a1, b2, c3], [a3, b2, c1]]

board = '\n  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3 + '\n'
print(board) 

o_moves = []
x_moves = []

cell = ''

# Ask user for input, check validity, return user's choice
def get_input():
    cell = input("Player " + active_player + " chose your cell: ")
    if cell in o_moves or cell in x_moves:
        print('\nCell is already taken. Chose another cell.\n')
        get_input()
    if cell not in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']:
        print('\nInvalid cell. Chose another cell.\n')
        get_input()
    return cell

# Set user's choice cell to active player's character, append to player's list of moves, print board
def write_board(cell, active_player):
    globals()[cell] = active_player
    if active_player == 'X':
        x_moves.append(cell)
    else:
        o_moves.append(cell)
    print(board)

# Check if the active player has won the game
def check_win(active_player):
    if active_player == 'X':
        for moves in winning_moves:
            for move in moves:
                if move in x_moves:
                    continue
                else:
                    break
                print('\nPlayer X wins!\n')
                exit
    else:
        for moves in winning_moves:
            for move in moves:
                if move in o_moves:
                    continue
                else:
                    break
                print('\nPlayer O wins!\n')
                exit


# WRITE_BOARD IS NOT UPDATING THE BOARD BEFORE PRINTING IT
# MOVES ARE NOT BEIGN ADDED TO THE PLAYER'S MOVES LIST


round = 1
while round < 10:
    if round % 2 == 0:
        active_player = "O"
    else:
        active_player = "X"
    get_input()
    write_board(cell, active_player)
    check_win(active_player)
    round += 1
    print(x_moves, o_moves)
    print(a1)
print('\nStalemate.')










# ORIGINAL VERSION

# round = 1
# while round < 10:
#     if round % 2 == 0:
#         active_player = "O"
#     else:
#         active_player = "X"
#     cell = input("Player " + active_player + " chose your cell: ")
#     if cell in moves:
#         print('\nCell is already taken. Chose another cell.\n')
#         continue
#     if cell not in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']:
#         print('\nInvalid cell. Chose another cell.\n')
#         continue
#     else:
#         globals()[cell] = active_player
        
#         # Game is declaring a winner if any move is in the below cells.

#         if active_player in (a1 and b1 and c1) or active_player in (a2 and b2 and c2) or active_player in (a3 and b3 and c3) or active_player in (a1 and a2 and a3) or active_player in (b1 and b2 and b3) or active_player in (c1 and c2 and c3) or active_player in (a1 and b2 and c3) or active_player in (a3 and b2 and c1):
#             board = '\n  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3 + '\n'
#             print(board) 
#             print("Player " + active_player + " wins!")
#             break
#         board = '\n  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3 + '\n'
#         print(board)
#         round += 1
#         moves.append(cell)
#         continue
# print('\nStalemate')




# ALTERNATE VERSIONS

#         for moves in winning_moves:
#             for move in moves:
#                 if move != active_player:
#                     break
#                 else:
#                     board = '\n  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3 + '\n'
#                     print(board) 
#                     print("Player " + active_player + " wins!")
#                     break
#         board = '\n  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3 + '\n'
#         print(board)
#         round += 1
#         moves.append(cell)
#         continue
# print('\nStalemate')


#         for moves in winning_moves:
#             for move in moves:
#                 if move == active_player:
#                     continue
#                 else:
#                     break
#                 board = '\n  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3 + '\n'
#                 print(board) 
#                 print("Player " + active_player + " wins!")
#                 break
#         board = '\n  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3 + '\n'
#         print(board)
#         round += 1
#         moves.append(cell)
#         continue
# print('\nStalemate')
