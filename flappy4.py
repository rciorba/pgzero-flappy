import pygame

WIDTH = 800
HEIGHT = 800
ACCELERATION = 70 / 1000
MAX_SPEED = 20
MIN_SPEED = -20

bird = Actor('bird-1/frame-1')
bird.pos = (200, 400)
bird.speed = 0

last_ticks = 0


def draw():
    screen.clear()
    bird.draw()


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
