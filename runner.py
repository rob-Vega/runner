import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

pygame.init()
# display surface
screen = pygame.display.set_mode((800, 400))
# window title
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

game_active = False
start_time = 0
score = 0

font = pygame.font.Font('./font/Pixeltype.ttf', 50)

title_surf = font.render('Runner', False, (111, 196, 169))
title_rect = title_surf.get_rect(center = (400, 60))

game_message_surf = font.render('Press [Space] to run', False, (111, 196, 169))
game_message_rect = game_message_surf.get_rect(center = (400, 330))

# surface
sky_surf = pygame.image.load('./graphics/sky.png').convert()
ground_surf = pygame.image.load('./graphics/ground.png').convert()

snail_surf = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('./graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# intro screen 
player_stand_surf = pygame.image.load('./graphics/player/player_stand.png')
player_stand_surf = pygame.transform.rotozoom(player_stand_surf, 0, 2)
player_stand_rect = player_stand_surf.get_rect(center = (400, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
            

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 2)
        # screen.blit(score_surf, score_rect)
        score = display_score()

        snail_rect.x -= 5
        if snail_rect.right < 0: snail_rect.left = 800

        screen.blit(snail_surf, snail_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))

        screen.blit(title_surf, title_rect)
        screen.blit(player_stand_surf, player_stand_rect)

        score_message_surf = font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message_surf.get_rect(center = (400, 330))

        if score: screen.blit(score_message_surf, score_message_rect)
        else: screen.blit(game_message_surf, game_message_rect)

    pygame.display.update()
    # framerate
    clock.tick(30)