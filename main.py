import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Use PIL for better image support
import subprocess

# Function to run the game
def run_game(project):
    games_scripts = {
        "game1": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "subdir", "main.py"),
        "chess": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "chess", "main.py"),
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

    # Load images for buttons
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "download.png")
    if os.path.exists(image_path):
        button_image = ImageTk.PhotoImage(Image.open(image_path).resize((50, 50)))  # Resize image to fit button
    else:
        button_image = None  # Fallback if image is not found

    projects = ["game1", "chess", "game3", "game4", "game5"]
    for project in projects:
        frame = tk.Frame(root)
        frame.pack(pady=5)

        run_button = tk.Button(
            frame,
            text=f"{project}",
            image=button_image,
            compound="left",  # Display image to the left of the text
            command=lambda p=project: run_game(p)
        )
        run_button.image = button_image  # Keep a reference to avoid garbage collection
        run_button.pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()