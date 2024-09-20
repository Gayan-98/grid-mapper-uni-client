'''
task2.py - modified from task1.py to complete Task 2

Student Name: 
Student ID  :

Version History:
 - 9/9/24 - original version of demo1.py
 - 11/9/24 - modifications for task1.py as follows:
     a. Added 10 Trees to the item list
     b. Plotted them using scatter with red circles
     c. Updated the plot title
     d. Saved the plot as task1.png
 - 20/9/24 - modifications for task2.py:
     a. Created side by side subplots
     b. Modified grid to have green frame with a colorbar
     c. Increased number of trees to 20 and changed color to green
     d. Updated titles and saved as task2.png
'''

import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from canopy import *  


def create_trees(num_trees, xlim, ylim, color='r', size=100):
    trees = []
    for _ in range(num_trees):
        x = random.randint(0, xlim-1)
        y = random.randint(0, ylim-1)
        trees.append(Tree((x, y), color, size))
    return trees


def plot_trees(ax, grid, trees, rectangle=True, padding=5, circle_color='r', size_factor=1):
    # Set the background color
    ax.set_facecolor('pink' if circle_color == 'r' else 'black')
    
    # Display the grid with a colormap
    img = ax.imshow(grid, cmap='hot', vmin=0, vmax=1)
    
    # Now the colorbar is properly associated with `img`
    plt.colorbar(img, ax=ax)

    # Variables to track the boundaries of the enclosing rectangle
    min_x, max_x = grid.shape[1], 0
    min_y, max_y = grid.shape[0], 0

    # Plot the trees
    for tree in trees:
        x, y = tree.get_coord()
        ax.scatter(x, y, c=circle_color, s=tree.get_size() * size_factor)

        # Update the boundaries for the enclosing rectangle
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    # Draw the rectangle around the trees
    if rectangle:
        rect = Rectangle((min_x - padding, min_y - padding),
                         (max_x - min_x) + 2 * padding,
                         (max_y - min_y) + 2 * padding,
                         edgecolor='green', facecolor='none', linewidth=1.5)
        ax.add_patch(rect)

    return img


def main():
    xlim = 60
    ylim = 80

    # Create the figure and two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Grid for both plots
    grid = np.zeros((ylim, xlim))

    # First subplot (10 trees, red circles)
    trees1 = create_trees(10, xlim, ylim, color='r', size=100)
    plot_trees(ax1, grid, trees1, rectangle=True, circle_color='r', size_factor=1)
    ax1.set_title("Red Trees with Green Frame (10 Trees)")

    # Second subplot (20 trees, green circles, twice the size, hot colormap)
    trees2 = create_trees(20, xlim, ylim, color='g', size=100)
    plot_trees(ax2, grid, trees2, rectangle=True, circle_color='g', size_factor=2)
    ax2.set_title("Green Trees with Hot Colormap (20 Trees, Larger)")

    # Set the higher-level title (suptitle)
    plt.suptitle("Comparison of Red vs Green Trees with Different Sizes and Colors")

    # Save the figure as task2.png
    fig.savefig("task2.png")

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
