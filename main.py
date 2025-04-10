import tkinter as tk
from tkinter import messagebox

# Define your game functions
def game1():
    messagebox.showinfo("Game 1", "Game 1")

def game2():
    messagebox.showinfo("Game 2", "Game 2")

def game3():
    messagebox.showinfo("Game 3", "Game 3")

def game4():
    messagebox.showinfo("Game 4", "Game 4")

def game5():
    messagebox.showinfo("Game 5", "Game 5")

# Create the main window
root = tk.Tk()
root.title("Game Selector")

# Create buttons for each game
tk.Button(root, text="Game 1", command=game1).pack(pady=5)
tk.Button(root, text="Game 2", command=game2).pack(pady=5)
tk.Button(root, text="Game 3", command=game3).pack(pady=5)
tk.Button(root, text="Game 4", command=game4).pack(pady=5)
tk.Button(root, text="Game 5", command=game5).pack(pady=5)

# Run the Tkinter event loop
root.mainloop()