import pygame
import random

WIDTH = 800
HEIGHT = 800
ACCELERATION = 70 / 1000
MAX_SPEED = 20
MIN_SPEED = -20

bird = Actor('bird-1/frame-1')
bird.pos = (200, 400)
bird.speed = 0

last_ticks = 0

walls = []


def draw():
    screen.clear()
    bird.draw()
    for wall in walls:
        wall.draw()


def update():
    global last_ticks
    ticks = pygame.time.get_ticks()
    time_delta = (ticks - last_ticks)
    last_ticks = ticks
    if keyboard.space:
        bird.speed -= ACCELERATION * time_delta
    else:
        bird.speed += ACCELERATION * time_delta
    if bird.speed > MAX_SPEED:
        bird.speed = MAX_SPEED
    if bird.speed < MIN_SPEED:
        bird.speed = MIN_SPEED
    bird.y += bird.speed
    if bird.y < 0:
        bird.y = 0
    if bird.y > HEIGHT:
        bird.y = HEIGHT


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


add_wall()
clock.schedule_interval(add_wall, 5)
