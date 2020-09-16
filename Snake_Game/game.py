import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

d_width = 800
d_height = 600

dis = pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption("Jogo da Cobrinha")

clock = pygame.time.Clock()

snake_block = 10

font_style = pygame.font.SysFont(None,25)

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,green,[x[0],x[1],snake_block,snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [d_width / 10, d_height / 5])

def game_loop():
    game_over = False
    game_close = False

    snake_speed =  10

    x1 = d_width / 2
    y1 = d_height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_size = 1

    x_food = round(random.randrange(0,d_width - snake_block) / 10) * 10
    y_food = round(random.randrange(0,d_height - snake_block) / 10) * 10

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("Você perdeu aperte Q Se quiser sair, e P se quise jogar novamente.",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = - snake_block    
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block

        if (
            (x1 >= d_width) 
            or (x1 < 0)
            or (y1 >= d_height) 
            or (y1 < 0)
        ):
            game_close = True
            #print(game_close)

        x1 += x_change
        y1 += y_change
        dis.fill(white)
        pygame.draw.rect(dis,red,[x_food,y_food,snake_block,snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_size:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block,snake_list)

        pygame.display.update()

        if x1 == x_food and y1 == y_food:
            x_food = round(random.randrange(0,d_width - snake_block) / 10) * 10
            y_food = round(random.randrange(0,d_height - snake_block) / 10) * 10
            snake_size += 1
            snake_speed += 5

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()