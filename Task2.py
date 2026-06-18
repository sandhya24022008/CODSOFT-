def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, is_max):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_max:
        best = -100
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best = max(best, score)
        return best
    else:
        best = 100
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best = min(best, score)
        return best

def best_move(board):
    best_score = -100
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move

board = [[" " for _ in range(3)] for _ in range(3)]

while True:
    print_board(board)

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter col (0-2): "))

    if board[row][col] != " ":
        print("Cell already taken!")
        continue

    board[row][col] = "X"

    if check_winner(board, "X"):
        print_board(board)
        print("You Win!")
        break

    if is_full(board):
        print_board(board)
        print("Draw!")
        break

    ai_row, ai_col = best_move(board)
    board[ai_row][ai_col] = "O"

    if check_winner(board, "O"):
        print_board(board)
        print("AI Wins!")
        break

    if is_full(board):
        print_board(board)
        print("Draw!")
        break
