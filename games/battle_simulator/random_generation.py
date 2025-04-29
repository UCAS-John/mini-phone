# Random generator

# Allows us to use the Faker library to be able to make fake/random information for the characters
from faker import Faker
import random

#Used to create faker objects which are used throughout a lot of code
faker = Faker()

# Function to generate a backstory with name, birthday, country, and job
def generate_backstory(name):
    birthday = faker.date_of_birth(minimum_age=18, maximum_age=100)  # Random birthday
    country = faker.country()  # Random country
    job = faker.job()  # Random job
    
    # The details for the backstory of each character
    backstory = f"{name} was born on {birthday} in {country}, currently working as a {job}."
    return backstory

# Function to generate a complete random character
def generate_character():
    name = faker.name()  # Generate the random character's name
    return {
        'name': name,
        'backstory': generate_backstory(name),  # Uses the name in the backstory
        'strength': random.randint(5, 15),  # Random stats
        'defense': random.randint(5, 15),
        'speed': random.randint(5, 15),
        'health': random.randint(20, 100),
        'xp': 0, 
        'level': 1  # Every character starts at level 1
    }

