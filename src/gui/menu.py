import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import subprocess
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from profiles.profile import create_profile, delete_profile, login_profile
from manage.scores import load_all, load_top

# Paths for images and game scripts
IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
GAMES_SCRIPTS = {
    # "Battle Simulator": os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', "games", "battle_simulator", "main.py"), # Remove this game
    "Cookie Clicker": os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', "games", "cookie_clicker", "cookie_main.py")),
    "Hangman": os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', "games", "Hangman", "hangman_main.py")),
    "Number Guessing": os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', "games", "number_guessing", "number_guessing_main.py")),
    "Rock Paper Scissors": os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', "games", "rock-paper-scissor", "rps_main.py")),
    "Simon": os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', "games", "simon", "simon_main.py")),
    "Simple Quiz": os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', "games", "Simple_quiz", "quiz_main.py")),
    "Tic Tac Toe": os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', "games", "Tic_Tac_Toe", "tic_tac_toe_main.py"))
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

        tk.Label(self.root, text="Be aware some of the game run on terminal!", font=("Arial", 16)).pack(pady=10)

        # Create a frame for game buttons
        game_frame = tk.Frame(self.root)
        game_frame.pack(pady=20)

        # Create game buttons with a row limit of 5
        row, col = 0, 0
        for game_name, script_path in GAMES_SCRIPTS.items():
            # Load button image
            image_path = os.path.join(IMAGE_DIR, f"{game_name.replace(' ', '_').lower()}.png")
            if os.path.exists(image_path):
                button_image = ImageTk.PhotoImage(Image.open(image_path).resize((50, 50)))
            else:
                button_image = None

            # Create button
            button = tk.Button(
                game_frame,
                text=game_name,
                image=button_image,
                compound="top",
                bg="blue",
                font=("Arial", 12),
                command=lambda path=script_path: self.run_game(path)
            )
            button.image = button_image  # Keep a reference to avoid garbage collection
            button.grid(row=row, column=col, padx=10, pady=10)

            # Add top score label below the button
            top_scores = load_top()  # Load top scores as a DataFrame
            top_score_text = f"Top Score:\n"
            try:
                top_score_data = top_scores[game_name.lower()]  # Get the top score based on iteration index
                # print(top_score_data)
                # print(top_score_data.to_string())
                for pair in top_score_data:   
                    text = f"{pair[0]}: {pair[1]}"
                    top_score_text += f"{text}\n"
            except IndexError:
                top_score_text = "Top Score: N/A"
            except KeyError:
                # top_score_text = "No Top score for this game"
                top_score_text = ""

            top_score_label = tk.Label(game_frame, text=top_score_text, font=("Arial", 10))
            top_score_label.grid(row=row + 1, column=col, pady=(0, 10))

            col += 1
            if col == 5:  # Move to the next row after 5 buttons
                col = 0
                row += 2

        # Create a frame for the "Show Score" button (beneath the game buttons)
        score_button_frame = tk.Frame(self.root)
        score_button_frame.pack(pady=20)

        # "Show Score" button
        tk.Button(score_button_frame, text="Show Score", font=("Arial", 14), command=self.show_score).pack()

        # Create a frame for bottom buttons (aligned horizontally)
        bottom_buttons_frame = tk.Frame(self.root)
        bottom_buttons_frame.pack(side="bottom", pady=20, fill="x")

        # "Delete Profile" button on the bottom right corner
        delete_profile_button = tk.Button(
            bottom_buttons_frame, text="Delete Profile", font=("Arial", 14), command=self.delete_profile
        )
        delete_profile_button.pack(side="right", padx=10, anchor="se")

        # Create a separate frame for the "Logout" button
        logout_button_frame = tk.Frame(self.root)
        logout_button_frame.pack(side="bottom", pady=10)

        # "Logout" button in the bottom middle
        logout_button = tk.Button(
            logout_button_frame, text="Logout", font=("Arial", 14), command=self.logout
        )
        logout_button.pack()

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
        print(script_path)
        if os.path.exists(script_path):
            subprocess.run(["python", script_path])
        else:
            messagebox.showerror("Error", f"Game script not found: {script_path}")
    
    def show_score(self):
        root = tk.Tk()
        root.title(f"{self.current_user} Scoreboard")
        root.geometry("600x400")
        scores = load_all(self.current_user)

        print(scores)

        for game, score in scores.items():
            if game == "username":
                continue
            tk.Label(root, text=f"{game}: {score}", font=("Arial", 14)).pack(pady=5)

        root.mainloop()

    def show_top_scores(self):
        # Display the top 5 scores for each game in a new window.
        top_scores = load_top()  

        # Create a new window
        top_scores_window = tk.Toplevel(self.root)
        top_scores_window.title("Top 5 Scores")
        top_scores_window.geometry("1200x900")

        tk.Label(top_scores_window, text="Top 5 Scores", font=("Arial", 20, "bold")).pack(pady=20)

        # Display the top scores for each game
        for game, scores in top_scores.items():
            tk.Label(top_scores_window, text=f"{game}", font=("Arial", 16, "bold")).pack(pady=10)
            for username, score in scores:
                tk.Label(top_scores_window, text=f"{username}: {score}", font=("Arial", 14)).pack()

        tk.Button(top_scores_window, text="Close", font=("Arial", 14), command=top_scores_window.destroy).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()