import pygame


pygame.init()


screen_width = 800
screen_height = 600


screen = pygame.display.set_mode((screen_width, screen_height))


def draw_room():
    
    screen.fill((0, 0, 0))  

while True:
    draw_room()  
    pygame.display.flip()  


pygame.quit()
