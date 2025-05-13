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
  player_score = 0
  computer_score = 0
  playing = True

  print('This is a Tic-Tac-Toe game and all of the instructions\n'
          'are just like a normal game of Tic-Tac-Toe but instead\n'
          'of writing the X, you just type in a number (1-9) to\n'
          'place the X left to right and it goes like that \n'
          'for each of the rows.')
  #This function actually asks the questions and puts the spots into the board

  while playing:
      board = [" " for _ in range(9)]
      current_player = "X"

      # Show current score and board positions
      print(f"\nSCORE - You: {player_score} | Computer: {computer_score}")
      print("\nBoard positions:")
      print_board([str(i) for i in range(9)])
      print("\nGame starting!")

      # Main game loop
      while True:
          print_board(board)
          print(f"Player {current_player}'s turn.")

          if current_player == "X":
              while True:
                  try:
                      move = int(input("Enter your move (1-9): "))-1
                      if 0 <= move <= 8 and board[move] == " ":
                          board[move] = current_player
                          break
                      else:
                          print("Invalid move. Try again.")
                  except ValueError:
                      print("Please enter a valid number between 1 and 9.")
          else:
              move = computer(board)
              board[move] = current_player
              print(f"Computer's move: {move+1}")
          
          if check_win(board,current_player):
             print_board(board)
             if current_player == "X":
                print('Congrats! You Win!')
                player_score += 1
             else:
                print('The Computer won!')
                computer_score+= 1
             print(f"SCORE - You: {player_score} | Computer: {computer_score}")
             break

          if " " not in board:
              print_board(board)
              print("\nIt's a tie!")
              print(f"SCORE - You: {player_score} | Computer: {computer_score}")
              break

          current_player = "O" if current_player == "X" else "X"

      # Ask to play again
      while True:
          play_again = input("\nDo you want to play again? (y/n): ").lower()
          if play_again in ['y', 'n']:
              playing = (play_again == 'y')
              break
          print("Please enter 'y' or 'n'")

  # Show final results
  print("\n=== FINAL SCORE ===")
  print(f"You: {player_score}")
  print(f"Computer: {computer_score}")
  if player_score > computer_score:
      print("🏆 Congratulations! You won more games!")
  elif computer_score > player_score:
      print("Better luck next time! The computer won more games.")
  else:
      print("It's a tie in the overall score!")
  return player_score
#Lastly this uses a specific name the computer knows to start the program at the play_game function
if __name__ == "__main__":
   play_game()