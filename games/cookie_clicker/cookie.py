import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import pandas as pd
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from main import app

# Paths for images and data
COOKIE_IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "images", "cookie.png")
COOKIE_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "cookies.csv")

# Building data
BUILDINGS = [
    {"name": "Cursor", "cost": 15, "cps": 0.1},
    {"name": "Grandma", "cost": 100, "cps": 1},
    {"name": "Farm", "cost": 1100, "cps": 8},
    {"name": "Factory", "cost": 12000, "cps": 47},
    {"name": "Mine", "cost": 130000, "cps": 260},
    {"name": "Shipment", "cost": 1400000, "cps": 1400},
    {"name": "Alchemy Lab", "cost": 20000000, "cps": 7800},
    {"name": "Portal", "cost": 166000000, "cps": 44000},
    {"name": "Time Machine", "cost": 1230000000, "cps": 260000},
    {"name": "Antimatter Condenser", "cost": 31000000000, "cps": 1600000},
    {"name": "Prism", "cost": 750000000000, "cps": 10000000},
]

class CookieClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookie Clicker")
        self.root.geometry("800x600")
        self.current_user = app.current_user

        # Game state
        self.cookies = 0
        self.cps = 0
        self.buildings = {building["name"]: {"count": 0, "cost": building["cost"], "cps": building["cps"]} for building in BUILDINGS}

        # Load saved data
        self.load_data()

        # UI setup
        self.create_ui()

        # Start the CpS loop
        self.update_cookies_per_second()

    def create_ui(self):
        # Create the user interface.

        # Cookie display
        self.cookie_label = tk.Label(self.root, text=f"Cookies: {self.cookies:.1f}", font=("Arial", 20))
        self.cookie_label.pack(pady=10)

        # Cookie button
        # image = Image.open(COOKIE_IMAGE_PATH)
        # self.cookie_photo = ImageTk.PhotoImage(image)
        # self.cookie_button = tk.Button(self.root, image=self.cookie_photo, command=self.click_cookie)
        # self.cookie_button.image = self.cookie_photo  # Prevent garbage collection
        # self.cookie_button.pack(side="top", pady=10)

        # Buildings frame
        self.buildings_frame = tk.Frame(self.root)
        self.buildings_frame.pack(pady=20)

        # Create building buttons
        for building in BUILDINGS:
            frame = tk.Frame(self.buildings_frame)
            frame.pack(pady=5)

            name_label = tk.Label(frame, text=building["name"], font=("Arial", 14))
            name_label.pack(side="left", padx=10)

            cost_label = tk.Label(frame, text=f"Cost: {self.buildings[building['name']]['cost']}", font=("Arial", 12))
            cost_label.pack(side="left", padx=10)

            count_label = tk.Label(frame, text=f"Owned: {self.buildings[building['name']]['count']}", font=("Arial", 12))
            count_label.pack(side="left", padx=10)

            button = tk.Button(frame, text="Buy", command=lambda b=building: self.buy_building(b["name"]))
            button.pack(side="left", padx=10)

            # Save references for updating
            self.buildings[building["name"]]["cost_label"] = cost_label
            self.buildings[building["name"]]["count_label"] = count_label

    def click_cookie(self):
        """Handle cookie clicks."""
        self.cookies += 1
        self.update_cookie_display()

    def buy_building(self, building_name):
        """Buy a building."""
        building = self.buildings[building_name]
        if self.cookies >= building["cost"]:
            self.cookies -= building["cost"]
            building["count"] += 1
            building["cost"] = int(building["cost"] * 1.15)  # Increase cost by 15%
            self.cps += building["cps"]

            # Update UI
            self.update_cookie_display()
            building["cost_label"].config(text=f"Cost: {building['cost']}")
            building["count_label"].config(text=f"Owned: {building['count']}")
        else:
            messagebox.showerror("Not Enough Cookies", f"You need {building['cost'] - self.cookies:.1f} more cookies to buy {building_name}.")

    def update_cookie_display(self):
        """Update the cookie count display."""
        self.cookie_label.config(text=f"Cookies: {self.cookies:.1f}")

    def update_cookies_per_second(self):
        # Update cookies based on CpS.
        self.cookies += self.cps / 10  # Update every 0.1 seconds
        self.update_cookie_display()
        self.root.after(100, self.update_cookies_per_second)

    def save_data(self):
        # Save the game state to a CSV file.
        data = {
            "username": [self.current_user],
            "cookies": [self.cookies],
            "cps": [self.cps],
        }
        for building_name, building in self.buildings.items():
            data[f"{building_name}_count"] = [building["count"]]
            data[f"{building_name}_cost"] = [building["cost"]]

        df = pd.DataFrame(data)
        df.to_csv(COOKIE_DATA_PATH, index=False)

    def load_data(self):
        # Load the game state from a CSV file.
        if os.path.exists(COOKIE_DATA_PATH):
            try:
                df = pd.read_csv(COOKIE_DATA_PATH)
                self.cookies = df["cookies"][0]
                self.cps = df["cps"][0]
                for building_name in self.buildings.keys():
                    self.buildings[building_name]["count"] = int(df[f"{building_name}_count"][0])
                    self.buildings[building_name]["cost"] = int(df[f"{building_name}_cost"][0])
            except Exception as e:
                print(f"Error loading data: {e}")

    def on_close(self):
        # Handle the window close event.
        self.save_data()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = CookieClicker(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)  # Save data on close
    root.mainloop()