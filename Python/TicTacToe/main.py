import random


def makePlay(board, player):
    playIndex = int(input("Please choose an index (1-9) "))

    while playIndex > 9 or playIndex < 0:
        playIndex = int(input("Sorry you chose an invalid number. Choose a number between 1 and 9. "))

    while board[playIndex - 1] == "X" or board[playIndex - 1] == "O":
        playIndex = int(input("Sorry, that spot is taken. Choose another spot. "))

    character = ""
    if player:
        character = "X"
    else:
        character = "O"

    board[playIndex - 1] = character
    printBoard(board)
    winner = checkGameBoardForWinner(board, False, "")
    if winner == "Player1" or winner == "Player2":
        print(f"\nCongrats {winner}! You won.")
        return True
    else:
        return False


def makeAiPlay(board, char):
    print("AiBot now playing.")
    num = -1
    attempts = 0
    while num == -1:
        if attempts >= 100:
            print("AiBot can't make a play!")
            break
        num = random.randint(0, 8)
        if board[num] == "X" or board[num] == "O":
            num = -1
        attempts += 1
    if num > -1:
        board[num] = char
        printBoard(board)
        winner = checkGameBoardForWinner(board, True, char)
        if winner == "AiBot":
            print("\nAiBot won the game! Sorry Player1...")
        elif winner == "Player1" or winner == "Player2":
            print(f"\nCongrats {winner}! You won.")
            return True
        else:
            return False


def checkGameBoardForWinner(board, ai, aiChar):
    chars = ["X", "O"]
    for route in possibleWins:
        for char in chars:
            if board[route[0]] == char and board[route[1]] == char and board[route[2]] == char:
                if (ai == True) and (aiChar == char):
                    return "AiBot"
                else:
                    if char == "X":
                        return "Player1"
                    elif char == "O":
                        return "Player2"
    return "None"


def printBoard(board):
    print(
        f"\n {board[0]} | {board[1]} | {board[2]} \n ---------- \n {board[3]} | {board[4]} | {board[5]}  \n "
        f"---------- \n {board[6]} | {board[7]} | {board[8]} \n")


def announceTurn(turn):
    if turn:
        print("It is player 1's turn.")
    else:
        print("It is player 2's turn.")


possibleWins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
