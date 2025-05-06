import os

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
        start = input(" you chose the easy level, this quiz is close note, internet and friend. press space and then enter when you are ready.")
        if start == " ":
            os.system('cls')

            #quiz part will go here

            break

        else: print("brotha it ain't that hard to press space and enter. do it again!! ")

    elif start == "2":
        start = input(" you chose the easy level, this quiz is close note, internet and friend. press space and then enter when you are ready.")
        if start == " ":
            os.system('cls')
        else: print("brotha it ain't that hard to press space and enter. do it again!! ")

        #quiz part will go here

        break

    elif start == "3":
        start = input(" you chose the easy level, this quiz is close note, internet and friend. press space and then enter when you are ready.")
        if start == " ":
            os.system('cls')
        else: print("brotha it ain't that hard to press space and enter. do it again!! ")

        #quiz part will go here

        break
    
    else:
        break

if __name__ == "__main__":
    main()