import random

#Working on it
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
  print('''
___    __           ___       __           ___  __   ___ 
 |  | /  `    __     |   /\  /  `    __     |  /  \ |__  
 |  | \__,           |  /--\ \__,           |  \__/ |___ 

        ''')
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
<<<<<<< HEAD

if __name__ == "__main__":
    play_game()
=======
if __name__ == "__main__":
   play_game()
>>>>>>> 42ebbf421ef1b32b4bc906b09c8ebe5fdd3a00b2
