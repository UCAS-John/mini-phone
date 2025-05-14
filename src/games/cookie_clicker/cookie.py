import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from manage.file import read_csv, save_csv
from manage.scores import save_score

# Paths for cookie image and data
# COOKIE_IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "images", "cookie.png"))
# print("COOKIE_IMAGE_PATH:", COOKIE_IMAGE_PATH)
# if not os.path.exists(COOKIE_IMAGE_PATH):
#     raise FileNotFoundError(f"Image file not found at: {COOKIE_IMAGE_PATH}")

# Cookie image keep not working i give up :( Use emoji 🍪 instead

COOKIE_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "data", "cookies.csv"))

class CookieClicker:
    def __init__(self, root, username):
        self.root = root
        self.username = str(username)
        self.root.title("Cookie Clicker")
        self.cookies = 0
        self.cps = 0  # Cookies per second use "cps" for easy and short
        self.buildings = {
            "Cursor": {"cost": 10, "cps": 1, "count": 0},
            "Grandma": {"cost": 100, "cps": 5, "count": 0},
            "Farm": {"cost": 500, "cps": 20, "count": 0},
            "Factory": {"cost": 3000, "cps": 100, "count": 0},
            "Mine": {"cost": 10000, "cps": 500, "count": 0},
            "Shipment": {"cost": 40000, "cps": 2000, "count": 0},
            "Alchemy Lab": {"cost": 200000, "cps": 10000, "count": 0},
            "Portal": {"cost": 1666666, "cps": 50000, "count": 0},
            "Time Machine": {"cost": 123456789, "cps": 1000000, "count": 0},
            "Antimatter Condenser": {"cost": 9876543210, "cps": 5000000, "count": 0},
            "Prism": {"cost": 123456789012, "cps": 10000000, "count": 0},
            "Chancemaker": {"cost": 987654321098, "cps": 50000000, "count": 0},
        }

        # Load player data
        self.load_data()

        # GUI Setup
        self.setup_gui()

        # Start CPS update loop
        self.update_cookies_per_second()

    def setup_gui(self):
        """Set up the GUI components."""
        # Cookie Button with Emoji
        self.cookie_button = tk.Button(
            self.root,
            text="🍪",  # Use the cookie emoji
            command=self.click_cookie,
            font=("Arial", 50),  # Set a large font size for the emoji
            bg="light yellow",  # Background color
            activebackground="gold",  # Background color when clicked
            relief="raised",  # Button style
            bd=5,  # Border width
            width=5,  # Button width
            height=2,  # Button height
        )
        self.cookie_button.pack(pady=20)

        # Cookie Counter
        self.cookie_label = tk.Label(self.root, text=f"Cookies: {self.cookies:,}", font=("Arial", 16))
        self.cookie_label.pack()

        # Buildings Frame
        self.buildings_frame = tk.Frame(self.root)
        self.buildings_frame.pack(pady=20)

        # Add building buttons
        for building_name in self.buildings:
            self.add_building_button(building_name)

        # Save and Exit Button
        self.save_button = tk.Button(self.root, text="Save and Exit", command=self.save_and_exit, font=("Arial", 14))
        self.save_button.pack(pady=10)

    def add_building_button(self, building_name):
        # Add a button for purchasing a building.
        building = self.buildings[building_name]
        button = tk.Button(
            self.buildings_frame,
            text=f"{building_name}\nCost: {building['cost']:,}\nCPS: {building['cps']:,}\nOwned: {building['count']}",
            command=lambda: self.purchase_building(building_name),
            font=("Arial", 12),
            width=20,
            height=4,
        )
        # Calculate row and column for grid placement
        index = list(self.buildings.keys()).index(building_name)
        row = index // 3  # 3 buttons per row
        col = index % 3
        button.grid(row=row, column=col, padx=10, pady=10)  # Add padding for spacing
        building["button"] = button

    def click_cookie(self):
        # Handle cookie clicks.
        self.cookies += 1
        self.update_cookie_label()

    def update_cookie_label(self):
        # Update the cookie counter label.
        self.cookie_label.config(text=f"Cookies: {self.cookies}")

    def purchase_building(self, building_name):
        # Handle purchasing a building.
        building = self.buildings[building_name]
        if self.cookies >= building["cost"]:
            self.cookies -= building["cost"]
            building["count"] += 1
            building["cost"] = int(building["cost"] * 1.15)  # Increase cost by 15%
            self.cps += building["cps"]
            self.update_cookie_label()
            self.update_building_button(building_name)
        else:
            messagebox.showwarning("Not Enough Cookies", f"You need {building['cost'] - self.cookies} more cookies!")

    def update_building_button(self, building_name):
        # Update the text on a building button.
        building = self.buildings[building_name]
        building["button"].config(
            text=f"{building_name}\nCost: {building['cost']}\nCPS: {building['cps']}\nOwned: {building['count']}"
        )

    def update_cookies_per_second(self):
        # Update cookies based on CPS.
        self.cookies += self.cps
        self.update_cookie_label()
        self.root.after(1000, self.update_cookies_per_second)

    def load_data(self):
        # Load player data from the CSV file.
        df = read_csv(COOKIE_DATA_PATH)  # Use the read_csv function

        if df is not None:
            df["username"] = df["username"].astype(str)  # Ensure all usernames are strings

        if df is None or self.username not in df["username"].values:
            # If the file doesn't exist, is empty, or the username doesn't exist, create a new account
            self.save_data()
            return

        # Load existing player data
        user_data = df[df["username"] == self.username].iloc[0]
        self.cookies = int(user_data["cookies"])
        self.cps = int(user_data["cps"])
        for building_name in self.buildings:
            self.buildings[building_name]["count"] = int(user_data[building_name])

    def save_data(self):
        # Save player data to the CSV file.
        # Create a dictionary for the current player's data
        player_data = {
            "username": self.username,
            "cookies": self.cookies,
            "cps": self.cps,
        }
        for building_name in self.buildings:
            player_data[building_name] = self.buildings[building_name]["count"]

        # Load existing data if the file exists
        df = read_csv(COOKIE_DATA_PATH)
        if df is None:
            # Create an empty DataFrame with the required columns
            df = pd.DataFrame(columns=["username", "cookies", "cps"] + list(self.buildings.keys()))

        # Ensure the username column is treated as a string
        if "username" in df.columns:
            df["username"] = df["username"].astype(str)

        # Check if the username exists in the DataFrame
        if self.username in df["username"].values:
            # Update the existing row for the username
            for key, value in player_data.items():
                df.loc[df["username"] == self.username, key] = value
        else:
            # Append a new row for the username
            df = pd.concat([df, pd.DataFrame([player_data])], ignore_index=True)

        # Save the updated DataFrame back to the CSV file
        save_csv(COOKIE_DATA_PATH, df)

    def save_and_exit(self):
        # Save the game data and exit the application.
        self.save_data()  # Save the player's data to the CSV file
        save_score(self.username, "cookie", self.cookies)
        self.root.destroy()  # Close the application window

if __name__ == "__main__":
    username = input("Enter your username: ")
    root = tk.Tk()
    game = CookieClicker(root, username)
    root.mainloop()