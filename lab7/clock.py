import pygame
import sys
import math
from datetime import datetime, timedelta
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

mickey_clock_image = pygame.image.load("mainclock.png")
mickey_right_arm_image = pygame.image.load("mickey_right_arm.png")
mickey_left_arm_image = pygame.image.load("mickey_left_arm.png")

mickey_clock_rect = mickey_clock_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
mickey_right_arm_rect = mickey_right_arm_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
mickey_left_arm_rect = mickey_left_arm_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

def draw_clock(seconds_angle, minutes_angle):
    screen.fill((255, 255, 255)) 
  
    screen.blit(mickey_clock_image, mickey_clock_rect)
    rotated_right_arm = pygame.transform.rotate(mickey_right_arm_image, -minutes_angle)
    
    right_arm_rect = rotated_right_arm.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(rotated_right_arm, right_arm_rect)
    rotated_left_arm = pygame.transform.rotate(mickey_left_arm_image, -seconds_angle)
    left_arm_rect = rotated_left_arm.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(rotated_left_arm, left_arm_rect)
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = datetime.now()
        seconds = current_time.second
        minutes = current_time.minute+10

        seconds_angle = (seconds / 60) * 360
        minutes_angle = (minutes / 60) * 360

        draw_clock(seconds_angle, minutes_angle)
        clock.tick(60)

    pygame.quit()
    sys.exit()
main()
