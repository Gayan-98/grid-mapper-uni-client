import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Assuming the Tree class exists in canopy.py
from canopy import Tree

# Block class to represent 20x20 block with items
class Block:
    def __init__(self, size, topleft):
        self.size = size  # 20x20 block
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

def generate_image(blocks, block_size, map_shape):
    grid = np.zeros((map_shape[0] * block_size, map_shape[1] * block_size))
    for block in blocks:
        cx_start, ry_start = block.get_topleft()  # x,y mapping to column,row
        grid[ry_start:ry_start + block_size, cx_start:cx_start + block_size] = block.generate_image()[:, :]
    return grid

def main():
    block_size = 20  # Each block is a 20x20 square
    map_shape = (2, 3)  # 2 rows of blocks, 3 columns
    blocks = []

    # Create six blocks
    for row in range(2):
        for col in range(3):
            blocks.append(Block(block_size, (col * block_size, row * block_size)))

    # Add items to the blocks
    # Top row: 3 trees and a house
    for i in range(3):
        blocks[i].add_item(House((5, 5), 5, 5, 8))  # House
        blocks[i].add_item(Tree((3, 10), 3, 3))     # Tree
        blocks[i].add_item(Tree((10, 5), 3, 3))     # Tree
        blocks[i].add_item(Tree((15, 10), 3, 3))    # Tree

    # Bottom row: Only trees with random shades of green
    for i in range(3, 6):
        for _ in range(5):  # 5 trees per block
            x = random.randint(3, 17)  # Random x-coordinate within block
            y = random.randint(3, 17)  # Random y-coordinate within block
            blocks[i].add_item(Tree((x, y), 3, 3))  # Removed the extra size argument

    # Plot the image
    plt.imshow(generate_image(blocks, block_size, map_shape), vmin=0, vmax=10)
    plt.colorbar()

    # Add red lines around the blocks
    for row in range(1, map_shape[0]):
        plt.plot([0, map_shape[1] * block_size], [row * block_size, row * block_size], color='red', linewidth=2)
    for col in range(1, map_shape[1]):
        plt.plot([col * block_size, col * block_size], [0, map_shape[0] * block_size], color='red', linewidth=2)

    # Update plot title
    plt.title("Task 4: (2, 3) grid of blocks with houses and trees")

    # Show plot
    plt.show()

if __name__ == "__main__":
    main()
