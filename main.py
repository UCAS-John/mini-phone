import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk 
import subprocess

def run_game(project):
    games_scripts = {
        "game1": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "game1", "main.py"),
        "game2": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "game2", "main.py"),
        "game3": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "game3", "main.py"),
        "game4": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "game4", "main.py"),
        "game5": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "game5", "main.py"),
    }
    script_path = games_scripts.get(project)

    if script_path and os.path.exists(script_path):
        subprocess.run(["python", script_path])
    else:
        messagebox.showerror("Error", f"Script for {project} not found!")

# Main application
def main():
    root = tk.Tk()
    root.title("Game Launcher")
    root.geometry("1920x1024")  

    title_label = tk.Label(root, text="Game Launcher", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # Load image for buttons
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "download.png")
    if os.path.exists(image_path):
        button_image = ImageTk.PhotoImage(Image.open(image_path).resize((50, 50)))  # Resize image to fit button
    else:
        button_image = None  # Fallback if image is not found

    # List of projects
    projects = ["game1", "game2", "game3", "game4", "game5"]

    # Create buttons for each project
    for project in projects:
        frame = tk.Frame(root)
        frame.pack(pady=5)

        run_button = tk.Button(
            frame,
            text=f"Run: {project}",
            image=button_image,
            compound="left",  # Display image to the left of the text
            command=lambda p=project: run_game(p)
        )
        run_button.image = button_image  # Keep a reference to avoid garbage collection
        run_button.pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()