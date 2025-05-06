
from faker import Faker

fake = Faker()
rand_word = fake.word().lower()

def word(rand_word):
    score = 0
    wordy = list(rand_word)
    letters = ['_|' for _ in wordy]
    while True:
        guesser(letters, wordy, score)

def guesser(letters, wordy, score):
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    while '_|' in letters and wrong_guesses < max_wrong:
        print('\nWord:', end=' ')
        for ch in letters:
            print(ch, end='')
        print(f"\nWrong guesses: {wrong_guesses}/{max_wrong}")
        
        ask = input("Guess a letter: ").lower()

        if not ask.isalpha() or len(ask) != 1:
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
            wrong_guesses += 1

    if '_|' not in letters:
        print("\nCongratulations! You guessed the word correctly!" )

    else:
        print("\nLOSER!💀 You ran out of guesses. The word was:", end=' ')
        for ch in wordy:
            print(ch, end='')
        print()


word(rand_word)