import tkinter as tk
from gui import menu

def main():
    root = tk.Tk()
    app = menu.Menu(root)
    root.mainloop()
    return app

#Rons the whole program
if __name__ == "__main__":
    app = main()