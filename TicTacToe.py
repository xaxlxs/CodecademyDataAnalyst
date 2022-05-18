a1 = ' '
b1 = ' '
c1 = ' '
a2 = ' '
b2 = ' '
c2 = ' '
a3 = ' '
b3 = ' '
c3 = ' '

board = '  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3
print(board) 

round = 1
while round < 10:
    if round % 2 == 0:
        active_player = "O"
    else:
        active_player = "X"
    print("Player " + active_player + " chose your cell.")
    cell = input()
    if cell != " ":
        print("Chose another cell.")
        continue
    else:
        cell = active_player
        if active_player in (a1 and b1 and c1):
            board = '  a   b   c ' + '\n1 ' + a1 + ' | '+ b1 + ' | ' + c1 + '\n ---|---|---' + '\n2 ' + a2 + ' | '+ b2 + ' | ' + c2 + '\n ---|---|---' + '\n3 ' + a3 + ' | '+ b3 + ' | ' + c3
            print(board) 
            print("Player " + active_player + " wins!")
            break
        else:
            print(board)
            continue
        round += 1





'''
Psudo:
check which player is active (counter)
ask player for their move
if requested square != ' ' ask to pick again (loop)
increment counter
set requested square to player's character
check for winner





'''