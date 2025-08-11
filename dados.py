import pygame

class Dados:
    def __init__(self, ai):
        self.settings = ai.settings
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.fonte = pygame.font.SysFont('Pixel', 25)

    def desenhar(self):
        self.expressao = self.fonte.render(self.settings.texto, True, (255,255,255))
        self.retangulo = self.expressao.get_rect(midtop=(120,10))
        self.screen.blit(self.expressao, self.retangulo)

class Won:
    def __init__(self, ai):
        self.settings = ai.settings
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        fonte = pygame.font.SysFont('Pixel', 50)
        texto = "Win"
        self.expressao = fonte.render(texto, True, (255,255,255))
        self.retangulo = self.expressao.get_rect(center=(375, 250))

    def desenhar(self):
        self.screen.blit(self.expressao, self.retangulo)