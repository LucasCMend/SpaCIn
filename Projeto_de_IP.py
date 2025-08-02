import pygame, sys
class Jogo:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((500,500))
    def rodar(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
if __name__ == "__main__":
    ai = Jogo()
    ai.rodar()
