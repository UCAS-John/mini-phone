import random

#This is the rock paper scissors game
def rps_main():
    print('''

 ______    _______  _______  ___   _    _______  _______  _______  _______  ______      _______  _______  ___   _______  _______  _______  ______    _______ 
|    _ |  |       ||       ||   | | |  |       ||   _   ||       ||       ||    _ |    |       ||       ||   | |       ||       ||       ||    _ |  |       |
|   | ||  |   _   ||       ||   |_| |  |    _  ||  |_|  ||    _  ||    ___||   | ||    |  _____||       ||   | |  _____||  _____||   _   ||   | ||  |  _____|
|   |_||_ |  | |  ||       ||      _|  |   |_| ||       ||   |_| ||   |___ |   |_||_   | |_____ |       ||   | | |_____ | |_____ |  | |  ||   |_||_ | |_____ 
|    __  ||  |_|  ||      _||     |_   |    ___||       ||    ___||    ___||    __  |  |_____  ||      _||   | |_____  ||_____  ||  |_|  ||    __  ||_____  |
|   |  | ||       ||     |_ |    _  |  |   |    |   _   ||   |    |   |___ |   |  | |   _____| ||     |_ |   |  _____| | _____| ||       ||   |  | | _____| |
|___|  |_||_______||_______||___| |_|  |___|    |__| |__||___|    |_______||___|  |_|  |_______||_______||___| |_______||_______||_______||___|  |_||_______|
                                                                                                                                                                          
''')
    #keeps track of the comp and users score
    score = 0
    comp_score = 0
    #This is the loop that keeps going if the user wants to play again
    while True:
        #The list that the random generator chooses from
        computer = ['rock', 'paper', 'scissors']
        #The options the user can type in
        user = input('Type in your choice(rock, paper, or scissors): ')
        #Randomly chooses from the list
        computer_choice = random.choice(computer)

        #All the different options for a win or tie etc.
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
        #Error Handling
        else:
            print('That is not one of the options')
        
        #The options fo the user to play again or exit
        choice = input('What would you like to do:\n1. Play again\n2. Exit\nChoice: ')
        if choice == '1':
            continue
        elif choice == '2':
            #Shows the user their final score and saves it to the personal score 
            print('Your final score is:',score)
            print('The computers final score is:', comp_score)
            return score
        #Error Handling
        else:
            print('That is not an option')
            continue


if __name__ == "__main__":
    score = rps_main()
    print(score)