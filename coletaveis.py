import pygame
from pygame.sprite import Sprite
from random import randint

class Placa(Sprite):
    def __init__(self,ai):
        super().__init__()
        self.settings = ai.settings
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()

        self.image = pygame.image.load('imagens/placa.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.screen_rect.right)
        self.rect.y = self.screen_rect.top - 40
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.right
        self.x += self.settings.left
        self.y += self.settings.up

        self.rect.y = self.y
        self.rect.x = self.x

    def desenhar(self):
        self.screen.blit(self.image, self.rect)

class Combustivel(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.settings = ai.settings
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()

        self.image = pygame.image.load("imagens/combustivel.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.screen_rect.right)
        self.rect.y = self.screen_rect.top - 100
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.right
        self.x += self.settings.left
        self.y += self.settings.up

        self.rect.y = self.y
        self.rect.x = self.x

    def desenhar(self):
        self.screen.blit(self.image, self.rect)


