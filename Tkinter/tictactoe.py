import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game board
board = [" " for _ in range(9)]
current_player = "X"

def check_winner():
    global current_player
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
        (0, 4, 8), (2, 4, 6)             # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return True
    return False

def is_draw():
    return all(space != " " for space in board)

def button_click(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player
    for i in range(9):
        board[i] = " "
        buttons[i].config(text=" ")
    current_player = "X"

# Create buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Reset button
reset_button = tk.Button(root, text="Reset", font=('normal', 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Start the main loop
root.mainloop()
