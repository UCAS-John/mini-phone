import tkinter as tk
from games.cookie_clicker.cookie import CookieClicker

def cookie_main(username=None):
    root = tk.Tk()
    app = CookieClicker(root, username)
    root.mainloop()

if __name__ == "__main__":
    cookie_main("1")