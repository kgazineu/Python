import pygame
import random 
import time

speed = 15
size = width, height = 840, 560

snake_body = [[60, 50], [50, 50], [40, 50]]
snake_position = [50, 50]
apple_position = [random.randrange(1, (width//10)) * 10,
                  random.randrange(1, (height//10)) * 10]
apple_spawn = True

direction = 'down'
update_dir = direction

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

pygame.init()

window = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

def lose():
    text = pygame.font.Font("special_font.ttf", 60)
    window.fill(black)
    loss_text = text.render('SE FODEU', True, red)
    window.blit(loss_text, (320, 250))
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                update_dir = 'up'
            elif event.key == pygame.K_DOWN:
                update_dir = 'down'
            elif event.key == pygame.K_RIGHT:
                update_dir = 'right'
            elif event.key == pygame.K_LEFT:
                update_dir = 'left'
            elif event.key == pygame.K_ESCAPE: 
                pygame.quit()
    if update_dir == 'up' and direction != 'down':
        direction = 'up'
    elif update_dir == 'down' and direction != 'up':
        direction = 'down'
    elif update_dir == 'left' and direction != 'right':
        direction = 'left'
    elif update_dir == 'right' and direction != 'left':
        direction = 'right'

    if direction == 'up':
        snake_position[1] -= 10
    if direction == 'down':
        snake_position[1] += 10
    if direction == 'left':
        snake_position[0] -= 10
    if direction == 'right':
        snake_position[0] += 10
    
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
        apple_spawn = False
    else:
        snake_body.pop()
    if not apple_spawn:
            apple_position = [random.randrange(1, (width//10)) * 10,
                                random.randrange(1, (height//10)) * 10]
    apple_spawn = True
    window.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(window, green, (pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, red, (apple_position[0], apple_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > width-10:
        lose()
    elif snake_position[1] < 0 or snake_position[1] > height-10:
        lose()
    for shape in snake_body[1:]:
        if snake_position[0] == shape[0] and snake_position[1] == shape[1]:
            lose()


    pygame.display.update()
    clock.tick(speed)