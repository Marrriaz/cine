import pygame

# Define the background color (RGB values)
background_color = (234, 212, 252)

# Create the screen object (window) with dimensions (width, height)
screen = pygame.display.set_mode((800, 600))

# Set the window title
pygame.display.set_caption("My Awesome Game")

# Fill the background color
screen.fill(background_color)

# Update the display
pygame.display.flip()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
