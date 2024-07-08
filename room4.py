import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lord of the Rings Escape Room")

# Define colors
background_color = (0, 0, 0)  # Black

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(background_color)

    # Your room-specific logic goes here
    # For example:
    # - Display the Doors of Durin inscription
    # - Handle player input for the cryptex
    # - Show Galadriel's scrying pool

    # Update the display
    pygame.display.flip()

# Clean up and exit
pygame.quit()
sys.exit()
