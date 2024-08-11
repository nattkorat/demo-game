from pygame import *
import utils

window = display.set_mode((600, 400))
display.set_caption("Ping Pong Game")

icon = image.load("ball.png")
display.set_icon(icon)

clock = time.Clock()

background = (200, 255, 255)

ball = utils.GameSprite("ball.png", 300, 200, 50, 50, 3)


game = True
while game:
    window.fill(background)

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    ball.reset(window)

    clock.tick(60)
    display.update()
