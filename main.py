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
text_rect = text_surface.get_rect(center = (400, 50))

snail_guy = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_guy.get_rect(midbottom = (600, 300))


player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("collision")




    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, "Pink", text_rect, 10)
    pygame.draw.rect(screen, "Pink", text_rect)
    pygame.draw.line(screen, "Black", (800, 0), pygame.mouse.get_pos(), 10)
    screen.blit(text_surface, text_rect)

    screen.blit(snail_guy, snail_rect)
    screen.blit(player_surface, player_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    # if player_rect.colliderect(snail_rect):
    #     print("collision")
    mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())

    # update everything
    pygame.display.update()
    clock.tick(60)
