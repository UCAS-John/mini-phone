import os
from manage.file import read_csv, save_csv
from typing import Literal
import pandas as pd

_TYPES = Literal["hangman", "number guessing", "rock paper scissors", "simon", "simple quiz", "tic tac toe", "cookie"]

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "scores.csv"))

def save_score(username: str, game: _TYPES, score: int):
    data = read_csv(PATH)
    if data is None:
        data = pd.DataFrame(columns=["username", "hangman", "number guessing", "rock paper scissors", "simon", "simple quiz", "tic tac toe", "cookie"])
    if game not in data.columns:
        raise ValueError(f"Game '{game}' is not a valid game type.")

    if not data.loc[data["username"] == username, game].empty:
        current_score = data.loc[data["username"] == username, game].iloc[0]  # Get the first matching value
        if current_score > score:
            pass
        else:
            data.loc[data["username"] == username, game] = score
        if game == "cookie":
            data.loc[data["username"] == username, game] = score

    # print(PATH)
    save_csv(PATH, data)

def load_score(username, game: _TYPES):
    data = read_csv(PATH)
    if data is None:
        return None
    if game not in data.columns:
        data = pd.DataFrame(columns=["username", "hangman", "number guessing", "rock paper scissors", "simon", "simple quiz", "tic tac toe", "cookie"])

    data = data[data["username"] == username]

    if data.empty:
        return None
    return data.iloc[0][game]

def load_all(username):
    data = read_csv(PATH)
    if data is None:
        return None
    data = data[data["username"] == username]
    if data.empty:
        return None
    return data.iloc[0].to_dict()

def load_top(n=5):
    data = read_csv(PATH)
    if data is None:
        return None
    top_scores = {}
    for game in data.columns[1:]:
        if game != 'username':
            # Sort by score in descending order, handle NaN values, and select top n
            sorted_data = data.sort_values(by=[game], ascending=False, na_position='last')
            top_scores[game] = list(zip(sorted_data.head(n)["username"], sorted_data.head(n)[game]))
    return pd.DataFrame.from_dict(top_scores, orient='index').transpose()

# if __name__ == "__main__":
    
    # data = read_csv(PATH)
    # print(data.to_string())
    # data = load_top()
    # print(data.to_string())

    # save_score("1", "rock paper scissors", 21)
