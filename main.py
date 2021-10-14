import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Glob Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render("My Goober Run", False, "Black")

snail_guy = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 600
snail_y_pos = 250

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.K_SPACE:
            snail_y_pos = 300



    # draw all our elements

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_x_pos -= 4
    if snail_x_pos < -200:
        snail_x_pos = 800
    screen.blit(snail_guy, (snail_x_pos, snail_y_pos))
    screen.blit(player_surface, (80, 200))


    # update everything
    pygame.display.update()
    clock.tick(60)
