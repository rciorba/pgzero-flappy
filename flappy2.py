WIDTH = 800
HEIGHT = 800


bird = Actor('bird-1/frame-1')
bird.pos = (200, 400)


def draw():
    screen.clear()
    bird.draw()
