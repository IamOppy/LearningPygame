import pygame
from sys import exit
import os
from random import randint

from pygame.constants import K_SPACE, KEYDOWN

pygame.init()

WIDTH = 800
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
NAME_OF_DISPLAY = pygame.display.set_caption('PYGAME INTIAL')
CLOCK = pygame.time.Clock()  # CONTROL/SET FRAMERATE
FONT_ = pygame.font.Font(os.path.join(
    'BuildingBlocks/FONT', 'Pixeltype.ttf'), 50)  # FONT TYPE AND SIZE

SKY_SURFACE = pygame.image.load(os.path.join("BuildingBlocks", "Sky.png"))
GROUND_SURFACE = pygame.image.load(
    os.path.join("BuildingBlocks", "ground.png"))
SNAIL_SURFACE = pygame.image.load(
    os.path.join("BuildingBlocks/snail", "snail1.png")).convert_alpha()
SNAIL_RECT = SNAIL_SURFACE.get_rect(bottomright=(600, 250))
TEXT_SURFACE = FONT_.render("My Game", False, "Black")
TEXT_RECT = TEXT_SURFACE.get_rect(center=(400, 50))

PLAYER_SURFACE = pygame.image.load(os.path.join(
    "BuildingBlocks/Players", "Player_stand.png")).convert_alpha()
PLAYER_RECT = PLAYER_SURFACE.get_rect(midbottom=(80, 250))
PLAYER_GRAVITY = 0
GAME_RUNNING = True


def draw_window():
    SCREEN.blit(SKY_SURFACE, (0, 0))
    SCREEN.blit(GROUND_SURFACE, (0, 250))

    pygame.draw.rect(SCREEN, "purple", TEXT_RECT)
    pygame.draw.rect(SCREEN, "purple", TEXT_RECT, 10)
    pygame.draw.line(SCREEN, "Black", start_pos=(0, 0), end_pos=(800, 400))
    pygame.draw.ellipse(SCREEN, "black", pygame.Rect(50, 150, 100, 100))

    SCREEN.blit(TEXT_SURFACE, TEXT_RECT)
    SCREEN.blit(SNAIL_SURFACE, SNAIL_RECT)
    SCREEN.blit(PLAYER_SURFACE, PLAYER_RECT)


def SNAIL_POS_RESET():
    SNAIL_RECT.x -= 5
    if SNAIL_RECT.right <= 0:
        SNAIL_RECT.left = 800


def collision_detections_MouseKey_Detections():
    key_detection = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    if PLAYER_RECT.colliderect(SNAIL_RECT):
        print('Collided')
    elif PLAYER_RECT.collidepoint(mouse_pos):
        print("Mouse Detected on Object")
        print(key_detection)


def actions():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('Key pressed')


def border_limit():
    if PLAYER_RECT.bottom > 250:
        PLAYER_RECT.bottom = 250


def game_state_end():
    global GAME_RUNNING
    if SNAIL_RECT.colliderect(PLAYER_RECT):
        GAME_RUNNING = False
        SCREEN.fill("white")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if GAME_RUNNING:
            if event.type == pygame.MOUSEMOTION:
                if PLAYER_RECT.collidepoint(event.pos):
                    PLAYER_GRAVITY = -20
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE and PLAYER_RECT.bottom == 250:  # IF PLAYER HITS THE GROUND, THE PLAYER CAN JUMP
                    PLAYER_GRAVITY = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                GAME_RUNNING = True
                SNAIL_RECT.left = 800

    if GAME_RUNNING:
        PLAYER_GRAVITY += 1
        PLAYER_RECT.y += PLAYER_GRAVITY

        SNAIL_POS_RESET()
        border_limit()
        # collision_detections_MouseKey_Detections()
        draw_window()
        game_state_end()

        pygame.display.update()
        CLOCK.tick(60)
