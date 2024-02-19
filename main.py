# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
square_width = 800
pixel_width = 30
screen = pygame.display.set_mode([square_width, square_width])
clock = pygame.time.Clock() #cria um objeto clock que pode ser usado para controlar o tempo de jogo como a taxa de quadros por segundoo (FPS)
running = True #variavel de controle para manter o loop do jogo executando até que um evento de saida seja executado

position_range = (pixel_width // 2, square_width - pixel_width // 2)

def generate_starting_position():
    return [random.randrange(position_range[0], position_range[1]), random.randrange(position_range[0], position_range[1])]

def reset():
    global snake, snake_length
    target.center = generate_starting_position()
    snake_pixel.center = generate_starting_position()
    snake = [snake_pixel.copy()] #essa lista representa todos os seguimentos da cobra, que é reiniciada para conter apenas um segmento: uma cópia do estado atual de "snake_pixel"
    snake_length = 1

def isOutOfBounds(snake_pixel):
    return snake_pixel.bottom > square_width or snake_pixel.top < 0 or snake_pixel.left < 0 or snake_pixel.right > square_width

#snake
snake_pixel = pygame.Rect([0, 0, pixel_width, pixel_width])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = pygame.Vector2(0,0)
snake_length = 1

#target 
target = pygame.Rect([0,0, pixel_width -2, pixel_width - 2])
target.center = generate_starting_position()

# RENDER YOUR GAME HERE

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_direction = pygame.Vector2(0, -pixel_width)
    if keys[pygame.K_s]:
        snake_direction = pygame.Vector2(0, pixel_width)
    if keys[pygame.K_a]:
        snake_direction = pygame.Vector2(-pixel_width, 0)
    if keys[pygame.K_d]:
        snake_direction = pygame.Vector2(pixel_width, 0)

    snake_pixel.move_ip(snake_direction)
    if isOutOfBounds(snake_pixel):
        reset()
    elif snake_pixel.colliderect(target):
        target.center = generate_starting_position()
        snake_length += 1 
    else:
        if len(snake) > snake_length:
            snake = snake[-snake_length:]

    snake.insert(0, snake_pixel.copy())
    if len(snake) > snake_length:
        snake.pop() #remove o segmento mais antigo se a cobra estiver maior que o comprimento

# fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_part)
    pygame.draw.rect(screen, "red", target)
    pygame.display.flip()
    clock.tick(10)  # limits FPS to 60

pygame.quit()