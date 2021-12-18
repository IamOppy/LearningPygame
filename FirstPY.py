import pygame
from sys import exit
import os
from random import randint

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

ENEMY_SURFACE = pygame.image.load(os.path.join(
    "BuildingBlocks/Players", "Player_stand.png")).convert_alpha()
ENEMY_RECT = ENEMY_SURFACE.get_rect(midbottom=(80, 250))


def draw_window():
    SCREEN.blit(SKY_SURFACE, (0, 0))
    SCREEN.blit(GROUND_SURFACE, (0, 250))
    SCREEN.blit(TEXT_SURFACE, (TEXT_RECT))
    SCREEN.blit(SNAIL_SURFACE, SNAIL_RECT)
    SCREEN.blit(ENEMY_SURFACE, ENEMY_RECT)


def SNAIL_POS_RESET():
    SNAIL_RECT.x -= 1
    if SNAIL_RECT.right <= 0:
        SNAIL_RECT.left = 800


def collision_detections_Key_Detections():
    key_detection = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    if ENEMY_RECT.colliderect(SNAIL_RECT):
        print('Collided')
    elif ENEMY_RECT.collidepoint(mouse_pos):
        print("Mouse Detected on Object")
        print(key_detection)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if ENEMY_RECT.collidepoint(event.pos):
                print("Mouse Object detected on Enemy")

    SNAIL_POS_RESET()
    # collision_detections_Key_Detections()
    draw_window()

    pygame.display.update()
    CLOCK.tick(60)
