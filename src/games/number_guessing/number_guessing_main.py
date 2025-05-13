import random

# import num_gess_score as scores

# Rando mTemplate jus remove it
def main():

    score = 0
    rand_num = random.randint(1,1000)
    print("""

 ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ 
||N |||U |||M |||B |||E |||R |||       |||G |||U |||E |||S |||S |||I |||N |||G |||       |||G |||A |||M |||E |||! |||! |||! |||! ||
||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

""")
    
    print("welcome to the number guessing game this game is very simple you keep guessing numbers till you get the right one. (if you want to leave at any given point in time input done.)(the numbers are 1-1000)")
    #main for num guess
    while True:

        while True:
            try:
                num_guess=int(input("what is your guess for the number?? "))
                break
                #makes sure that the number that the user put in is a number
            except:
                print("bud, choose a number it ain't that hard. 😊")
                continue
        

        if num_guess == rand_num:
            print("you got it that was a one in a thousand chance. now you should go find the bible in the code. one of the magic numbers will print the whole bible.")
            print("your score was ",score)
            return score

            break
        #teams easter eggs
        elif num_guess == 123:
            print("I wish I could have put the bible here, the enitre thing.")
        elif num_guess == 429:
            print(""" IS that.. glitter on your lips?
                MMMM cherry flavoured... want a taste?
                    """)
        elif num_guess == 145:
            print("hatred does not cease by hatred, but only by love this is the eternal rule.")
        elif num_guess == 324:
            print("""King Julien - Maurice is right you can't run around like a footless chicken
                  Maurice - headless chichen you majesty
                  King Julien - uh no how's a chicken supposed to without a head
                  Maurice - how's it run around without feet?
                  King Julien - I'm not a chicken Maurice, WHY ARE YOU ASKING ME ALL THIS QUESTION??
                  Mort - Oh I hate it when mommy and daddy fight WAHHHHH...
                  """)
        elif num_guess > rand_num:
            print("your number is tooo high.")
            score += 1

        elif num_guess < rand_num:
            print("your number is too small")
            score += 1

if __name__ == "__main__":
    score = main()