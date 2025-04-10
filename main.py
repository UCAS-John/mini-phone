import tkinter as tk
from tkinter import messagebox
import os
import subprocess

# Function to display project details

# Function to run the selected project
def run_project(project):
    games_scripts = {
        "game": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "subdir", "main.py"),
        "game": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "subdir", "main.py"),
        "game": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "subdir", "main.py"),
        "game": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "subdir", "main.py"),
        "game": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "subdir", "main.py"),
        "game": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "subdir", "main.py")
    }
    script_path = games_scripts.get(project)
    if script_path and os.path.exists(script_path):
        subprocess.run(["python", script_path])
    else:
        messagebox.showerror("Error", f"Script for {project} not found!")

# Main application
def main():
    root = tk.Tk()
    root.title("Personal Portfolio")

    # Introduction
    intro_label = tk.Label(
        root,
        text="Welcome to Mini Phone\n\n"
             "Select a game from the menu to run it.",
        justify="center",
        padx=10,
        pady=10
    )
    intro_label.pack()

    # Menu
    menu_label = tk.Label(root, text="Games", font=("Arial", 14, "bold"))
    menu_label.pack(pady=10)

    projects = ["game", "game", "game", "game", "game", "game"]
    for project in projects:
        frame = tk.Frame(root)
        frame.pack(pady=5)

        run_button = tk.Button(frame, text=f"Run: {project}", command=lambda p=project: run_project(p))
        run_button.pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()