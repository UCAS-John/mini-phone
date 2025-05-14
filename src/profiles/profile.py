import pandas as pd 
import hashlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from manage import file

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "users.csv"))
SCORE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "scores.csv"))

def create_profile(username: str, password: str):
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Read the users CSV file
    try:
        data = pd.read_csv(PATH)
    except Exception as e:
        print(f"Error reading CSV file {PATH}: {e}")
        data = pd.DataFrame(columns=["username", "password"])

    # Check if the username already exists
    if username in data["username"].values:
        return f"Username '{username}' already exists."

    # Add the new user to the users DataFrame
    new_row = pd.DataFrame([{"username": username, "password": hashed_password}])
    data = pd.concat([data, new_row], ignore_index=True)

    # Read the scores CSV file
    try:
        score = pd.read_csv(SCORE_PATH)
    except Exception as e:
        print(f"Error reading CSV file {SCORE_PATH}: {e}")
        score = pd.DataFrame(columns=["username", "hangman", "number guessing", "rock paper scissors", "simon", "simple quiz", "tic tace toe"])

    # Initialize user scores
    new_scores = pd.DataFrame([{"username": username, "hangman": 0, "number guessing": 0, "rock paper scissors": 0, "simon": 0, "simple quiz": 0, "tic tace toe": 0}])
    score = pd.concat([score, new_scores], ignore_index=True)

    # Save the updated DataFrames back to their respective CSV files
    data.to_csv(PATH, index=False)
    score.to_csv(SCORE_PATH, index=False)

    return f"Profile for '{username}' created successfully."

def delete_profile(username: str):

    data = file.read_csv(PATH)
    score = file.read_csv(SCORE_PATH)

    if data is None:
        return
    if score is None:
        return
    if username not in data["username"].values:
        raise ValueError("Username does not exist.")
    
    data = data[data["username"] != username]
    score = score[score["username"] != username]

    file.save_csv(PATH, data)
    file.save_csv(SCORE_PATH, score)

    return f"Profile for {username} deleted successfully."

def login_profile(username: str, password: str):
    data = file.read_csv(PATH)

    if data is None:
        return False
    if username not in data["username"].values:
        raise ValueError("Username does not exist.")
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if hashed_password != data.loc[data["username"] == username, "password"].values[0]:
        raise ValueError("Incorrect password.")
    
    return f"Login successful for {username}."

if __name__ == "__main__":

    print(create_profile("rq", "test_password"))
    print(login_profile("rq", "test_password"))