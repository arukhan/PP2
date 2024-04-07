import pygame 
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# paddle
paddleW = 300
paddleH = 25
paddleSpeed = 25
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)
paddle_shrink_rate = 0.1

# Ball
ballRadius = 20
ballSpeed = 3
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1
ball_speed_increase_rate = 0.005

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(0, 255, 0) for _ in range(10) for _ in range(4)]  # Fixed list of colors for blocks

is_breakable = [True] * len(block_list)

# In the block creation loop, mark some blocks as unbreakable
# Example: Mark every 5th block as unbreakable
unbreakable_indices = [i for i in range(len(block_list)) if i % 5 == 0][:3]  # First 4 unbreakable blocks
unbreakable_hits = [0] * len(unbreakable_indices)  # Track hits on unbreakable blocks
for i in unbreakable_indices:
    is_breakable[i] = False
    
font = pygame.font.SysFont(None, 30)  

# Add some bonus blocks among regular blocks
num_bonus_blocks = 5  # Number of bonus blocks
bonus_blocks = []  # Initialize bonus blocks list
for _ in range(num_bonus_blocks):
    idx = random.randint(0, len(block_list) - 1)
    bonus_blocks.append(block_list.pop(idx))

bonus_color = (255, 215, 0)  # Gold color for bonus blocks
bonus_block_points = 10  # Points to be added on destroying a bonus block

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Function to open main menu
def main_menu():
    global paddleSpeed, ballSpeed, FPS
    menu_font = pygame.font.SysFont('comicsansms', 50)
    menu_text = menu_font.render('Settings', True, (255, 255, 255))
    menu_text_rect = menu_text.get_rect(center=(W // 2, H // 2 - 150))

    paddle_speed_text = menu_font.render('Paddle Speed:', True, (255, 255, 255))
    paddle_speed_text_rect = paddle_speed_text.get_rect(center=(W // 2 - 150, H // 2))

    ball_speed_text = menu_font.render('Ball Speed:', True, (255, 255, 255))
    ball_speed_text_rect = ball_speed_text.get_rect(center=(W // 2 - 150, H // 2 + 50))

    fps_text = menu_font.render('FPS:', True, (255, 255, 255))
    fps_text_rect = fps_text.get_rect(center=(W // 2 - 150, H // 2 + 100))

    paddle_speed_input = pygame.Rect(W // 2 + 50, H // 2 - 25, 100, 50)
    ball_speed_input = pygame.Rect(W // 2 + 50, H // 2 + 25, 100, 50)
    fps_input = pygame.Rect(W // 2 + 50, H // 2 + 75, 100, 50)

    paddle_speed_value = str(paddleSpeed)
    ball_speed_value = str(ballSpeed)
    fps_value = str(FPS)

    input_active = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        if paddle_speed_input.collidepoint(event.pos):
                            paddle_speed_value = paddle_speed_value[:-1]
                        elif ball_speed_input.collidepoint(event.pos):
                            ball_speed_value = ball_speed_value[:-1]
                        elif fps_input.collidepoint(event.pos):
                            fps_value = fps_value[:-1]
                    else:
                        if paddle_speed_input.collidepoint(event.pos):
                            paddle_speed_value += event.unicode
                        elif ball_speed_input.collidepoint(event.pos):
                            ball_speed_value += event.unicode
                        elif fps_input.collidepoint(event.pos):
                            fps_value += event.unicode
                elif event.key == pygame.K_ESCAPE:
                    return  # Close menu and resume game
                elif event.key == pygame.K_RETURN:
                    paddleSpeed = int(paddle_speed_value)
                    ballSpeed = int(ball_speed_value)
                    FPS = int(fps_value)
                    return
                elif event.key == pygame.K_TAB:
                    input_active = True

        screen.fill(bg)

        pygame.draw.rect(screen, (255, 255, 255), paddle_speed_input, 2)
        pygame.draw.rect(screen, (255, 255, 255), ball_speed_input, 2)
        pygame.draw.rect(screen, (255, 255, 255), fps_input, 2)

        paddle_speed_value_text = menu_font.render(paddle_speed_value, True, (255, 255, 255))
        ball_speed_value_text = menu_font.render(ball_speed_value, True, (255, 255, 255))
        fps_value_text = menu_font.render(fps_value, True, (255, 255, 255))

        screen.blit(menu_text, menu_text_rect)
        screen.blit(paddle_speed_text, paddle_speed_text_rect)
        screen.blit(ball_speed_text, ball_speed_text_rect)
        screen.blit(fps_text, fps_text_rect)

        screen.blit(paddle_speed_value_text, paddle_speed_input)
        screen.blit(ball_speed_value_text, ball_speed_input)
        screen.blit(fps_value_text, fps_input)

        pygame.display.flip()
        clock.tick(FPS)

# Main game loop
menu_open = False  # Track if the menu is open
space_pressed = False  # Track if the Space key has been pressed

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_pressed = not space_pressed  # Toggle the menu with each press of the Space key

    if space_pressed:
        main_menu()
        space_pressed = False  # Reset the flag after closing the menu
    else:
        screen.fill(bg)

        # Drawing blocks
        for i, block in enumerate(block_list):
            if is_breakable[i]:
                pygame.draw.rect(screen, color_list[i], block)
            else:
                pygame.draw.rect(screen, (255, 255, 255), block)  # Yellow color for unbreakable blocks
                text = font.render('U', True, (0, 0, 0))
                text_rect = text.get_rect(center=block.center)
                screen.blit(text, text_rect)
                
        # Draw bonus blocks
        for block in bonus_blocks:
            pygame.draw.rect(screen, bonus_color, block)
            text = font.render('B', True, (0, 0, 0))
            text_rect = text.get_rect(center=block.center)
            screen.blit(text, text_rect)

        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

        # Ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        # Collision left
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        # Collision top
        if ball.centery < ballRadius + 50:
            dy = -dy
        # Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

        # Collision with bonus blocks
        for i, block in enumerate(bonus_blocks):
            if ball.colliderect(block):
                dx, dy = detect_collision(dx, dy, ball, block)
                bonus_blocks.pop(i)
                collision_sound.play()
                game_score += bonus_block_points
                # Display "+10" message
                font = pygame.font.SysFont('comicsansms', 30)
                text_surface = font.render('+10', True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(W // 2, H // 2))
                screen.blit(text_surface, text_rect)
                pygame.display.flip()
                pygame.time.delay(500)  # Delay for 0.5 seconds to display the message
            
        # Collision blocks
        hitIndex = ball.collidelist(block_list)
        if hitIndex != -1:
            hitRect = block_list[hitIndex]
            if is_breakable[hitIndex]:
                block_list.pop(hitIndex)
                dx, dy = detect_collision(dx, dy, ball, hitRect)
                game_score += 1
                collision_sound.play()
            else:
                dx, dy = detect_collision(dx, dy, ball, hitRect)  

        # Game score
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)

        # Win/lose screens
        if ball.bottom > H:
            screen.fill((255, 0, 0))
            screen.blit(losetext, losetextRect)
        elif not len(block_list):
            screen.fill((255, 255, 255))
            screen.blit(wintext, wintextRect)

        # Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed

        # Paddle shrink over time
        paddleW -= paddle_shrink_rate
        paddle.width = max(int(paddleW), 50)

        # Ball speed increase over time
        ballSpeed += ball_speed_increase_rate

        pygame.display.flip()
        clock.tick(FPS)
