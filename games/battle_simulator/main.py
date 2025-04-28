#Alishya Xavier, Battle Simulator


#These make it able for that main file to get the functions from many other files
from visualization import radar_chart
from data_analysis import analyze_characters
from random_generation import generate_character
from save_characters import save_characters
from load_characters import load_characters
from create_character import create_character
from display_characters import display_characters
from battle import battle

def main():
    # This is a list that stores all of the characters
    characters = []

    while True:
        # Lets the user input one of the options that keeps repeating until they exit
        print("\nWhat would you like to do?")
        print("1. Create a character manually")
        print("2. Generate a random character")  # New option for random generation
        print("3. Load characters from file")
        print("4. Save characters to a file")
        print("5. Display characters")
        print("6. Battle")
        print("7. Visualize a character's stats")  # New option for visualization
        print("8. Analyze character data")        # New option for analysis
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_character(characters)
        elif choice == '2':
            # Generates and adds a random character to the list
            random_character = generate_character()
            characters.append(random_character)
            #Displays to the user, the stats for the new character
            print(f"Random character '{random_character['name']}' created successfully!")
            print(f"Backstory: {random_character['backstory']}")
        elif choice == '3':
            # If it is an actual file then it will get the characters from it
            file_name = input("Enter file name to load: ")
            try:
                characters.extend(load_characters(file_name))
            except FileNotFoundError:
                print("That file has not been found. Pease check the file name and try again.")
        elif choice == '4':
            # If it is an actual file then it will save all of those characters to it
            file_name = input("Enter file name to save: ")
            try:
                save_characters(file_name, characters)
            except Exception:
                    print("That file has not been found. Please try again.")
        elif choice == '5':
            # Displays all of the characters
            display_characters(characters)
        elif choice == '6':
            # Takes two characters to battle
            battle(characters)
        elif choice == '7':
            # Visualizes a character's stats using Matplotlib
            char_name = input("Enter the character's name to visualize: ")
            character = next((char for char in characters if char['name'].lower() == char_name.lower()), None)
            if character:
                radar_chart(character)
            else:
                print("Character not found.")
        elif choice == '8':
            # Analyzes character data using Pandas
            if characters:
                analyze_characters(characters)
            else:
                print("No character data available for analysis.")
        elif choice == '9':
            # Exits the program
            print("Goodbye!")
            exit()
        else:
            # Error-Handling
            print("That is not an option. Try again...")

# This starts the whole program
if __name__ == "__main__":
    main()
