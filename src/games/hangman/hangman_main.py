from faker import Faker

fake = Faker()

def word(score): #makes a random word and creates the crypted version to display amount of letters
    rand_word = fake.word().lower()
    wordy = list(rand_word)
    letters = ['_|' for _ in wordy]
    score = guesser(letters, wordy, score)
    return score

def guesser(letters, wordy, score): #This function is the actual game where the user guesses characters
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    while '_|' in letters and wrong_guesses < max_wrong:
        print('\nWord:', end=' ')
        for ch in letters:
            print(ch, end='')
        print(f"\nWrong guesses: {wrong_guesses}/{max_wrong}")
        
        ask = input("Guess a letter: ").lower()

        if not ask.isalpha() or len(ask) != 1: #Checks if theres any letter in the alphabet in ask
            print("Please enter a single alphabet letter.")
            continue

        if ask in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(ask)

        if ask in wordy:
            for i in range(len(wordy)):
                if wordy[i] == ask:
                    letters[i] = ask + '|'
        else:
            print("Incorrect guess.")
            wrong_guesses+=1

    if '_|' not in letters:
        print("\nCongratulations! You guessed the word correctly!" )
        score+=1
        print(f'your score is: ', score) 
        play= input("do you want to play again (y/n): ").lower()
        if play == 'yes' or play == 'y':
            word(score)
        elif play == 'no' or play == 'n':
            print("Thanks for playing! ")
            return score
        else:
            print("PICK A VALID INPUT. Exiting game...")
            return score
            


    else:
        print("\nLOSER!💀 You ran out of guesses. The word was:", end=' ')
        for ch in wordy:
            print(ch, end='')
        print(f'\nyour score is: ', score) 
        play= input("\nDo you want to play again (y/n): ").lower()
        if play == 'yes' or play == 'y':
            word(score)
        elif play == 'no' or play == 'n':
            print("Thanks for playing! ")
            return score

def main(): #Main user interface
    print("-----HANGMAN-----\n")
    score = 0
    while True:
        options = input("what would you like to do?\n1) play\n2) exit\n")
        if options == '1':
            score = 0
            score = word(score)
        elif options == '2':
            print('Please return back to the main menu to play different games')
            break
        else:
            print("Pick a valid choice.")
    return score

if __name__ == "__main__":
    main()
