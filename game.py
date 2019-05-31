from board import Board
from computer import Computer


if __name__ == '__main__':
    print("Let's play tic tac toe game")
    board = Board()
    computer = Computer(board)

    while not board.has_winner():
        print("Make your move:")
        move = input("Type your move in format XxY: ")
        while not (len(move.split("x")) == 2 and all(
                map(lambda x: x.isdigit() and 1 <= int(x) <= 3, move.split("x")))):
            move = input("\nType your move in format XxY: ")
        x, y = list(map(int, move.split("x")))
        made = board.make_move((x - 1, y - 1))
        if board.has_winner():
            break

        if made:
            print(board)
            computer.make_move()
            print("Computer's move:\n")
            print(board)

    if board.has_winner() == board.CROSS_WINNER:
        print("Congrats! You won!")
    elif board.has_winner() == board.NOUGHT_WINNER:
        print("You lost!")
    else:
        print("It's a draw")
