import pygame
import random


WIDTH = 800
HEIGHT = 800

ACCELERATION = 70 / 1000
MAX_SPEED = 20

last_ticks = 0


bird = Actor('bird-1/frame-1')
bird.speed = 0
bird.pos = (200, 400)
walls = []
is_game_over = False


def draw():
    screen.clear()
    bird.draw()
    for wall in walls:
        wall.draw()
    

def update_bird():
    global last_ticks
    global is_game_over
    ticks = pygame.time.get_ticks()
    time_delta = (ticks - last_ticks)
    if keyboard.space:
        bird.speed += ACCELERATION * time_delta
    else:
        bird.speed -= ACCELERATION * time_delta
    if bird.speed > MAX_SPEED:
        bird.speed = MAX_SPEED
    if bird.speed < -1 * MAX_SPEED:
        bird.speed = -1 * MAX_SPEED
    bird.y -= bird.speed
    last_ticks = ticks
    if bird.y < 0:
        bird.y = 0
        bird.speed = 0
    if bird.y > HEIGHT:
        bird.y = HEIGHT
        bird.speed = 0
    if bird.collidelist(walls) != -1:
        game_over()
    # print(bird.speed)


def add_wall():
    top_wall = Actor(
        'brick1',
        pos=(WIDTH+64, random.randint(40, HEIGHT/2-70)),
        anchor=('center', 'bottom'))
    top_wall.animation = animate(top_wall, pos=(-64, top_wall.y), duration=7)
    bottom_wall = Actor(
        'brick1',
        pos=(WIDTH+64, random.randint(HEIGHT/2+70, HEIGHT-40)),
        anchor=('center', 'top'))
    bottom_wall.animation = animate(bottom_wall, pos=(-64, bottom_wall.y), duration=7)
    walls.extend([top_wall, bottom_wall])
    print([top_wall.pos, bottom_wall.pos])


def game_over():
    global is_game_over
    is_game_over = True
    print('oh no')
    for wall in walls:
        wall.animation.stop()
    clock.unschedule(add_wall)


def update():
    if not is_game_over:
        update_bird()

add_wall()
clock.schedule_interval(add_wall, 5)
