# Visualization

#These make it possible to make certain charts/graphs
import matplotlib.pyplot as plt
import numpy as np

#This function makes a radar chart to show the user the stats of a character they choose
def radar_chart(character):
    # List of stats on the chart
    stats = ['strength', 'defense', 'speed', 'health']
    #Takes the stats from the dictionary and makes sure that it ends
    values = [character[stat] for stat in stats]
    values += values[:1]  # Repeat the first value to close the radar chart
    
    # Makes the angles on the chart
    angles = np.linspace(0, 2 * np.pi, len(stats), endpoint=False).tolist()
    angles += angles[:1]

    # Makes it pop up as a 6 by 6
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True) # shows coordinates
    plt.xticks(angles[:-1], stats) # labels for the stats

    ax.plot(angles, values, linewidth=2, linestyle='solid') # Plotted the points with a line
    ax.fill(angles, values, alpha=0.4) # Adds color inside the chart
    
    plt.title(f"Stats for {character['name']}") #Title
    plt.show() #Displays the chart
