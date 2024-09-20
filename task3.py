import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Assuming the Tree class exists in canopy.py
from canopy import Tree

# Block class to represent 25x25 block with items
class Block:
    def __init__(self, size, topleft):
        self.size = size  # 25x25 block
        self.topleft = topleft  # (x, y) coordinates of the top-left corner
        self.items = []  # Trees and Houses

    def add_item(self, item):
        self.items.append(item)

    def get_topleft(self):
        return self.topleft

    def generate_image(self):
        grid = np.zeros((self.size, self.size))
        for item in self.items:
            x, y = item.get_coord()
            if isinstance(item, Tree):
                # Assume Trees are represented by a single point (3x3 area)
                grid[y-1:y+2, x-1:x+2] = item.get_size()  # Small square for a tree
            elif isinstance(item, House):
                # House has height and width
                grid[y:y + item.height, x:x + item.width] = item.get_size()
        return grid

# House class with height and width attributes
class House:
    def __init__(self, coord, width, height, size):
        self.coord = coord  # (x, y) coordinates
        self.width = width
        self.height = height
        self.size = size

    def get_coord(self):
        return self.coord

    def get_size(self):
        return self.size

def generate_image(b, s, mshape):
    grid = np.zeros((mshape[0] * s, mshape[1] * s))
    for block in b:
        cx_start, ry_start = block.get_topleft()  # x,y mapping to column,row
        grid[ry_start:ry_start + s, cx_start:cx_start + s] = block.generate_image()[:, :]
    return grid

def main():
    blocksize = 25  # Update block size to 25x25
    map_shape = (1, 1)  # One block on the grid

    # Create block and add items
    blocks = []
    block = Block(blocksize, (0, 0))

    # Adding trees
    block.add_item(Tree((5, 5), 3, 3))  # Tree at x=5, y=5
    block.add_item(Tree((15, 5), 3, 3))  # Tree at x=15, y=5
    block.add_item(Tree((10, 20), 3, 3))  # Tree at x=10, y=20
    block.add_item(Tree((20, 20), 3, 3))  # Tree at x=20, y=20

    # Add one house (yellow) with height 5 and width 10
    block.add_item(House((10, 10), 10, 5, 10))  # House size 10 (yellow)

    blocks.append(block)

    # Plot the image
    plt.imshow(generate_image(blocks, blocksize, map_shape), vmin=0, vmax=10)
    plt.colorbar()

    # Add the rectangle for the house in yellow
    plt.gca().add_patch(Rectangle((10, 10), 10, 5, edgecolor='yellow', facecolor='none', linewidth=2))

    # Title update
    plt.title("Task 3: Testing Block with Trees and House")

    # Show plot
    plt.show()

if __name__ == "__main__":
    main()
