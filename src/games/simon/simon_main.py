import tkinter as tk
from games.simon.simon import SimonGame

def simon_main(cureent_user=None):
    # Initialize the game
#     print('''

# ███████╗██╗███╗   ███╗ ██████╗ ███╗   ██╗
# ██╔════╝██║████╗ ████║██╔═══██╗████╗  ██║
# ███████╗██║██╔████╔██║██║   ██║██╔██╗ ██║
# ╚════██║██║██║╚██╔╝██║██║   ██║██║╚██╗██║
# ███████║██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
# ╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
#           ''')
    root = tk.Tk()
    game = SimonGame(root=root, current_user=cureent_user)
    root.protocol("WM_DELETE_WINDOW", game.close_game)  # Ensure safe closing
    root.mainloop()
    return game.score

if __name__ == "__main__":
    score = simon_main()
    print(f"Final Score: {score}")