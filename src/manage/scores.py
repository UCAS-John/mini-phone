import os
from file import read_csv, save_csv
from typing import Literal
import pandas as pd

_TYPES = Literal["hangman", "number guessing", "rock paper scissors", "simon", "simple quiz", "tic tace toe"]

PATH = dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "scores.csv")

def save_score(username: str, game: _TYPES, score: int):
    data = read_csv(PATH)
    if data is None:
        data = pd.DataFrame(columns=["username", "hangman", "number guessing", "rock paper scissors", "simon", "simple quiz", "tic tace toe"])
    if game not in data.columns:
        raise ValueError(f"Game '{game}' is not a valid game type.")

def load_score(game: _TYPES):
    raise NotImplementedError("Loading scores is not implemented yet.")