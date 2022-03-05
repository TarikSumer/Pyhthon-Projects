board = int(input("What Size Game GoPy?"))
tahta = []
for i in range(board):                  # we are creating an empty 2d list using for
    rows = []
    for j in range(board):
        rows.append(str((i * board) + j))
    tahta.append(rows)
def kazanma_kontrol_fonksiyonu():
    for i in range(board):
         if tahta[i].count('X') == len(tahta):   # horizontal X
            print("Winner: X")
            exit()
    for i in range(board):
        if tahta[i].count('O') == len(tahta):    # horizontal O
            print("Winner: O")
            exit()
    counter_x = 0
    for i in range(board):                       # diagonal left X
        if tahta[i][i] == "X":
            counter_x += 1
            if counter_x == board:
                print("Winner: X")
                exit()
    counter_o = 0
    for i in range(board):                       # diagonal left O
        if tahta[i][i] == "O":
            counter_o += 1
            if counter_o == board:
                print("Winner: O")
                exit()
    counter_diagonal_x = 0
    for i in range(board):                       # diagonal right x
        if tahta[board-i-1][i] == "X":
            counter_diagonal_x += 1
            if counter_diagonal_x == board:
                print("Winner: X")
                exit()
    counter_diagonal_o = 0
    for i in range(board):
        if tahta[board - i - 1][i] == "O":
            counter_diagonal_o += 1
            if counter_diagonal_o == board:
                print("Winner: O")
                exit()
    for i in range(board):                       # vertical x
        counter_x = 0
        for j in range(board):
            if tahta[j][i] == "X":
                counter_x +=1
        if counter_x == board:
            print("Winner: X")
            exit()
    for i in range(board):                       # vertical o
        counter_o = 0
        for j in range(board):
            if tahta[j][i] == "O":
                counter_o +=1
        if counter_o == board:
            print("Winner: O")
            exit()
def tahta_bastirma_fonksiyonu():    # we want to print our board with single function and trying to not overuse it
    for i in range(board):
        for j in range(board):
            print("{:^3}".format(tahta[i][j]) ,end=" ")
        print()
def birinci_oyuncunun_hamlesi():        # this function simply calls itself or the second one until returns a value
    sayi1 = int(input("Player 1 turn--> "))
    if sayi1 >= board ** 2 or sayi1 < 0:
        print("Please enter a valid number.")
        birinci_oyuncunun_hamlesi()     # recursion
    row_number = sayi1 // board
    column_number = sayi1 % board
    if tahta[row_number][column_number] == "O":
        print("The other player select this cell before.")
        tahta_bastirma_fonksiyonu()
        ikinci_oyuncunun_hamlesi()
    elif tahta[row_number][column_number] == "X":
        print("You have made this choice before.")
        tahta_bastirma_fonksiyonu()
        ikinci_oyuncunun_hamlesi()
    else:
        tahta[row_number][column_number] = "X"
        tahta_bastirma_fonksiyonu()
        kazanma_kontrol_fonksiyonu()
        ikinci_oyuncunun_hamlesi()
def ikinci_oyuncunun_hamlesi():         # only differ with the first function is it simply uses 'O' character
    sayi1 = int(input("Player 2 turn--> "))
    if sayi1 >= board ** 2 or sayi1 < 0:
        print("Please enter a valid number")
        ikinci_oyuncunun_hamlesi()
    row_number = sayi1 // board
    column_number = sayi1 % board
    if tahta[row_number][column_number] == "X":
        print("The other player select this cell before.")
        birinci_oyuncunun_hamlesi()
    elif tahta[row_number][column_number] == "O":
        print("You have made this choice before.")
        tahta_bastirma_fonksiyonu()
        birinci_oyuncunun_hamlesi()
    else:
        tahta[row_number][column_number] = "O"
        tahta_bastirma_fonksiyonu()
        kazanma_kontrol_fonksiyonu()
        birinci_oyuncunun_hamlesi()
tahta_bastirma_fonksiyonu()
birinci_oyuncunun_hamlesi()
