import tkinter as tk
from cookie import CookieClicker

def cookie():
    root = tk.Tk()
    app = CookieClicker(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)  # Save data on close
    root.mainloop()

if __name__ == "__main__":
    cookie()