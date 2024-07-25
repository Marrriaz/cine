import pygame
import sys
import subprocess


pygame.init()


window_width, window_height = 894, 700
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Cineverse")

background_image = pygame.image.load('cineverse.png')
background_image = pygame.transform.scale(background_image, (window_width, window_height))

font_path = 'InknutAntiqua-Regular.ttf'
font_size = 14
font = pygame.font.Font(font_path, font_size)
input_text = ''
input_active = False
input_box = pygame.Rect(370, window_height - 150, 150, 40)
prompt_text = "Enter room number (from 1 to 4):"
prompt_position = (320, window_height - 200)

clock = pygame.time.Clock()
cursor_visible = True
cursor_timer = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                input_active = True
            else:
                input_active = False
        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text == "1":
                        subprocess.run(["python", "room1.py"])
                    input_text = ''
                else:
                    input_text += event.unicode

    window.blit(background_image, (0, 0))

    prompt_surface = font.render(prompt_text, True, (255, 255, 255))
    window.blit(prompt_surface, prompt_position)

    pygame.draw.rect(window, (255, 255, 255), input_box, 2)

    text_surface = font.render(input_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=input_box.center)  
    window.blit(text_surface, text_rect)

    cursor_timer += clock.tick(30) / 1000
    if cursor_timer >= 0.5:
        cursor_timer = 0
        cursor_visible = not cursor_visible
    if input_active and cursor_visible:
        cursor_rect = pygame.Rect(text_rect.right + 2, text_rect.top, 2, text_rect.height)
        pygame.draw.rect(window, (255, 255, 255), cursor_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
