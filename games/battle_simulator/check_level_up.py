# Check Level Up

# This is a function that checks if a character has leveled up
def check_level_up(character):
    # Checks if the characters xp is higher or the same as the xp can be
    if int(character['xp']) >= 50:
        # This takes away 50 xp and makes them a level higher
        character['xp'] = int(character['xp']) - 50
        character['level'] = int(character['level']) + 1

        # This is what happens to that characters stats when they level up
        character['health'] += 10
        character['strength'] += 2
        character['defense'] += 1
        character['speed'] += 1
        #Lets the user know that character is at a certain level
        print(f"{character['name']} leveled up to Level {character['level']}!")