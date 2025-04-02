

import pygame
import random

# 游戏窗口的大小
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# 蛇和食物的大小
BLOCK_SIZE = 10

# 蛇的初始位置和方向
snake_x = WINDOW_WIDTH / 2
snake_y = WINDOW_HEIGHT / 2
snake_direction = 'right'

# 食物的初始位置
food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

# 初始化pygame
pygame.init()

# 创建游戏窗口
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('贪吃蛇')

# 更新蛇的位置
def update_snake(snake_direction, snake_x, snake_y):
    if snake_direction == 'up':
        snake_y -= BLOCK_SIZE
    elif snake_direction == 'down':
        snake_y += BLOCK_SIZE
    elif snake_direction == 'left':
        snake_x -= BLOCK_SIZE
    elif snake_direction == 'right':
        snake_x += BLOCK_SIZE
    return snake_x, snake_y

# 绘制蛇和食物
def draw_game(snake_x, snake_y, food_x, food_y):
    game_display.fill((255, 255, 255))
    pygame.draw.rect(game_display, (0, 255, 0), [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
    pygame.draw.rect(game_display, (0, 0, 255), [snake_x, snake_y, BLOCK_SIZE, BLOCK_SIZE])
    pygame.display.update()

# 游戏主循环
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = 'up'
            elif event.key == pygame.K_DOWN:
                snake_direction = 'down'
            elif event.key == pygame.K_LEFT:
                snake_direction = 'left'
            elif event.key == pygame.K_RIGHT:
                snake_direction = 'right'

    snake_x, snake_y = update_snake(snake_direction, snake_x, snake_y)

    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    draw_game(snake_x, snake_y, food_x, food_y)

pygame.quit()
quit()
