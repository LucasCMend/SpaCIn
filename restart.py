import pygame

class Restart:
    def __init__(self, ai):
        self.settings = ai.settings
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.image = pygame.image.load("imagens/reinicia.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.rect.y += 50

    def desenhar(self):
        self.screen.blit(self.image,self.rect)