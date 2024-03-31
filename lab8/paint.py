import pygame

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    drawing_shape = None
    color = (255, 255, 255)
    eraser_mode = False
    eraser_color = (0, 0, 0)
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:  
                    color = pygame.color.Color("black")  
                elif event.key == pygame.K_e:
                    color = (0, 0, 0)
                elif event.key == pygame.K_1:
                    drawing_shape = 'rectangle'
                elif event.key == pygame.K_2:
                    drawing_shape = 'circle'
                elif event.key == pygame.K_3:
                    if not eraser_mode:
                        color = eraser_color 
                    else:
                        color = (255, 255, 255)
                    eraser_mode = not eraser_mode
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append(position)
                points = points[-256:]
        
        screen.fill((0, 0, 0))
        
        for i in range(len(points) - 1):
            if drawing_shape == 'rectangle':
                pygame.draw.rect(screen, color, (points[i], (points[i+1][0]-points[i][0], points[i+1][1]-points[i][1])), 2)
            elif drawing_shape == 'circle':
                pygame.draw.circle(screen, color, points[i], radius)
            else:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
        
        pygame.display.flip()
        clock.tick(60)

main()
