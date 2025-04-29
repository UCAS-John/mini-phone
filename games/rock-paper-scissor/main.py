#Alishya Xavier, Profiecency test: Rock, Paper, Scissors
import random

def main():
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
        
        choice = input('What would you like to do:\n1. Play again\n2. Display top 5 scores\n3. Exit\nChoice: ')
        #Add it to all of the profiles who have used the phone
        if choice == 'y':
            print('Your final score is:',score)
            print('The computers final score is:', comp_score)
            break
        else:
            continue
    return score
