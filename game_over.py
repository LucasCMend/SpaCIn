import pygame

class Over:
    def __init__(self, ai):
        super().__init__()
        self.settings = ai.settings
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()

        fonte = pygame.font.SysFont('Pixel', 50)
        texto = "Game Over"
        self.expressao = fonte.render(texto, True, (255,255,255))
        self.retangulo = self.expressao.get_rect(center=(375, 250))
        self.som_gameover = "imagens/game-over-arcade.mp3"

    def tocar_musica(self):
        pygame.mixer.music.load(self.som_gameover)
        pygame.mixer.music.play(0)
        
        

    def desenhar(self):
        self.screen.blit(self.expressao, self.retangulo)