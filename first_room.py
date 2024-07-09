import pygame
import sys


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
FONT_SIZE = 24

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Matrix Escape Room")


font = pygame.font.Font(None, FONT_SIZE)


room_state = "start"  # Possible states: "start", "red_pill", "blue_pill"

def draw_room():
    screen.fill(WHITE)
    if room_state == "start":
        text = font.render("Welcome to the Matrix Escape Room!", True, (0, 0, 0))
        screen.blit(text, (100, 100))
        text = font.render("You find yourself in a dimly lit room.", True, (0, 0, 0))
        screen.blit(text, (100, 150))
        text = font.render("A red pill lies on a table.", True, (0, 0, 0))
        screen.blit(text, (100, 180))
        text = font.render("A sign reads, 'Choose wisely.'", True, (0, 0, 0))
        screen.blit(text, (100, 210))
    elif room_state == "red_pill":
        # Display red pill riddle
        # ...
        pass
    elif room_state == "blue_pill":
        # Display blue pill riddle
        # ...
        pass

def main():
    global room_state
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    room_state = "red_pill"
                elif event.key == pygame.K_b:
                    room_state = "blue_pill"

        draw_room()
        pygame.display.flip()

if __name__ == "__main__":
    main()
