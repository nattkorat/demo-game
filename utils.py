from random import randint
import pygame

class GameSprite(pygame.sprite.Sprite):
    """
    GameSprite

    The base custom sprite game.
    
    """
    def __init__(self, image, x, y, w, h, speed = 0):
        super().__init__() # forgot here
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    bullets = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        
        if keys[pygame.K_SPACE]:
            self.fire()
            fire_sound = pygame.mixer.Sound("fire.ogg")
            fire_sound.set_volume(0.15)
            fire_sound.play()
