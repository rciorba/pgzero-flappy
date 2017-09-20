WIDTH = 800
HEIGHT = 800


bird = Actor('bird-1/frame-1')
bird.pos = (200, 400)


def draw():
    screen.clear()
    bird.draw()


def update():
    if keyboard.space:
        bird.y -= 1
    else:
        bird.y += 1
