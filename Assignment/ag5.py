import chess
import chess.svg

def print_board(board):
    print(board)

def get_move():
    move = input("Enter your move (e.g., 'e2e4'): ")
    try:
        chess.Move.from_uci(move)
        return move
    except ValueError:
        print("Invalid move. Please enter a move in UCI format (e.g., 'e2e4').")
        return get_move()

def main():
    board = chess.Board()

    while not board.is_game_over():
        print_board(board)

        if board.turn == chess.WHITE:
            print("White's turn")
        else:
            print("Black's turn")

        move = get_move()

        if chess.Move.from_uci(move) in board.legal_moves:
            board.push(chess.Move.from_uci(move))
        else:
            print("Invalid move. Try again.")

    print("Game Over")
    print("Result: {}".format(board.result()))

if __name__ == "__main__":
    main()
