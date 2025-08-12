from random import randint
from pygame.sprite import Sprite
import pygame

class Asteroide(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.settings = ai.settings
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.medida = randint(1,4)

        self.image = pygame.image.load("imagens/asteroide.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(40*self.medida,40*self.medida))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.screen_rect.right)
        self.rect.y = self.screen_rect.top - 200
        self.y = float(self.rect.y)

    def atualizar(self):
        self.y += self.settings.up
        self.rect.y = self.y

    def desenhar(self):
        self.screen.blit(self.image, self.rect)