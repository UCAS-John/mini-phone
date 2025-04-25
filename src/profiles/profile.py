import pandas as pd 
import hashlib
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "manage")))
from manage import file

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "users.csv"))

def create_profile(username: str, password: str):
    data = file.read_csv(PATH)

    if data is None:
        data = pd.DataFrame(columns=["username", "password"])
    if username in data["username"].values:
        raise ValueError("Username already exists.")
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    data = data.append({"username": username, "password": hashed_password}, ignore_index=True)

    file.save_csv(data, PATH)

    return f"Profile for {username} created successfully."

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
    print("\n".join(sys.path))
    print(create_profile("test_user", "test_password"))
    print(login_profile("test_user", "test_password"))