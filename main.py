from pygame import *
import utils

window = display.set_mode((600, 400))
display.set_caption("Ping Pong Game")


icon = image.load("ball.png")
display.set_icon(icon)

clock = time.Clock()

background = (200, 255, 255)

ball = utils.Ball("ball.png", 300, 200, 30, 30, 3)

l_paddle = utils.Paddle(20, 150, 20, 100, (255, 255, 0))
r_paddle = utils.Paddle(540, 150, 20, 100, (255, 255, 0))

font.init()
fonts = font.Font(None, 70)
lose1 = fonts.render(
    "PLAYER 1 LOSE",
    True,
    (200, 50, 20)
)
lose2 = fonts.render(
    "PLAYER 2 LOSE",
    True,
    (200, 50, 200)
)


game = True
finish = False

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(background)
        ball.reset(window)
        l_paddle.reset(window)
        r_paddle.reset(window)

        ball.update(window)
        ball.is_collided(r_paddle)
        ball.is_collided(l_paddle)

        l_paddle.l_update(window)
        r_paddle.r_update(window)
        
        if ball.rect.x < l_paddle.rect.x:
            finish = True
            window.blit(lose1, (130, 150))
        if ball.rect.x > r_paddle.rect.x:
            finish = True
            window.blit(lose2, (130, 150))


    clock.tick(60)
    display.update()
