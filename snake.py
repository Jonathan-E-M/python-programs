# snake.py
# by Jonathan M. 
# Date: April 9, 2021
# Idea from edureka.com/blog/snake-game-with-pygame/

#Imports:
import pygame
import time
import random




pygame.init()
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 102)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
display_width = 800
display_hight = 600


clock = pygame.time.Clock()

# Seting up display:
display = pygame.display.set_mode((display_width,display_hight))
pygame.display.set_caption('Snake Game')

# Setting up snake:
snake_block = 10
snake_speed = 15


# Function for displaying messages:
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width/6, display_hight/3])

# function for displaying score:
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])

# Snake function
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

# Game function:
def gameLoop():
    game_over = False
    game_close = False

    # Setting up snake:
    x1 = display_width/2
    y1 = display_hight/2
    x1_change = 0
    y1_change = 0
    snake_List =[]
    length_of_snake = 1

    # Food:
    foodx = round(random.randrange(0, display_width - snake_block)/10.0) * 10.0
    foody = round(random.randrange(0, display_hight - snake_block)/10.0) * 10.0

    # Game controls:
    while not game_over:
        while game_close == True:
            display.fill(blue)
            message("you lost! Press Q-Quit or C-Play Again",red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEY_DOWN:
                    if event.key == pygame.K_q:
                        game_over == True
                        game_close == False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        # Checking for out of bounds:
        if x1 >= display_width or x1 < 0 or y1 >= display_hight or y1 <0 :
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        display.fill(white)
        pygame.draw.rect(display, green, [foodx,foody,snake_block,snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]
        
        for x in snake_List[:-1]:
            if x == snake_head:
                game_close == True
        
        our_snake(snake_block, snake_List)
        display_score(length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block)/10.0) * 10.0
            foody = round(random.randrange(0, display_hight - snake_block)/10.0) * 10.0
            length_of_snake += 1
            print("Yummy!!")
        clock.tick(snake_speed)
    pygame.quit()
    quit()  
        
gameLoop()



