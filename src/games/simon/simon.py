import random
import tkinter as tk
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from manage import scores

class SimonGame:
    def __init__(self, root, current_user=None):
        self.root = root
        self.current_user = current_user    
        self.root.title("Simon Game")
        self.running = False
        self.sequence = []
        self.player_sequence = []
        self.buttons = []
        self.score = 0
        self.pending_after_id = None  
        self.create_grid()
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game, font=("Arial", 14))
        self.start_button.grid(row=3, column=0, columnspan=3, pady=10)
        self.close_button = tk.Button(root, text="Close Game", command=self.close_game, font=("Arial", 14))
        self.close_button.grid(row=6, column=0, columnspan=3, pady=10)
        self.info_label = tk.Label(root, text="Press Start to Begin", font=("Arial", 14))
        self.info_label.grid(row=4, column=0, columnspan=3, pady=10)

    def create_grid(self):
        """Create a 3x3 grid of buttons."""
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, bg="gray", width=10, height=5, state="disabled")
                button.grid(row=i, column=j, padx=5, pady=5)
                button.config(command=lambda b=button: self.player_input(b))
                row.append(button)
            self.buttons.append(row)

    def start_game(self):
        # Start the game by resetting the sequence and adding the first pattern.
        if not self.running:
            self.score = 0
            self.sequence = []
            self.player_sequence = []
            self.info_label.config(text="Watch the pattern!")
            self.add_to_sequence()
            self.running = True
        else:
            return
        
    def add_to_sequence(self):
        # Add a random button to the sequence and play it.
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        self.sequence.append(self.buttons[row][col])
        self.play_sequence()

    def play_sequence(self):
        # Play the current sequence by flashing the buttons.
        self.disable_buttons()
        self.info_label.config(text="Watch the pattern!")
        self.root.after(500, self._play_sequence_step, 0)

    def _play_sequence_step(self, index):
        # Play each step of the sequence with a delay.
        if index < len(self.sequence):
            button = self.sequence[index]
            self.flash_button(button)
            self.pending_after_id = self.root.after(1000, self._play_sequence_step, index + 1)
        else:
            self.enable_buttons()
            self.info_label.config(text="Your turn!")

    def flash_button(self, button):
        # Flash a button by changing its color temporarily.
        original_color = button.cget("bg")
        button.config(bg="yellow")
        self.root.update()
        self.root.after(500, lambda: button.config(bg=original_color))

    def player_input(self, button):
        # Handle the player's input.
        self.player_sequence.append(button)
        self.flash_button(button)
        time.sleep(0.5)
        if self.player_sequence == self.sequence[:len(self.player_sequence)]:
            if len(self.player_sequence) == len(self.sequence):
                self.info_label.config(text="Correct! Watch the next pattern!")
                self.player_sequence = []
                self.root.after(1000, self.add_to_sequence)
                self.score += 1
        else:
            self.info_label.config(text=f"Wrong! Game Over!\nYou got {self.score} score")
            self.disable_buttons()
            self.running = False
            scores.save_score(username=self.current_user, game="simon", score=self.score)  # Save the score
            return self.score

    def enable_buttons(self):
        # Enable all buttons for player input.
        for row in self.buttons:
            for button in row:
                button.config(state="normal")

    def disable_buttons(self):
        # Disable all buttons to prevent input.
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def close_game(self):
        scores.save_score(username=self.current_user, game="simon", score=self.score)
        self.root.destroy()
