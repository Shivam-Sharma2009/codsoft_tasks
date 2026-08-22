# Tic-Tac-Toe AI using Minimax

board = [" "] * 9
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def show():
    print(f" {board[0]} | {board[1]} | {board[2]}\n---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}\n---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def winner():
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return "Tie" if " " not in board else None

def minimax(ai_turn):
    result = winner()
    if result:
        return 1 if result == "O" else -1 if result == "X" else 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if ai_turn else "X"
            scores.append(minimax(not ai_turn))
            board[i] = " "

    return max(scores) if ai_turn else min(scores)

def best_move():
    best_score, move = -2, None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score, move = score, i
    return move

print("Tic-Tac-Toe | You = X | AI = O")

while True:
    show()
    try:
        pos = int(input("Choose a position (1-9): ")) - 1
        if not 0 <= pos < 9 or board[pos] != " ":
            print("Choose an empty position from 1 to 9.")
            continue
    except ValueError:
        print("Please enter a number.")
        continue

    board[pos] = "X"
    result = winner()
    if result:
        show()
        print("You win!" if result == "X" else "It's a tie!")
        break

    move = best_move()
    board[move] = "O"
    print("AI chose:", move + 1)

    result = winner()
    if result:
        show()
        print("AI wins!" if result == "O" else "It's a tie!")
        break
