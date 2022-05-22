from random import randint

# Comp Moves:   1:Rock   2:Paper   3:Scisors

while True:
    comp_move = randint(1,3)

    print('Select your move: rock, paper or scisors?')
    move = input()

    if move != 'rock' and move != 'paper' and move != 'scisors':
        print('Try again...')
        continue

    if move == 'rock':
        if comp_move == 1:
            print("It's a tie.")
            continue
        if comp_move == 2:
            print('Paper covers rock. Better luck next time.')
            continue
        else:
            print('Rock smashes scisors! Great job!')
            continue

    if move == 'paper':
        if comp_move == 2:
            print("It's a tie.")
            continue
        if comp_move == 1:
            print('Paper covers rock! Great job!')
            continue            
        if comp_move == 3:
            print('Scisors cut paper. Better luck next time.')
            continue

    if move == 'scisors':
        if comp_move == 3:
            print("It's a tie.")
            continue
        if comp_move == 1:
            print('Rock smashes scisors. Better luck next time.')
            continue
        if comp_move == 2:
            print('Scisors cut paper! Great job!')
            continue