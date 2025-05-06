import random

#Working on it
#Alishya Xavier, TicTacToe project
import random

def print_board(board):
#This is the function that prints the tic tac toe board
  print(f" {board[0]} | {board[1]} | {board[2]} ")
  print("---+---+---")
  print(f" {board[3]} | {board[4]} | {board[5]} ")
  print("---+---+---")
  print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board, player):
#Checks all of the options for the user to win 
  winning_combinations = [[0, 1, 2],
                          [3, 4, 5],
                          [6, 7, 8],
                          [0, 3, 6],
                          [1, 4, 7],
                          [2, 5, 8],
                          [0, 4, 8],
                          [2, 4, 6]]
  for combo in winning_combinations:
      if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
          return True
  return False

def computer(board):
#This one gets the computers move randomly
  empty_spaces = [i for i in range(9) if board[i] == " "]
  return random.choice(empty_spaces)

def play_game():
  score = 0
  print('This is a Tic-Tac-Toe game and all of the instructions\nare just like a normal game of Tic-Tac-Toe but instead\nof writing the X, you just type in a number (0-8) to\nplace the X left to right and it goes like that \nfor each of the rows.')
#This function actually asks the questions and puts the spots into the board
  while True:
      
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        if current_player == "X":
            while True:
                move = int(input("Enter your move (0-8): "))
                if 0 <= move <= 8 and board[move] == " ":
                    board[move] = current_player
                    break
                else:
                    print("Invalid move. Try again.")
        else:
            move = computer(board)
            board[move] = current_player
            print(f"Computer's move: {move + 1}")

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            if current_player == 'X':
               score+=1
            else:
               #working on it
                break

        if " " not in board:
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

        #question = input('Do you want to keep playing ')

#Lastly this uses a specific name the computer knows to start the program at the play_game function
if __name__ == "__main__":
   play_game()

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
    play_game()