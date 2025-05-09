import tkinter as tk
from games.simon.simon import SimonGame

def main():
    print('''

███████╗██╗███╗   ███╗ ██████╗ ███╗   ██╗
██╔════╝██║████╗ ████║██╔═══██╗████╗  ██║
███████╗██║██╔████╔██║██║   ██║██╔██╗ ██║
╚════██║██║██║╚██╔╝██║██║   ██║██║╚██╗██║
███████║██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
          ''')
    root = tk.Tk()
    game = SimonGame(root)
    root.mainloop()
    return game.score

if __name__ == "__main__":
    main()