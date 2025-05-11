import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import csv

# Paths for cookie image and data
COOKIE_IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "images", "cookie.png")
COOKIE_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "data", "cookies.csv")

class CookieClicker:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Cookie Clicker")
        self.cookies = 0
        self.cps = 0  # Cookies per second
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
        }

        # Load player data
        self.load_data()

        # GUI Setup
        self.setup_gui()

        # Start CPS update loop
        self.update_cookies_per_second()

    def setup_gui(self):
        """Set up the GUI components."""
        # Cookie Button with Image
        cookie_image = Image.open(COOKIE_IMAGE_PATH)
        cookie_image = cookie_image.resize((100, 100))  # Resize to 100x100 pixels
        cookie_image = ImageTk.PhotoImage(cookie_image)

        self.cookie_button = tk.Button(self.root, image=cookie_image, command=self.click_cookie)
        self.cookie_button.image = cookie_image  # Keep a reference to avoid garbage collection
        self.cookie_button.pack(pady=20)

        # Cookie Counter
        self.cookie_label = tk.Label(self.root, text=f"Cookies: {self.cookies}", font=("Arial", 16))
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
        """Add a button for purchasing a building."""
        building = self.buildings[building_name]
        button = tk.Button(
            self.buildings_frame,
            text=f"{building_name}\nCost: {building['cost']}\nCPS: {building['cps']}\nOwned: {building['count']}",
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
        """Handle cookie clicks."""
        self.cookies += 1
        self.update_cookie_label()

    def update_cookie_label(self):
        """Update the cookie counter label."""
        self.cookie_label.config(text=f"Cookies: {self.cookies}")

    def purchase_building(self, building_name):
        """Handle purchasing a building."""
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
        """Update the text on a building button."""
        building = self.buildings[building_name]
        building["button"].config(
            text=f"{building_name}\nCost: {building['cost']}\nCPS: {building['cps']}\nOwned: {building['count']}"
        )

    def update_cookies_per_second(self):
        """Update cookies based on CPS."""
        self.cookies += self.cps
        self.update_cookie_label()
        self.root.after(1000, self.update_cookies_per_second)

    def load_data(self):
        """Load player data from the CSV file."""
        if not os.path.exists(COOKIE_DATA_PATH):
            return

        with open(COOKIE_DATA_PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == self.username:
                    self.cookies = int(row["cookies"])
                    self.cps = int(row["cps"])
                    for building_name in self.buildings:
                        self.buildings[building_name]["count"] = int(row[building_name])
                    break

    def save_data(self):
        """Save player data to the CSV file."""
        data = []
        if os.path.exists(COOKIE_DATA_PATH):
            with open(COOKIE_DATA_PATH, "r") as file:
                reader = csv.DictReader(file)
                data = list(reader)

        # Update or add the current player's data
        updated = False
        for row in data:
            if row["username"] == self.username:
                row["cookies"] = self.cookies
                row["cps"] = self.cps
                for building_name in self.buildings:
                    row[building_name] = self.buildings[building_name]["count"]
                updated = True
                break

        if not updated:
            row = {"username": self.username, "cookies": self.cookies, "cps": self.cps}
            for building_name in self.buildings:
                row[building_name] = self.buildings[building_name]["count"]
            data.append(row)

        # Write data back to the CSV file
        with open(COOKIE_DATA_PATH, "w", newline="") as file:
            fieldnames = ["username", "cookies", "cps"] + list(self.buildings.keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def save_and_exit(self):
        """Save the game and exit."""
        self.save_data()
        self.root.destroy()

if __name__ == "__main__":
    username = input("Enter your username: ")
    root = tk.Tk()
    game = CookieClicker(root, username)
    root.mainloop()