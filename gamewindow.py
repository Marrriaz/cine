import pygame
background_color = (234, 212, 252)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Awesome Game")
screen.fill(background_color)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
