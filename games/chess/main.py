import tkinter as tk
class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = []
        self.pieces = {}
        self.selected_piece = None
        self.create_board()
        self.initialize_pieces()

    def create_board(self):
        for row in range(8):
            row_list = []
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "gray"
                frame = tk.Frame(self.root, width=60, height=60, bg=color)
                frame.grid(row=row, column=col)
                frame.bind("<Button-1>", lambda event, r=row, c=col: self.on_square_click(r, c))
                row_list.append(frame)
            self.board.append(row_list)

    def initialize_pieces(self):
        # Place pawns
        for col in range(8):
            self.add_piece("♙", 1, col)
            self.add_piece("♟", 6, col)
        # Place rooks
        self.add_piece("♖", 0, 0)
        self.add_piece("♖", 0, 7)
        self.add_piece("♜", 7, 0)
        self.add_piece("♜", 7, 7)
        # Place knights
        self.add_piece("♘", 0, 1)
        self.add_piece("♘", 0, 6)
        self.add_piece("♞", 7, 1)
        self.add_piece("♞", 7, 6)
        # Place bishops
        self.add_piece("♗", 0, 2)
        self.add_piece("♗", 0, 5)
        self.add_piece("♝", 7, 2)
        self.add_piece("♝", 7, 5)
        # Place queens
        self.add_piece("♕", 0, 3)
        self.add_piece("♛", 7, 3)
        # Place kings
        self.add_piece("♔", 0, 4)
        self.add_piece("♚", 7, 4)

    def add_piece(self, piece, row, col):
        label = tk.Label(self.board[row][col], text=piece, font=("Arial", 24), bg=self.board[row][col].cget("bg"))
        label.pack(expand=True)
        self.pieces[(row, col)] = piece

    def on_square_click(self, row, col):
        if self.selected_piece:
            self.move_piece(row, col)
        elif (row, col) in self.pieces:
            self.select_piece(row, col)

    def select_piece(self, row, col):
        self.selected_piece = (row, col)
        label = self.board[row][col].winfo_children()[0]
        label.config(bg="yellow")

    def move_piece(self, row, col):
        old_row, old_col = self.selected_piece
        piece = self.pieces[(old_row, old_col)]

        if self.is_valid_move(piece, old_row, old_col, row, col):
            # Remove highlight from the selected piece
            label = self.board[old_row][old_col].winfo_children()[0]
            label.config(bg=self.board[old_row][old_col].cget("bg"))

            # Move the piece
            self.pieces.pop((old_row, old_col))
            self.pieces[(row, col)] = piece

            # Update the GUI
            label = self.board[old_row][old_col].winfo_children()[0]
            label.destroy()
            self.add_piece(piece, row, col)

        self.selected_piece = None

    def is_valid_move(self, piece, old_row, old_col, new_row, new_col):
        # Validate moves based on the type of piece
        if piece in ["♙", "♟"]:  # Pawn
            direction = 1 if piece == "♙" else -1
            start_row = 1 if piece == "♙" else 6
            if old_col == new_col:  # Move forward
                if (new_row - old_row == direction and (new_row, new_col) not in self.pieces) or \
                   (old_row == start_row and new_row - old_row == 2 * direction and (new_row, new_col) not in self.pieces):
                    return True
            elif abs(new_col - old_col) == 1 and new_row - old_row == direction:  # Capture diagonally
                if (new_row, new_col) in self.pieces:
                    return True
        elif piece in ["♖", "♜"]:  # Rook
            if old_row == new_row or old_col == new_col:
                if self.is_path_clear(old_row, old_col, new_row, new_col):
                    return True
        elif piece in ["♘", "♞"]:  # Knight
            if (abs(new_row - old_row), abs(new_col - old_col)) in [(2, 1), (1, 2)]:
                return True
        elif piece in ["♗", "♝"]:  # Bishop
            if abs(new_row - old_row) == abs(new_col - old_col):
                if self.is_path_clear(old_row, old_col, new_row, new_col):
                    return True
        elif piece in ["♕", "♛"]:  # Queen
            if old_row == new_row or old_col == new_col or abs(new_row - old_row) == abs(new_col - old_col):
                if self.is_path_clear(old_row, old_col, new_row, new_col):
                    return True
        elif piece in ["♔", "♚"]:  # King
            if max(abs(new_row - old_row), abs(new_col - old_col)) == 1:
                return True
        return False

    def is_path_clear(self, old_row, old_col, new_row, new_col):
        # Check if the path between two squares is clear
        step_row = (new_row - old_row) // max(1, abs(new_row - old_row)) if old_row != new_row else 0
        step_col = (new_col - old_col) // max(1, abs(new_col - old_col)) if old_col != new_col else 0
        current_row, current_col = old_row + step_row, old_col + step_col
        while (current_row, current_col) != (new_row, new_col):
            if (current_row, current_col) in self.pieces:
                return False
            current_row += step_row
            current_col += step_col
        return True


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()