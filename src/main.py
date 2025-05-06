import tkinter as tk
from gui.menu import Menu

app = None

def main():
    global app
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()