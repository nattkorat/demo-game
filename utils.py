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

class Ball(GameSprite):
    def __init__(self, image, x, y, w, h, speed=0):
        super().__init__(image, x, y, w, h, speed)
        self.speed_x = self.speed
        self.speed_y = self.speed
        self.h = h
        self.w = w

    def update(self, window: pygame.surface):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.y > window.get_size()[1] - self.h or self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.x > window.get_size()[0] - self.w or self.rect.x <= 0:
            self.speed_x *= -1
    
    def is_collided(self, object: pygame.Surface):
        if pygame.sprite.collide_rect(self, object):
            self.speed_x *= -1


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
    
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def l_update(self, window: pygame.Surface):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[pygame.K_s] and self.rect.y < window.get_size()[1] - self.h:
            self.rect.y += 5
    
    def r_update(self, window: pygame.Surface):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.y < window.get_size()[1] - self.h:
            self.rect.y += 5
