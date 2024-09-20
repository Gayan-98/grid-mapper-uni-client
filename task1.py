'''
task1.py - modified from demo1.py to complete Task 1

Student Name: 
Student ID  :

Version History:
 - 9/9/24 - original version of demo1.py
 - 11/9/24 - modifications for task1.py as follows:
     a. Added 10 Trees to the item list
     b. Plotted them using scatter with red circles
     c. Updated the plot title
     d. Saved the plot as task1.png
'''

import random
import numpy as np
import matplotlib.pyplot as plt
from canopy import *
from matplotlib.patches import Rectangle


def overlay(g, item):
    coords = item.get_topleft()
    size = item.get_size()
    g[coords[0]:coords[0]+size, coords[1]:coords[1]+size] = item.get_image()[:,:]

def main():
    xlim = 60
    ylim = 80
    grid = np.zeros((ylim, xlim))

    # Create a list to store 10 Tree objects
    trees = []

    # Loop to create 10 Tree objects and add them to the list
    for _ in range(10):
        # Random positions within the grid limits
        x = random.randint(0, xlim-1)
        y = random.randint(0, ylim-1)
        # Add each Tree to the list
        trees.append(Tree((x, y), "r", 100))

    # Plotting setup
    fig, ax = plt.subplots()
    img = ax.imshow(grid)  # Associate the colorbar with this image
    plt.colorbar(img)      # Pass the image to colorbar

    # Variables to track the boundaries of the enclosing rectangle
    min_x, max_x = xlim, 0
    min_y, max_y = ylim, 0

    # Loop to plot the 10 trees and calculate bounding box
    for tree in trees:
        x, y = tree.get_coord()
        ax.scatter(x, y, c='r', s=tree.get_size())

        # Update the boundaries for the enclosing rectangle
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    # Add some padding to the rectangle
    padding = 5
    rect = Rectangle((min_x - padding, min_y - padding),
                     (max_x - min_x) + 2 * padding, 
                     (max_y - min_y) + 2 * padding, 
                     edgecolor='green', facecolor='none', linewidth=1.5)
    ax.add_patch(rect)

    # Update plot title
    plt.title("Plot of 10 Trees (Red Circles Enclosed by Green Rectangle)")

    # Save the plot as task1.png
    fig.savefig("task1.png")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
