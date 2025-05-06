import os

def main():
    print("""
  _________.__               . __           ________        .__             ___ __________        __     _______          __    ___    
 /   _____/|__| _____ ,______ |  |   ____   \_____  \  __ __|__|_______    /  / \______   \__ ___/  |_   \      \   _____/  |_  \  \   
 \_____  \ |  |/     \,\____ \|  | _/ __ \   /  / \  \|  |  \  \___   /   /  /   |    |  _/  |  \   __\  /   |   \ /  _ \   __\  \  \  
 /        \|  |  Y Y  \|  |_> >  |_\  ___/  /   \_/.  \  |  /  |/    /   (  (    |    |   \  |  /|  |   /    |    (  <_> )  |     )  ) 
/_______  /|__|__|_|  /|   __/|____/\___  > \_____\ \_/____/|__/_____ \   \  \   |______  /____/ |__|   \____|__  /\____/|__|    /  /  
        \/          \/,|__|             \/         \__>              \/    \__\         \/                      \/              /__/   """)

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