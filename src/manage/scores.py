import os
from manage.file import read_csv, save_csv
from typing import Literal
import pandas as pd

_TYPES = Literal["hangman", "number guessing", "rock paper scissors", "simon", "simple quiz", "tic tace toe"]

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "scores.csv"))

def save_score(username: str, game: _TYPES, score: int):
    data = read_csv(PATH)
    if data is None:
        data = pd.DataFrame(columns=["username", "hangman", "number guessing", "rock paper scissors", "simon", "simple quiz", "tic tace toe"])
    if game not in data.columns:
        raise ValueError(f"Game '{game}' is not a valid game type.")

    data.loc[data["username"] == username, game] = score

    save_csv(PATH, data)

def load_score(username, game: _TYPES):
    data = read_csv(PATH)
    if data is None:
        return None
    if game not in data.columns:
        data = pd.DataFrame(columns=["username", "hangman", "number guessing", "rock paper scissors", "simon", "simple quiz", "tic tace toe"])

    data = data[data["username"] == username]

    if data.empty:
        return None
    return data.iloc[0][game]

if __name__ == "__main__":
    save_score("test_user", "hangman", 100)
    print(load_score("test_user", "hangman"))