import random

# Rando mTemplate jus remove it
def main():
    print("""

 ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ 
||N |||U |||M |||B |||E |||R |||       |||G |||U |||E |||S |||S |||I |||N |||G |||       |||G |||A |||M |||E |||! |||! |||! |||! ||
||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

""")
    
    print("welcome to the number guessing game this game is very simple you keep guessing numbers till you get the right one. (if you want to leave at any given point in time input done.)")

    while True:

        rand_num = random.randint(1,1000)

        num_guess=("what is your guess for the number?? ")

        if num_guess == rand_num:
            print("you got it that was a one in a million chance. now you should go find the bible in the code. one of the magic numbers will print the whole bible.")

        elif num_guess == 429:
            print("bible goes here")
        elif num_guess == 62:
            print("Lord Faraad")
        elif num_guess == 145:


if __name__ == "__main__":
    main()