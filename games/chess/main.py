import tkinter as tk

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = []
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
        self.pieces = {}
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
        self.pieces[(row, col)] = label

    def on_square_click(self, row, col):
        if self.selected_piece:
            self.move_piece(row, col)
        elif (row, col) in self.pieces:
            self.select_piece(row, col)

    def select_piece(self, row, col):
        self.selected_piece = (row, col)
        label = self.pieces[(row, col)]
        label.config(bg="yellow")

    def move_piece(self, row, col):
        old_row, old_col = self.selected_piece
        piece_label = self.pieces.pop((old_row, old_col))
        piece_label.pack_forget()
        piece_label.config(bg=self.board[row][col].cget("bg"))
        piece_label.pack(expand=True)
        self.pieces[(row, col)] = piece_label
        self.selected_piece = None

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()