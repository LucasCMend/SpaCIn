import pygame, sys
from stars import Stars
from settings import Settings
class Jogo:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stars_code = True
        self.i = 0
        self.screen = pygame.display.set_mode((750,500))
        self.clock = pygame.time.Clock()
        self.sprite_stars = pygame.sprite.Group()
        self.stars = Stars(self)
    def rodar(self):
        while True:
            self.imagem()
            self.update()
            self.apply_stars()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.movimento(event)
                elif event.type == pygame.KEYUP:
                    self.parado(event)
            self.clock.tick(60)
    def movimento(self,event):
        if event.key == pygame.K_s:
            self.settings.down = 0.25
        elif event.key == pygame.K_w:
            self.settings.up = 0.25
        elif event.key == pygame.K_d:
            self.settings.right = 0.25
        elif event.key == pygame.K_a:
            self.settings.left = 0.25
    def parado(self,event):
        if event.key == pygame.K_s:
            self.settings.down = 0
        elif event.key == pygame.K_w:
            self.settings.up = 0
        elif event.key == pygame.K_d:
            self.settings.right = 0
        elif event.key == pygame.K_a:
            self.settings.left = 0
    def update(self):
        self.sprite_stars.update()
        for star in self.sprite_stars.copy():
            if star.rect.bottom >= self.stars.screen_rect.bottom or star.rect.right >= self.stars.screen_rect.right \
                or star.rect.left <= self.stars.screen_rect.left or star.rect.top <= self.stars.screen_rect.top:
                self._remove_and_add(star)
    def _remove_and_add(self, star):
        self.sprite_stars.remove(star)
        one_star = Stars(self)
        self.sprite_stars.add(one_star)
    def apply_stars(self):
        if self.stars_code:
            self.i += 1
            one_star = Stars(self)
            self.sprite_stars.add(one_star)
            if self.i >= 500:
                self.stars_code = False
    def imagem(self):
        self.screen.fill((0,0,0))
        for star in self.sprite_stars.sprites():
            star.draw_stars()
        pygame.display.flip()
if __name__ == "__main__":
    ai = Jogo()
    ai.rodar()
