#Load Characters

import csv
# This is a function that loads characters from a csv file
def load_characters(file_name):
    try:
        with open(file_name, mode='r') as file:
            # This makes the characters into lists inside the dictionary
            characters = list(csv.DictReader(file))
            # This converts the stats into int
            for char in characters:
                char['health'] = int(char['health'])
                char['strength'] = int(char['strength'])
                char['defense'] = int(char['defense'])
                char['speed'] = int(char['speed'])
                char['xp'] = int(char['xp'])
                char['level'] = int(char['level'])
            return characters
    except FileNotFoundError:
        # This is what happens if the file isn't found
        print(f"File '{file_name}' has not been found.")
        return []