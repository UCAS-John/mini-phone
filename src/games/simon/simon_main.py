import tkinter as tk
from games.simon.simon import SimonGame

def main():
    root = tk.Tk()
    game = SimonGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()