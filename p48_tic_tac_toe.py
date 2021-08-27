game = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
turn = 1

while turn <= 9:
    if turn % 2 == 0:
        pos = int(input("Player2 Enter your position:"))
        game[pos-1] = 'O'
    else:
        pos = int(input("Player1 Enter your position:"))
        game[pos - 1] = 'X'

    print(game[0], " | ", game[1], " | ", game[2])
    print(game[3], " | ", game[4], " | ", game[5])
    print(game[6], " | ", game[7], " | ", game[8])

    # winning condition:

    if game[0] == game[1] and game[1] == game[2]:
        if game[0] == 'X':
            print("Player1 wins")
            turn = 10
        elif game[0] == 'O':
            print("Player2 wins")
            turn = 10

    if game[3] == game[4] and game[3] == game[5]:
        if game[3] == 'X':
            print("Player1 wins")
            turn = 10
        elif game[3] == 'O':
            print("Player2 wins")
            turn = 10

    if game[6] == game[7] and game[6] == game[8]:
        if game[6] == 'X':
            print("Player1 wins")
            turn = 10
        elif game[6] == 'O':
            print("Player2 wins")
            turn = 10

    if game[0] == game[3] and game[0] == game[6]:
        if game[0] == 'X':
            print("Player1 wins")
            turn = 10
        elif game[0] == 'O':
            print("Player2 wins")
            turn = 10

    if game[1] == game[4] and game[1] == game[7]:
        if game[1] == 'X':
            print("Player1 wins")
            turn = 10
        elif game[1] == 'O':
            print("Player2 wins")
            turn = 10

    if game[2] == game[5] and game[2] == game[8]:
        if game[2] == 'X':
            print("Player1 wins")
            turn = 10
        elif game[2] == 'O':
            print("Player2 wins")
            turn = 10

    if game[0] == game[4] and game[0] == game[8]:
        if game[0] == 'X':
            print("Player1 wins")
            turn = 10
        elif game[0] == 'O':
            print("Player2 wins")
            turn = 10

    if game[2] == game[4] and game[2] == game[6]:
        if game[0] == 'X':
            print("Player1 wins")
            turn = 10
        elif game[0] == 'O':
            print("Player2 wins")
            turn = 10

    elif turn == 9:
        print("Draw")

    turn += 1