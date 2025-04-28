import random

def main():

    def print_board(board):
        """Prints the Tic-Tac-Toe board."""
        for i in range(3):
            print(" | ".join(board[i * 3:(i + 1) * 3]))
            if i < 2:
                print("-" * 9)
        print()

    def check_winner(board, mark):
        """Checks if a player has won."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(board[i] == mark for i in condition) for condition in win_conditions)

    def tic_tac_toe():
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        available_moves = set(board)
        
        print("Welcome to Tic-Tac-Toe!")
        print_board(board)

        while True:
            # Human move
            while True:
                human_move = input("Enter your move (1-9): ")
                if human_move in available_moves:
                    break
                print("Invalid move. Try again.")

            board[int(human_move) - 1] = 'X'
            available_moves.remove(human_move)
            print_board(board)

            if check_winner(board, 'X'):
                print("You won!")
                return "Tic-Tac-Toe", "Player"

            if not available_moves:
                print("It's a draw!")
                return "Tic-Tac-Toe", "Draw"

            # Computer move
            computer_move = random.choice(list(available_moves))
            print(f"Computer chose: {computer_move}")
            board[int(computer_move) - 1] = 'O'
            available_moves.remove(computer_move)
            print_board(board)

            if check_winner(board, 'O'):
                print("Computer won!")
                return "Tic-Tac-Toe", "Computer"

if __name__ == "__main__":
    main()