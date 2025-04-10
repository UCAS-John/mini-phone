import nicegui

# Define your GUI elements and logic here
def game1():
    pass
    # Code for game 1

def game2():
    pass
    # Code for game 2

def game3():
    pass
    # Code for game 3

def game4():
    pass
    # Code for game 4

def game5():
    pass
    # Code for game 5

# Create buttons for each game
button1 = nicegui.Button("Game 1", game1)
button2 = nicegui.Button("Game 2", game2)
button3 = nicegui.Button("Game 3", game3)
button4 = nicegui.Button("Game 4", game4)
button5 = nicegui.Button("Game 5", game5)

# Create a vertical layout to hold the buttons
layout = nicegui.VBox(button1, button2, button3, button4, button5)

# Create the main window and set the layout
window = nicegui.Window("Mini Phone", layout)

# Run the GUI application
nicegui.app.run()