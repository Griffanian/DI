import pygame
import numpy as np

# Define the size of the grid
grid_size_num=100
grid_size_tuple = (grid_size_num, grid_size_num)
cell_size = 800/grid_size_num

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set up the Pygame window
screen = pygame.display.set_mode((grid_size_tuple[0]*cell_size, grid_size_tuple[1]*cell_size))
pygame.display.set_caption("Conway's Game of Life")

# Create the grid
grid = np.zeros(grid_size_tuple)

# Define the initial state
s=50
div=int(s/2)
mid=int(grid_size_num/2)
board=np.random.randint(2, size=(s, s))
print(board)
grid[mid-div:mid+div, mid-div:mid+div] = board

# Define a function to update the grid
def update_grid(grid):
    # Copy the grid to avoid modifying it during iteration
    new_grid = np.copy(grid)
    # Iterate over each cell in the grid
    for i in range(grid_size_tuple[0]):
        for j in range(grid_size_tuple[1]):
            # Count the number of live neighbors
            neighbors = np.sum(grid[max(0, i-1):min(grid_size_tuple[0], i+2), max(0, j-1):min(grid_size_tuple[1], j+2)]) - grid[i, j]
            # Apply the rules of the game of life
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
    return new_grid

# Define a function to draw the grid
def draw_grid(grid):
    # Fill the screen with black
    screen.fill(BLACK)
    # Draw each cell
    for i in range(grid_size_tuple[0]):
        for j in range(grid_size_tuple[1]):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, WHITE, (i*cell_size, j*cell_size, cell_size, cell_size))
    # Update the display
    pygame.display.update()

# Draw the initial grid
draw_grid(grid)

# Run the game loop
running = True
while running:
    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the grid
    grid = update_grid(grid)
    # Draw the grid
    draw_grid(grid)
    # Wait for a short time

