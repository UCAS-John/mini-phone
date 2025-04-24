import os
from file import read_csv, save_csv
import pandas as pd

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "cookies.csv")

def save_cookie_data(data):
    cookie_path = os.path.join(PATH, "cookie_clicker", "cookie.csv")
    save_csv(cookie_path, data)
    
def load_cookie_data():
    cookie_path = os.path.join(PATH, "cookie_clicker", "cookie.csv")