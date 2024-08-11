from pygame import *

window = display.set_mode((500, 500))
display.set_caption("Shooter Game")
clock = time.Clock()


game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)
    display.update()