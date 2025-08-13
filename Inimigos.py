import pygame
from random import randint
from pygame.sprite import Sprite

class TiroInimigo(Sprite):
    def __init__(self,ai):
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings
        self.screen_rect = ai.screen.get_rect()
        self.rect = pygame.Rect(-10,-10,4,8)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def atualizar(self):
        self.y += self.settings.vel_tiro
        self.rect.y = self.y
        self.rect.x = self.x
    def desenhe(self):
        pygame.draw.rect(self.screen,(255,0,0),self.rect)

class Inimigos(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings
        self.screen_rect = ai.screen.get_rect()

        self.image = pygame.image.load("imagens/NaveInimiga.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.screen_rect.right - self.rect.width)
        self.rect.y = self.screen_rect.top - 60

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.direita = True
        self.esquerda = False
    
    def update(self):
        self.y += self.settings.vel_alien
        if self.direita:
            self.x += self.settings.vel_lados
        if self.esquerda:
            self.x -= self.settings.vel_lados
        self.rect.y = self.y
        self.rect.x = self.x
    
    def desenhar(self):
        self.screen.blit(self.image, self.rect)

        


        
