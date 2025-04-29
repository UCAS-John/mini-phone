import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import subprocess
from profiles.profile import create_profile, delete_profile, login_profile
from manage.scores import load_all

# Paths for images and game scripts
IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
GAMES_SCRIPTS = {
    "Battle Simulator": os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "games", "battle_simulator", "main.py"),
    "Cookie Clicker": os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "games", "cookie_clicker", "main.py"),
    "Hangman": os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "games", "Hangman", "main.py"),
    "Number Guessing": os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "games", "number_guessing", "main.py"),
    "Rock Paper Scissors": os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "games", "rock_paper_scissors", "main.py"),
    "Simon Game": os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "games", "simon", "main.py"),
    "Simple Quiz": os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "games", "Simple_quiz", "main.py"),
    "Tic Tac Toe": os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', "games", "Tic_Tac_Toe", "main.py")
}

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Launcher")
        self.root.geometry("1200x800")
        self.current_user = None

        # Initialize UI
        self.login_screen()

    def login_screen(self):
        """Create the login screen."""
        self.clear_screen()

        tk.Label(self.root, text="Login", font=("Arial", 20, "bold")).pack(pady=20)

        tk.Label(self.root, text="Username:", font=("Arial", 14)).pack()
        self.username_entry = tk.Entry(self.root, font=("Arial", 14))
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", font=("Arial", 14)).pack()
        self.password_entry = tk.Entry(self.root, font=("Arial", 14), show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", font=("Arial", 14), command=self.login).pack(pady=10)
        tk.Button(self.root, text="Create Profile", font=("Arial", 14), command=self.create_profile_screen).pack(pady=10)

    def main_menu(self):
        """Create the main menu after login."""
        self.clear_screen()

        tk.Label(self.root, text=f"Welcome, {self.current_user}!", font=("Arial", 20, "bold")).pack(pady=20)

        # Create game buttons
        for game_name, script_path in GAMES_SCRIPTS.items():
            frame = tk.Frame(self.root)
            frame.pack(pady=10)

            # Load button image
            image_path = os.path.join(IMAGE_DIR, f"{game_name.replace(' ', '_').lower()}.png")
            if os.path.exists(image_path):
                button_image = ImageTk.PhotoImage(Image.open(image_path).resize((50, 50)))
            else:
                button_image = None

            # Create button
            button = tk.Button(
                frame,
                text=game_name,
                image=button_image,
                compound="left",
                font=("Arial", 14),
                command=lambda path=script_path: self.run_game(path)
            )
            button.image = button_image  # Keep a reference to avoid garbage collection
            button.pack(side="left", padx=10)

        # Logout button
        tk.Button(self.root, text="Logout", font=("Arial", 14), command=self.logout).pack(pady=20)
        # Delete profile button
        tk.Button(self.root, text="Delete Profile", font=("Arial", 14), command=self.delete_profile).pack(pady=10)

    def create_profile_screen(self):
        """Create the profile creation screen."""
        self.clear_screen()

        tk.Label(self.root, text="Create Profile", font=("Arial", 20, "bold")).pack(pady=20)

        tk.Label(self.root, text="Username:", font=("Arial", 14)).pack()
        self.new_username_entry = tk.Entry(self.root, font=("Arial", 14))
        self.new_username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", font=("Arial", 14)).pack()
        self.new_password_entry = tk.Entry(self.root, font=("Arial", 14), show="*")
        self.new_password_entry.pack(pady=5)

        tk.Button(self.root, text="Create", font=("Arial", 14), command=self.create_profile).pack(pady=20)
        tk.Button(self.root, text="Back to Login", font=("Arial", 14), command=self.login_screen).pack(pady=10)

    def clear_screen(self):
        """Clear all widgets from the screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        """Handle user login."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            message = login_profile(username, password)
            self.current_user = username
            # messagebox.showinfo("Login Successful", message) # Test
            self.main_menu()
        except ValueError as e:
            messagebox.showerror("Login Failed", str(e))

    def logout(self):
        """Handle user logout."""
        self.current_user = None
        self.login_screen()

    def create_profile(self):
        """Handle profile creation."""
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty!")
            return

        message = create_profile(username, password)
        messagebox.showinfo("Profile Created", message)
        self.login_screen()

    def delete_profile(self):
        """Handle profile deletion."""
        if messagebox.askyesno("Delete Profile", "Are you sure you want to delete your profile?"):
            try:
                message = delete_profile(self.current_user)
                messagebox.showinfo("Profile Deleted", message)
                self.logout()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def run_game(self, script_path):
        """Run the selected game."""
        if os.path.exists(script_path):
            subprocess.run(["python", script_path])
        else:
            messagebox.showerror("Error", f"Game script not found: {script_path}")
    
    def show_score(self):
        root = tk.Tk()
        scores = load_all(self.current_user)