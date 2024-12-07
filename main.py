import pygame
import time
import random

pygame.init()  # Initialize pygame.

white = (255, 255, 255)
black = (36, 36, 36)
red = (213, 50, 80)
green = (0, 255, 0)

# Sizes for window of the game
display_width = 600
display_height = 500

icon = pygame.image.load("snakeicon.ico")
pygame.display.set_icon(icon)

display = pygame.display.set_mode((display_width, display_height))  # Apply size to the game
pygame.display.set_caption('Snake Game')  # Set title of game window

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15  # Speed of snake (Player)


# Render Score Label
def score(score):
    # Size and font of score label (Top-Left)
    score_font = pygame.font.SysFont("arial", 15)
    value = score_font.render(" Score: " + str(score), True, white)
    display.blit(value, [0, 0])


# Render Snake body
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block], border_radius=3)


# Render message on screen (Centered)
def message(msg, color, size=12):
    font_style = pygame.font.SysFont("bahnschrift", size)
    mesg = font_style.render(msg, True, color)
    # Center the message on the screen
    text_rect = mesg.get_rect(center=(display_width / 2, display_height / 2))
    display.blit(mesg, text_rect)


# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(black)  # Background color
            message("You Lost! Press Space to Restart or Q to Quit", red, size = 25)
            score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        # Keys to move the snake (Arrow keys)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
