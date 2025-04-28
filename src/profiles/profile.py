import pandas as pd 
import hashlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from manage import file

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "users.csv"))

def create_profile(username: str, password: str):
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Read the CSV file
    try:
        data = pd.read_csv(PATH)
    except Exception as e:
        print(f"Error reading CSV file {PATH}: {e}")
        data = pd.DataFrame(columns=["username", "password"])

    # Check if the username already exists
    if username in data["username"].values:
        return f"Username '{username}' already exists."

    # Add the new user
    new_row = pd.DataFrame([{"username": username, "password": hashed_password}])
    data = pd.concat([data, new_row], ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    data.to_csv(PATH, index=False)
    return f"Profile for '{username}' created successfully."

def delete_profile(username: str):

    data = file.read_csv(PATH)

    if data is None:
        return
    if username not in data["username"].values:
        raise ValueError("Username does not exist.")
    
    data = data[data["username"] != username]

    file.save_csv(data, PATH)

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
    print(create_profile("test_user", "test_password"))
    print(login_profile("test_user", "test_password"))