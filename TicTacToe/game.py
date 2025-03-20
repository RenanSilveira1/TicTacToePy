import tkinter as tk
from tkinter import messagebox, simpledialog

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.player_x = None
        self.player_o = None
        self.scores = {"X": 0, "O": 0, "Draws": 0}
        self.show_main_menu()
        self.window.mainloop()

    def show_main_menu(self):
        """ Displays the main menu. """
        self.clear_window()
        tk.Label(self.window, text="Tic-Tac-Toe", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.window, text="Start Game", command=self.setup_players, width=20).pack(pady=5)
        tk.Button(self.window, text="Credits", command=self.show_credits, width=20).pack(pady=5)
        tk.Button(self.window, text="Exit", command=self.window.quit, width=20).pack(pady=5)

    def setup_players(self):
        """ Asks for player names. """
        self.player_x = simpledialog.askstring("Player X", "Enter name for Player X:") or "Player X"
        self.player_o = simpledialog.askstring("Player O", "Enter name for Player O:") or "Player O"
        self.scores = {"X": 0, "O": 0, "Draws": 0}
        self.start_new_game()

    def start_new_game(self):
        """ Starts a new match. """
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.create_game_board()

    def create_game_board(self):
        """ Creates the game board. """
        self.clear_window()
        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.window, text="", font=("Arial", 20), width=5, height=2, 
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

        self.label_turn = tk.Label(self.window, text=f"{self.player_x}'s Turn (X)", font=("Arial", 14))
        self.label_turn.grid(row=3, column=0, columnspan=3)

        self.label_score = tk.Label(self.window, text=self.get_score_text(), font=("Arial", 12))
        self.label_score.grid(row=4, column=0, columnspan=3)

    def make_move(self, index):
        """ Handles a move on the board. """
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg="blue" if self.current_player == "X" else "red")

            if self.check_winner():
                self.scores[self.current_player] += 1
                messagebox.showinfo("Game Over", f"{self.get_current_player_name()} wins!")
                self.ask_replay()
                return
            elif "" not in self.board:
                self.scores["Draws"] += 1
                messagebox.showinfo("Game Over", "It's a draw!")
                self.ask_replay()
                return

            self.switch_player()

    def switch_player(self):
        """ Switches the current player. """
        self.current_player = "O" if self.current_player == "X" else "X"
        self.label_turn.config(text=f"{self.get_current_player_name()}'s Turn ({self.current_player})")
        self.label_score.config(text=self.get_score_text())

    def check_winner(self):
        """ Checks if there is a winner. """
        win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                        (0, 4, 8), (2, 4, 6)]
        return any(self.board[a] == self.board[b] == self.board[c] != "" for a, b, c in win_patterns)

    def ask_replay(self):
        """ Asks if players want to play again, return to menu, or exit. """
        choice = messagebox.askquestion("Play Again", "Do you want to play again?\nYes: Play Again\nNo: Return to Menu")

        if choice == "yes":
            self.start_new_game()
        else:
            exit_choice = messagebox.askyesno("Exit", "Do you want to exit the game?\nYes: Exit\nNo: Return to Menu")
            if exit_choice:
                self.window.quit()
            else:
                self.reset_players()
                self.show_main_menu()


    def get_current_player_name(self):
        """ Returns the current player's name. """
        return self.player_x if self.current_player == "X" else self.player_o

    def get_score_text(self):
        """ Returns the scoreboard text. """
        return f"{self.player_x} (X): {self.scores['X']} | {self.player_o} (O): {self.scores['O']} | Draws: {self.scores['Draws']}"

    def show_credits(self):
        """ Displays the game credits. """
        messagebox.showinfo("Credits", "Developed by Renan Rubbo Silveira\nDate: March 19, 2025")

    def reset_players(self):
        """ Resets players when returning to the main menu. """
        self.player_x = None
        self.player_o = None

    def clear_window(self):
        """ Clears the window. """
        for widget in self.window.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    TicTacToe()
