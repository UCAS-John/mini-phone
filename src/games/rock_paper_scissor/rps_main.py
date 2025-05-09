#Alishya Xavier, Profiecency test: Rock, Paper, Scissors
import random

def rps_main():
    print('''

 ______     ______     ______     __  __           ______   ______     ______   ______     ______           ______     ______     __     ______     ______     ______     ______     ______    
/\  == \   /\  __ \   /\  ___\   /\ \/ /          /\  == \ /\  __ \   /\  == \ /\  ___\   /\  == \         /\  ___\   /\  ___\   /\ \   /\  ___\   /\  ___\   /\  __ \   /\  == \   /\  ___\   
\ \  __<   \ \ \/\ \  \ \ \____  \ \  _"-.        \ \  _-/ \ \  __ \  \ \  _-/ \ \  __\   \ \  __<         \ \___  \  \ \ \____  \ \ \  \ \___  \  \ \___  \  \ \ \/\ \  \ \  __<   \ \___  \  
 \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\        \ \_\    \ \_\ \_\  \ \_\    \ \_____\  \ \_\ \_\        \/\_____\  \ \_____\  \ \_\  \/\_____\  \/\_____\  \ \_____\  \ \_\ \_\  \/\_____\ 
  \/_/ /_/   \/_____/   \/_____/   \/_/\/_/         \/_/     \/_/\/_/   \/_/     \/_____/   \/_/ /_/         \/_____/   \/_____/   \/_/   \/_____/   \/_____/   \/_____/   \/_/ /_/   \/_____/ 
                                                                                                                                                                                               
''')
    score = 0
    comp_score = 0
    while True:
        computer = ['rock', 'paper', 'scissors']
        user = input('Type in your choice(rock, paper, or scissors): ')
        computer_choice = random.choice(computer)
        print('The computer chose .......\n', computer_choice)
        if computer_choice == 'rock' and user == 'rock':
            print('This was a tie')
        elif computer_choice == 'rock' and user == 'paper':
            print('You won this round')
            score+=1
        elif computer_choice == 'rock' and user == 'scissors':
            print('The computer won this round')
            comp_score+=1
        elif computer_choice == 'paper' and user == 'paper':
            print('This was a tie')
        elif computer_choice == 'paper' and user == 'rock':
            print('The computer won this round')
            comp_score+=1
        elif computer_choice == 'paper' and user == 'scissors':
            print('You won this round.')
            score+=1
        elif computer_choice == 'scissors' and user == 'scissors':
            print('This is a tie.')
        elif computer_choice == 'scissors' and user == 'paper':
            print('The computer won this round')
            comp_score+=1
        elif computer_choice == 'scissors' and user == 'rock':
            print('You won this round,')
            score+=1
        else:
            print('That is not one of the options')
        
        choice = input('What would you like to do:\n1. Play again\n2. Exit\nChoice: ')
        if choice == '1':
            continue
        elif choice == '2':
            print('Your final score is:',score)
            print('The computers final score is:', comp_score)
            return score
        else:
            print('That is not an option')
            continue

if __name__ == "__main__":
    score = rps_main()
    print(score)