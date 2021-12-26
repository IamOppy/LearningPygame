import pygame
from sys import exit
import os
from random import randint
from pygame import font
from random import randint, choice
from pygame.constants import K_SPACE, KEYDOWN
from pygame.sprite import spritecollide

pygame.init()
WIDTH = 800
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
NAME_OF_DISPLAY = pygame.display.set_caption('PYGAME INTIAL')
CLOCK = pygame.time.Clock()  # CONTROL/SET FRAMERATE
FONT_ = pygame.font.Font(os.path.join(
    'BuildingBlocks/FONT', 'Pixeltype.ttf'), 50)  # FONT TYPE AND SIZE


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        PLAYER_SURFACE = pygame.image.load(os.path.join(
            "BuildingBlocks/Players", "Player_walk_1.png")).convert_alpha()
        PLAYER_SURFACE_2 = pygame.image.load(os.path.join(
            "BuildingBlocks/Players", "Player_walk_2.png")).convert_alpha()
        self.PLAYER_JUMP = pygame.image.load(
            os.path.join('BuildingBlocks/Players', "Jump.png"))
        self.PLAYER_WALK = [PLAYER_SURFACE, PLAYER_SURFACE_2]
        self.PLAYER_INDEX = 0

        self.image = self.PLAYER_WALK[self.PLAYER_INDEX]
        self.rect = self.image.get_rect(midbottom=(200, 250))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 250:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 250:
            self.rect.bottom = 250

    def animate_state(self):
        if self.rect.bottom < 250:
            self.image = self.PLAYER_JUMP
        else:
            self.PLAYER_INDEX += 0.1
            if self.PLAYER_INDEX >= len(self.PLAYER_WALK):
                self.PLAYER_INDEX = 0
            self.image = self.PLAYER_WALK[int(PLAYER_INDEX)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animate_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            FLY_FRAME_1 = pygame.image.load(os.path.join(
                "BuildingBlocks/Fly", 'Fly1.png')).convert_alpha()
            FLY_FRAME_2 = pygame.image.load(os.path.join(
                "BuildingBlocks/Fly", 'Fly2.png')).convert_alpha()
            self.FRAMES = [FLY_FRAME_1, FLY_FRAME_2]
            y_pos = 100
        else:
            SNAIL_FRAME_1 = pygame.image.load(
                os.path.join("BuildingBlocks/snail", "snail1.png")).convert_alpha()
            SNAIL_FRAME_2 = pygame.image.load(
                os.path.join("BuildingBlocks/snail", "snail2.png")).convert_alpha()
            self.FRAMES = [SNAIL_FRAME_1, SNAIL_FRAME_2]
            y_pos = 250

        self.animation_index = 0
        self.image = self.FRAMES[self.animation_index]
        self.rect = self.image.get_rect(
            midbottom=(randint(1000, 1100), y_pos))

    def animate_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.FRAMES):
            self.animation_index = 0
        else:
            self.image = self.FRAMES[int(self.animation_index)]

    def update(self):
        self.animate_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle = pygame.sprite.Group()


def sprite_collision():
    if pygame.sprite.spritecollide(player.sprite, obstacle, False):
        obstacle.empty()
        return False
    else:
        return True


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


SNAIL_FRAME_1 = pygame.image.load(
    os.path.join("BuildingBlocks/snail", "snail1.png")).convert_alpha()
SNAIL_FRAME_2 = pygame.image.load(
    os.path.join("BuildingBlocks/snail", "snail2.png")).convert_alpha()
SNAIL_RECT = SNAIL_FRAME_1.get_rect(bottomright=(600, 250))
SNAIL_FRAMES = [SNAIL_FRAME_1, SNAIL_FRAME_2]
SNAIL_FRAME_INDEX = 0
SNAIL_SURF = SNAIL_FRAMES[SNAIL_FRAME_INDEX]


FLY_FRAME_1 = pygame.image.load(os.path.join(
    "BuildingBlocks/Fly", 'Fly1.png')).convert_alpha()
FLY_FRAME_2 = pygame.image.load(os.path.join(
    "BuildingBlocks/Fly", 'Fly2.png')).convert_alpha()
FLY_FRAMES = [FLY_FRAME_1, FLY_FRAME_2]
FLY_FRAME_INDEX = 0
FLY_SURF = FLY_FRAMES[FLY_FRAME_INDEX]


TEXT_SURFACE = FONT_.render("My Game", False, "Black")
TEXT_RECT = TEXT_SURFACE.get_rect(center=(400, 50))


PLAYER_SURFACE = pygame.image.load(os.path.join(
    "BuildingBlocks/Players", "Player_walk_1.png")).convert_alpha()
PLAYER_SURFACE_2 = pygame.image.load(os.path.join(
    "BuildingBlocks/Players", "Player_walk_2.png")).convert_alpha()
PLAYER_JUMP = pygame.image.load(
    os.path.join('BuildingBlocks/Players', "Jump.png"))
PLAYER_WALK = [PLAYER_SURFACE, PLAYER_SURFACE_2]
PLAYER_INDEX = 0

PLAYER_ACTION_SURF = PLAYER_WALK[PLAYER_INDEX]
PLAYER_RECT = PLAYER_ACTION_SURF.get_rect(midbottom=(80, 250))


END_GAME_PLAYER = pygame.image.load(os.path.join(
    'BuildingBlocks/Players', 'Player_stand.png')).convert_alpha()
END_GAME_PLAYER = pygame.transform.scale2x(END_GAME_PLAYER)
ENDGAME_PLAYER_RECT = END_GAME_PLAYER.get_rect(center=(400, 200))

GAME_NAME = FONT_.render("Pixel Runner", False, "Black")
GAME_NAME_RECT = GAME_NAME.get_rect(center=(400, 80))

GAME_START_MESSAGE = FONT_.render("Press Space To Start!", False, ('Black'))
GAMESTART_RECT = GAME_START_MESSAGE.get_rect(center=(400, 320))

PLAYER_GRAVITY = 0
START_TIME = 0
GAME_RUNNING = False
SCORE = 0

OBSTACLE_TIME = pygame.USEREVENT + 1
pygame.time.set_timer(OBSTACLE_TIME, 2000)

SNAIL_ANIMATION_TIMER = pygame.USEREVENT + 2
pygame.time.set_timer(SNAIL_ANIMATION_TIMER, 500)

FLY_ANIMATION_TIMER = pygame.USEREVENT + 3
pygame.time.set_timer(FLY_ANIMATION_TIMER, 200)

OBSTACLE_RECT_LIST = []


def player_animation():
    global PLAYER_ACTION_SURF, PLAYER_INDEX

    if PLAYER_RECT.bottom < 250:
        PLAYER_ACTION_SURF = PLAYER_JUMP
    else:
        PLAYER_INDEX += 0.1
        if PLAYER_INDEX >= len(PLAYER_WALK):
            PLAYER_INDEX = 0
        PLAYER_ACTION_SURF = PLAYER_WALK[int(PLAYER_INDEX)]


def display_time():
    current_time = int(pygame.time.get_ticks() / 1000) - START_TIME
    time_surface = FONT_.render(f"Score:{current_time}", False, (64, 64, 64))
    time_rect = time_surface.get_rect(center=(400, 50))
    SCREEN.blit(time_surface, time_rect)
    return current_time


def draw_window():
    SCREEN.blit(SKY_SURFACE, (0, 0))
    SCREEN.blit(GROUND_SURFACE, (0, 250))

    pygame.draw.line(SCREEN, "Black", start_pos=(0, 0), end_pos=(800, 400))
    pygame.draw.ellipse(SCREEN, "black", pygame.Rect(50, 150, 100, 100))
    #SCREEN.blit(SNAIL_SURF, SNAIL_RECT)
    player_animation()
    player.draw(SCREEN)
    player.update()

    obstacle.draw(SCREEN)
    obstacle.update()

    #SCREEN.blit(PLAYER_ACTION_SURF, PLAYER_RECT)


def OBSTACLE_MOVEMENT(OBSTACLE_LIST):
    if OBSTACLE_LIST:
        for obs_rect in OBSTACLE_LIST:
            obs_rect.x -= 5
            if obs_rect.bottom == 250:
                SCREEN.blit(SNAIL_SURF, obs_rect)
            else:
                SCREEN.blit(FLY_SURF, obs_rect)

        OBSTACLE_LIST = [obs for obs in OBSTACLE_LIST if obs.x > -100]
        return OBSTACLE_LIST
    else:
        return []


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


def game_state_end(SCORE, OBSTACLE_LIST):
    global GAME_RUNNING
    if OBSTACLE_LIST:
        for obs_rect in OBSTACLE_LIST:
            if PLAYER_RECT.colliderect(obs_rect) and SCORE > 0:
                pass


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

            if event.type == OBSTACLE_TIME and GAME_RUNNING:
                obstacle.add(Obstacle(choice(['fly', 'snail'])))
                # if randint(0, 2):
                # OBSTACLE_RECT_LIST.append(
                # SNAIL_SURF.get_rect(bottomright=(1200, 250)))
               # else:
                # OBSTACLE_RECT_LIST.append(FLY_SURF.get_rect(
                # topright=(1200, 100)))
            if event.type == SNAIL_ANIMATION_TIMER:
                if SNAIL_FRAME_INDEX == 0:
                    SNAIL_FRAME_INDEX = 1
                else:
                    SNAIL_FRAME_INDEX = 0
                SNAIL_SURF = SNAIL_FRAMES[SNAIL_FRAME_INDEX]

            if event.type == FLY_ANIMATION_TIMER:
                if FLY_FRAME_INDEX == 0:
                    FLY_FRAME_INDEX = 1
                else:
                    FLY_FRAME_INDEX = 0
                FLY_SURF = FLY_FRAMES[FLY_FRAME_INDEX]

        else:
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                GAME_RUNNING = True
                SNAIL_RECT.left = 800
                START_TIME = int(pygame.time.get_ticks() / 1000)

    if GAME_RUNNING:
        #PLAYER_GRAVITY += 1
        #PLAYER_RECT.y += PLAYER_GRAVITY

        # SNAIL_POS_RESET()
        # border_limit()
        # collision_detections_MouseKey_Detections()
        draw_window()
        GAME_RUNNING = sprite_collision()
        #OBSTACLE_RECT_LIST = OBSTACLE_MOVEMENT(OBSTACLE_RECT_LIST)
        #game_state_end(SCORE, OBSTACLE_RECT_LIST)
        SCORE = display_time()

    else:
        if SCORE == 0:
            SCREEN.fill('white')
            SCREEN.blit(GAME_NAME, GAME_NAME_RECT)
            SCREEN.blit(END_GAME_PLAYER, ENDGAME_PLAYER_RECT)
            SCREEN.blit(GAME_START_MESSAGE, GAMESTART_RECT)
        elif SCORE > 0:
            SCREEN.fill("white")
            SCREEN.blit(GAME_NAME, GAME_NAME_RECT)
            SCREEN.blit(END_GAME_PLAYER, ENDGAME_PLAYER_RECT)
            score_message = FONT_.render(
                f"Your score: {SCORE}", False, "Black")
            score_message_rect = score_message.get_rect(center=(400, 330))
            SCREEN.blit(score_message, score_message_rect)

    pygame.display.update()
    CLOCK.tick(60)
