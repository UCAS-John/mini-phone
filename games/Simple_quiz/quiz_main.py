import os

import random

from faker import Faker
fake = Faker()
fake.name()
fake.address()
fake.text()

question_num = 0

"""ex: to remeber how to do the thing

for _ in range(10):
  print(fake.name())
  print(fake.text())"""

#def quetion_easy():

#def quetion_medium():

#def quetion_hard():

#def quetion_impossible():


def main():
    print("""
  .-')            _   .-')      _ (`-.              ('-.             .-')                            .-') _         ,-..-. .-')               .-') _              .-') _               .-') _  ,-.   
 ( OO ).         ( '.( OO )_   ( (OO  )           _(  OO)          .(  OO)                          (  OO) )       /  |\  ( OO )             (  OO) )            ( OO ) )             (  OO) ) |  \  
(_)---\_)  ,-.-') ,--.   ,--.)_.`     \ ,--.     (,------.        (_)---\_)   ,--. ,--.    ,-.-') ,(_)----.       '  .' ;-----.\  ,--. ,--.  /     '._       ,--./ ,--,'  .-'),-----. /     '._'.  ' 
/    _ |   |  |OO)|   `.'   |(__...--'' |  |.-')  |  .---'        '  .-.  '   |  | |  |    |  |OO)|       |       |  |  | .-.  |  |  | |  |  |'--...__)      |   \ |  |\ ( OO'  .-.  '|'--...__)|  | 
\  :` `.   |  |  \|         | |  /  | | |  | OO ) |  |           ,|  | |  |   |  | | .-')  |  |  |'--.   /        |  |  | '-' /_) |  | | .-')'--.  .--'      |    \|  | )/   |  | |  |'--.  .--'|  | 
 '..`''.)  |  |(_/|  |'.'|  | |  |_.' | |  |`-' |(|  '--.       (_|  | |  |   |  |_|( OO ) |  |(_/(_/   /         |  |  | .-. `.  |  |_|( OO )  |  |         |  .     |/ \_) |  |\|  |   |  |   |  | 
.-._)   \ ,|  |_.'|  |   |  | |  .___.'(|  '---.' |  .--'         |  | |  |   |  | | `-' /,|  |_.' /   /___       '  '. | |  \  | |  | | `-' /  |  |         |  |\    |    \ |  | |  |   |  |  .'  ' 
\       /(_|  |   |  |   |  | |  |      |      |  |  `---.        '  '-'  '-.('  '-'(_.-'(_|  |   |        |       \  | | '--'  /('  '-'(_.-'   |  |         |  | \   |     `'  '-'  '   |  |  |  /  
 `-----'   `--'   `--'   `--' `--'      `------'  `------'         `-----'--'  `-----'     `--'   `--------'        `-' `------'   `-----'      `--'         `--'  `--'       `-----'    `--'  `-'   """)

difficulty=input("what is the difficulty you would like for you quiz? (Easy = 1 , medium = 2, hard = 3, impossible = 4) ")

while True:
    if difficulty == "1":
        start = input(" you chose the easy level, this quiz is close note, internet and friend(s). press space and then enter when you are ready.")
        if start == " ":
            os.system('cls')

            #quiz part will go here
            print("easy")

            break

        else: print("brotha it ain't that hard to press space and enter. do it again!! ")

    elif start == "2":
        start = input(" you chose the medium level, this quiz is close note, internet and friend(s). press space and then enter when you are ready.")
        if start == " ":
            os.system('cls')
        else: print("brotha it ain't that hard to press space and enter. do it again!! ")

        #quiz part will go here
        print("medium")

        break

    elif start == "3":
        start = input(" you chose the hard level, this quiz is close note, internet and friend(s). press space and then enter when you are ready.")
        if start == " ":
            os.system('cls')
        else: print("brotha it ain't that hard to press space and enter. do it again!! ")

        #quiz part will go here
        print("hard")

        break
    elif start == "4":
        start = input(""" you chose the impossible level B T doub this one works a little diffrent the first line is the quetion the second is the first answer, third second answer etc. this quiz is close note, internet and friend(s).
                      press space and then enter when you are ready.""")
        if start == " ":
            os.system('cls')
        else: print("brotha it ain't that hard to press space and enter. do it again!! ")

        def impossible():
            while question_num <= 10:

                ans = random.randint(1,4)

                print("quetion:")
                print(fake.text())
                
                1="1"

                print("1:")
                print(fake.text())

                2="2"

                print("2:")
                print(fake.text())

                3="3"

                print("3:")
                print(fake.text())

                4="4"

                print("4:")
                print(fake.text())

                user_ans = input("sooo what do you think it is??")

                if user_ans == ans:
                    print("")
                
        

        break
    
    else:
        break

if __name__ == "__main__":
    main()