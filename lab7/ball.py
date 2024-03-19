import pygame
import sys
pygame.init()
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Red Ball")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_radius = 25
ball_x, ball_y = screen_width // 2, screen_height // 2
ball_speed = 20
running = True
while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if ball_y - ball_speed >= ball_radius:
            ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        if ball_y + ball_speed <= screen_height - ball_radius:
            ball_y += ball_speed
    if keys[pygame.K_LEFT]:
        if ball_x - ball_speed >= ball_radius:
            ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        if ball_x + ball_speed <= screen_width - ball_radius:
            ball_x += ball_speed

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
