import pandas as pd 
import hashlib
from manage import file
import os

path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "users.csv")

def create_profile(username: str, password: str):
    data = file.read_csv()