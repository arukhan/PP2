import pygame
import sys
import random
import time
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set the frames per second
FPS = 60
FramePerSec = pygame.time.Clock()

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Set initial speed and enemy speed
SPEED = 1
ENEMY_SPEED = 5

# Initialize score variables
SCORE = 0
COIN_SCORE = 0

# Set coin spawning interval and timer
COIN_INTERVAL = 120
COIN_TIMER = COIN_INTERVAL

# Set up fonts for text rendering
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image and start playing background music
background = pygame.image.load("AnimatedStreet.png")
pygame.mixer.init()
pygame.mixer.Sound('background.wav').play(-1)

# Set up the display
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE, ENEMY_SPEED
        self.rect.move_ip(0, ENEMY_SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            if SCORE % 10 == 0:  # Increase enemy speed every 10 points
                ENEMY_SPEED += 0.5


# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Define the Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, coin_type):
        super().__init__()
        # Set coin value based on type (regular, golden, silver)
        if coin_type == "Golden":
            self.value = 10
            self.image = pygame.image.load("GoldenCoin.png")
        elif coin_type == "Silver":
            self.value = 5
            self.image = pygame.image.load("SilverCoin.png")
        else:
            self.value = 1
            self.image = pygame.image.load("Coin.png")

        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global COIN_SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.topleft = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Create instances of Player and Enemy
P1 = Player()
E1 = Enemy()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

coins = pygame.sprite.Group()
coin = Coin("Regular")
coins.add(coin)
all_sprites.add(coin)

# Set up event for increasing enemy speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            ENEMY_SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Render background image
    DISPLAYSURF.blit(background, (0, 0))

    # Render enemy and player sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Render coins and handle collisions with player
    for coin in coins:
        coin.move()
        DISPLAYSURF.blit(coin.image, coin.rect)

    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    COIN_SCORE += sum(coin.value for coin in collected_coins)

    # Render scores
    scores = font_small.render("Enemies: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    coin_score_text = font_small.render("Coins: " + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(coin_score_text, (SCREEN_WIDTH - coin_score_text.get_width() - 10, 10))

    # Handle collisions with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()

    # Update display and tick clock
    pygame.display.update()
    FramePerSec.tick(FPS)

    # Decrease coin spawn timer and spawn coins
    COIN_TIMER -= 1
    if COIN_TIMER <= 0:
        coin_type = random.choice(["Regular", "Golden", "Silver"])
        coin = Coin(coin_type)
        coins.add(coin)
        all_sprites.add(coin)
        COIN_TIMER = COIN_INTERVAL
