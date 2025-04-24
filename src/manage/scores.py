import os
from file import read_csv, save_csv
from typing import Literal

_TYPES = Literal["hangman", "number guessing", "rock paper scissors", "simon", "simple quiz", "tic tace toe"]

PATH = dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "scores.csv")

def save_score(game: _TYPES, score: int):
    data = {"score": [score]}
    save_csv(PATH, data)

def load_score(game: _TYPES):
    raise NotImplementedError("Loading scores is not implemented yet.")