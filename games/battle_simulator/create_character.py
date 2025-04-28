# Create Character

#ADDITIONAL FEATURE WITH FAKER(random skill and weapon)
# This is needed for the random skill and weapon given to each character
from faker import Faker

faker = Faker()

# This is an inner function that creates a new character.
def create_character(characters):
    try:
        # This gets the user's input for the details of the character
        name = input("Enter character name: ").strip().lower()
        # Checks if the name already exists
        if any(char['name'] == name for char in characters):
            print("A character with this name already exists. Choose a different name.")
            return
        # Set maximum values for each of the stats
        max_health = 200
        max_strength = 50
        max_defense = 30
        max_speed = 100

        # Informs the user the most the stats can be
        print(f"Health can be a maximum of {max_health}.")
        health = int(input("Enter health: "))
        if health > max_health:
            print(f"Health cannot exceed {max_health}. Please try again.")
            return

        print(f"Strength can be a maximum of {max_strength}.")
        strength = int(input("Enter strength: "))
        if strength > max_strength:
            print(f"Strength cannot exceed {max_strength}. Please try again.")
            return

        print(f"Defense can be a maximum of {max_defense}.")
        defense = int(input("Enter defense: "))
        if defense > max_defense:
            print(f"Defense cannot exceed {max_defense}. Please try again.")
            return

        print(f"Speed can be a maximum of {max_speed}.")
        speed = int(input("Enter speed: "))
        if speed > max_speed:
            print(f"Speed cannot exceed {max_speed}. Please try again.")
            return

        # This adds the character to the list with all of the stats
        character = {
            'name': name,
            'health': health,
            'strength': strength,
            'defense': defense,
            'speed': speed,
            'xp': 0,
            'level': 1
        }
        
        #IF I HAD MORE TIME TO IMPROVE THE CODE, I WOULD MAKE THESE EFFECT THE CHARACTERS DURING BATTLE
        # Assign a random weapon and skill using Faker
        character['weapon'] = faker.word()
        character['skill'] = faker.catch_phrase()

        # Add the character to the list
        characters.append(character)

        # Lets the user know their character has been made with a weapon and skill(Doesn't do anything to stats but just gives additional backround)
        
        print(f"Character '{name}' created successfully with weapon: {character['weapon']} and skill: {character['skill']}!")
    except ValueError:
        # If they type in not the right format for the stats
        print("That is not a valid option.")
