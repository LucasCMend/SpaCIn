import pygame

class Dados:
    def __init__(self, ai):
        self.settings = ai.settings
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.fonte = pygame.font.SysFont('Pixel', 25)

    def desenhar(self):
        self.expressao = self.fonte.render(self.settings.texto, True, (255,255,255))
        self.retangulo = self.expressao.get_rect(midtop=(180,10))
        self.screen.blit(self.expressao, self.retangulo)
