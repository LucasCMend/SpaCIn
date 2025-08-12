import pygame,sys

class Final:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((750,500))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.lista = ['imagens/pri.png','imagens/seg.png','imagens/ter.png']
        self.image = pygame.image.load(self.lista[0])
        self.image = pygame.transform.scale(self.image, (self.screen_rect.right, self.screen_rect.bottom))
        self.rect = self.image.get_rect()
        self.avancar = pygame.image.load("Pasta_Menu/avancar.png")
        self.avancar = pygame.transform.scale(self.avancar, (40, 20))  
        self.avancar_rect = self.avancar.get_rect(topright=(740, 10))

    def ativar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.avancar_rect.collidepoint(event.pos):
                        self.lista.pop(0)
                        if not self.lista:
                            sys.exit()
                        self.image = pygame.image.load(self.lista[0])
                        self.image = pygame.transform.scale(self.image, (self.screen_rect.right, self.screen_rect.bottom))
                        carregar = pygame.mixer.Sound("Pasta_Menu/alto.mp3")
                        carregar.play()
            self.screen.blit(self.image,self.rect)
            self.screen.blit(self.avancar,self.avancar_rect)
            pygame.display.flip()
            self.clock.tick(60)