import os

import random

question_num = 0

from faker import Faker
fake = Faker()
fake.name()
fake.address()
fake.text()


def impossible(question_num, score):
                while question_num <= 10:

                    ans = random.randint(1,4)

                    print("quetion:")
                    print(ans)
                    print(fake.text())

                    print("1:")
                    print(fake.text())

                    print("2:")
                    print(fake.text())

                    print("3:")
                    print(fake.text())

                    print("4:")
                    print(fake.text())

                    while True:
                        user_ans = input("sooo what do you think it is?? (pick the number associate with the answer) ").strip()
                        if user_ans.isdigit():
                            user_ans = int(user_ans)
                            break
                        else:
                            print("bud, choose a number it ain't that hard. 😊")
                            continue


                    if user_ans == ans:
                        os.system('cls')
                        print("WOW!! you got it right!")
                        start = input("press space and then enter to continue.")
                        os.system('cls')
                        question_num +=1
                        score +=1
                    elif user_ans != ans:
                        os.system('cls')
                        print("well, thats not it but that's not very supprising.")
                        start = input("press space and then enter to continue.")
                        os.system('cls')
                        question_num +=1
                    
                        print("your score is: ", score)
                            
                        return score

def main():
    print("""

         _   .-')      _ (`-.                .-')     .-')           .-. .-')               ('-.             .-')                            .-') _  
        ( '.( OO )_   ( (OO  )              ( OO ).  ( OO ).         \  ( OO )            _(  OO)          .(  OO)                          (  OO) ) 
  ,-.-') ,--.   ,--.)_.`     \ .-'),-----. (_)---\_)(_)---\_)  ,-.-') ;-----.\  ,--.     (,------.        (_)---\_)   ,--. ,--.    ,-.-') ,(_)----.  
  |  |OO)|   `.'   |(__...--''( OO'  .-.  '/    _ | /    _ |   |  |OO)| .-.  |  |  |.-')  |  .---'        '  .-.  '   |  | |  |    |  |OO)|       |  
  |  |  \|         | |  /  | |/   |  | |  |\  :` `. \  :` `.   |  |  \| '-' /_) |  | OO ) |  |           ,|  | |  |   |  | | .-')  |  |  |'--.   /   
  |  |(_/|  |'.'|  | |  |_.' |\_) |  |\|  | '..`''.) '..`''.)  |  |(_/| .-. `.  |  |`-' |(|  '--.       (_|  | |  |   |  |_|( OO ) |  |(_/(_/   /    
 ,|  |_.'|  |   |  | |  .___.'  \ |  | |  |.-._)   \.-._)   \ ,|  |_.'| |  \  |(|  '---.' |  .--'         |  | |  |   |  | | `-' /,|  |_.' /   /___  
(_|  |   |  |   |  | |  |        `'  '-'  '\       /\       /(_|  |   | '--'  / |      |  |  `---.        '  '-'  '-.('  '-'(_.-'(_|  |   |        | 
  `--'   `--'   `--' `--'          `-----'  `-----'  `-----'   `--'   `------'  `------'  `------'         `-----'--'  `-----'     `--'   `--------' 
""")

    difficulty=input("you sure you want to take the impossible quiz?? (1 yes, 2 no) ")

    score = 0

    while True:
        
        if difficulty == "1":
            start = input(""" you chose the impossible level B T doub this one works a little diffrent the first line is the quetion the second is the first answer, third second answer etc. this quiz is close note, internet and friend(s).
                        press space and then enter when you are ready.""")
            if start == " ":
                score = impossible(question_num, score)
                os.system('cls')
                
                if start == " ":
                    os.system('cls')
                    print("your final score is: ", score)
                    end =input("press space and enter to reture to the Game selector.")
                    if end == " ":
                         return score

                else: print("brotha it ain't that hard to press space and enter. do it again!! ")


                break
            else: print("brotha it ain't that hard to press space and enter. do it again!! ")

        elif difficulty == "2":
            return score
        
        else:
             print("you need a real choise not whatever you put in.")

if __name__ == "__main__":
    score = main()