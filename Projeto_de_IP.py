import pygame, sys
from stars import Stars
from settings import Settings
from fundo import Fundo
from ship import Ship
from Inimigos import Inimigos
from Inimigos import TiroInimigo
from coletaveis import Placa
from coletaveis import Combustivel
from game_over import Over
from dados import Dados
from dados import Won

class Jogo:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stars_code = True
        self.inimigos_code = True
        self.i = 0
        self.key = True
        self.primeiro_galao = True
        self.explosao = True
        self.primeira_placa = True
        self.won_game = False
        self.contador = 0
        self.diminui = 0
        self.conta = 0
        self.quantas = 0
        self.quanto = 10
        self.lista = []
        self.screen = pygame.display.set_mode((750,500))
        self.clock = pygame.time.Clock()
        self.sprite_stars = pygame.sprite.Group()
        self.fundo = Fundo(self)
        self.ship = Ship(self)
        self.over = Over(self)
        self.dados = Dados(self)
        self.win = Won(self)
        self.inimigos = pygame.sprite.Group()
        self.tiros = pygame.sprite.Group()
        self.galao = pygame.sprite.Group()
        self.placa = pygame.sprite.Group()
    def rodar(self):
        while True:
            self.imagem()
            if self.key:
                self.update()
                self.remove()
                self.atualizar()
                self.placa_e_combustivel()
                self.apply_inimigos()
                self.apply_stars()
                self.limites()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if self.key:
                        self.movimento(event)
            self.clock.tick(60)
    def limites(self):
        if self.ship.rect.right >= self.ship.screen_rect.right:
             self.settings.d = 0
        if self.ship.rect.left <= self.ship.screen_rect.left:
             self.settings.a = 0
        if self.ship.rect.bottom >= self.ship.screen_rect.bottom:
             self.settings.s = 0
        if self.ship.rect.top <= self.ship.screen_rect.top:
             self.settings.w = 0
    def movimento(self,event):
        if event.key == pygame.K_s:
            self.ship.image = pygame.image.load("imagens/1000102277.png").convert_alpha()
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.settings.right = 0
            self.settings.left = 0
            self.settings.s = 2
            self.settings.w = 0
            self.settings.d = 0
            self.settings.a = 0
        elif event.key == pygame.K_w:
            self.ship.image = pygame.image.load("imagens/1000102277.png").convert_alpha()
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.settings.right = 0
            self.settings.left = 0
            self.settings.w = 2
            self.settings.s = 0
            self.settings.d = 0
            self.settings.a = 0
        elif event.key == pygame.K_d:
            self.ship.image = pygame.image.load("imagens/1000102277.png").convert_alpha()
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.ship.image = pygame.transform.rotate(self.ship.image, -30)
            self.settings.right = 2
            self.settings.left = 0
            self.settings.d = 2
            self.settings.w = 0
            self.settings.s = 0
            self.settings.a = 0
        elif event.key == pygame.K_a:
            self.ship.image = pygame.image.load("imagens/1000102277.png").convert_alpha()
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.ship.image = pygame.transform.rotate(self.ship.image, 30)
            self.settings.left = 2
            self.settings.right = 0
            self.settings.a = 2
            self.settings.w = 0
            self.settings.d = 0
            self.settings.s = 0
    def update(self):
        self.sprite_stars.update()
        for star in self.sprite_stars.copy():
            if star.rect.bottom >= self.ship.screen_rect.bottom or star.rect.right >= self.ship.screen_rect.right \
                or star.rect.left <= self.ship.screen_rect.left or star.rect.top <= self.ship.screen_rect.top:
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
            if self.i >= 1000:
                self.stars_code = False
    def placa_e_combustivel(self):
        self.diminui += 1
        if self.diminui % 200 == 0:
            self.settings.texto = f"Placas: {self.quantas} | Combustível: {self.quanto}"
            self.diminui = 0
            self.quanto -= 1
        if self.quanto == 0:
            self.settings.w = 0
            self.settings.a = 0
            self.settings.s = 0
            self.settings.d = 0
            self.settings.fundo = 0
            self.key = False
        if self.quantas == 20:
            self.settings.w = 0
            self.settings.a = 0
            self.settings.s = 0
            self.settings.d = 0
            self.settings.fundo = 0
            self.key = False
            self.won_game = True
        if self.primeira_placa:
            placa = Placa(self)
            self.placa.add(placa)
            self.primeira_placa = False
        if self.primeiro_galao:
            galao = Combustivel(self)
            self.galao.add(galao)
            self.primeiro_galao = False
        self.placa.update()
        self.galao.update()
        for placa in self.placa.copy():
            if placa.rect.colliderect(self.ship.rect):
                self.quantas += 1
                self.settings.texto = f"Placas: {self.quantas} | Combustível: {self.quanto}"
                som = pygame.mixer.Sound("imagens/pop.mp3")
                som.set_volume(0.3)
                som.play()
                self.placa.remove(placa)
                self.primeira_placa = True
            if placa.y >= self.ship.screen_rect.bottom + 100:
                self.placa.remove(placa)
                self.primeira_placa = True
        for galao in self.galao.copy():
            if galao.rect.colliderect(self.ship.rect):
                self.diminui = 0
                self.quanto += 1
                self.settings.texto = f"Placas: {self.quantas} | Combustível: {self.quanto}"
                som = pygame.mixer.Sound("imagens/plim.mp3")
                som.set_volume(0.3)
                som.play()
                self.galao.remove(galao)
                self.primeiro_galao = True
            if galao.y >= self.ship.screen_rect.bottom + 100:
                self.galao.remove(galao)
                self.primeiro_galao = True
    def apply_inimigos(self):
        if self.inimigos_code:
            self.contador += 1
            if self.contador % 100 == 0:
                inimigo = Inimigos(self)
                self.lista.append(inimigo)
                self.inimigos.add(inimigo)
                self.atirar(inimigo)
            elif self.contador >= (5 * 100):
                self.contador = 0
                self.inimigos_code = False
    def atualizar(self):
        i = 0
        for tiro in self.tiros.copy():
            tiro.atualizar()
            if tiro.rect.colliderect(self.ship.rect):
                self.tiros.remove(tiro)
                self.settings.w = 0
                self.settings.a = 0
                self.settings.s = 0
                self.settings.d = 0
                self.settings.fundo = 0
                self.key = False
            if tiro.y >= self.ship.screen_rect.bottom + 100:
                if self.inimigos.copy():
                    inimigo = self.lista[i]
                    tiro.x,tiro.y = inimigo.x + 25,inimigo.y + 25
            i += 1
    def atirar(self,inimigo):
        som = pygame.mixer.Sound("imagens/tiro.mp3")
        som.set_volume(0.2)
        som.play()
        tiro = TiroInimigo(self)
        tiro.x,tiro.y = inimigo.x + 25,inimigo.y + 25
        self.tiros.add(tiro)
    def remove(self):
        self.inimigos.update()
        if not self.inimigos.copy():
            self.inimigos_code = True
        if self.ship.screen_rect.top <= self.fundo.screen_rect.top:
            self.settings.w = 0
            self.settings.a = 0
            self.settings.s = 0
            self.settings.d = 0
            self.settings.fundo = 0
            self.key = False
        for inimigo in self.inimigos.copy():
            if inimigo.rect.colliderect(self.ship.rect):
                self.inimigos.remove(inimigo)
                self.settings.w = 0
                self.settings.a = 0
                self.settings.s = 0
                self.settings.d = 0
                self.settings.fundo = 0
                self.key = False
            if inimigo.rect.bottom >= self.ship.screen_rect.bottom + 100:
                self.inimigos.remove(inimigo)
            if inimigo.x >= self.fundo.screen_rect.right:
                inimigo.direita = False
                inimigo.esquerda = True
            if inimigo.x <= self.fundo.screen_rect.left:
                inimigo.direita = True
                inimigo.esquerda = False
    def imagem(self):
        self.fundo.blitme()
        for star in self.sprite_stars.sprites():
            star.draw_stars()
        for galao in self.galao.sprites():
            galao.desenhar()
        for placa in self.placa.sprites():
            placa.desenhar()
        for tiro in self.tiros.sprites():
            tiro.desenhe()
        for inimigo in self.inimigos.sprites():
            inimigo.desenhar()
        self.ship.draw()
        if not self.key and not self.won_game:
            if self.explosao:
                som = pygame.mixer.Sound("imagens/explosao.mp3")
                som.set_volume(0.5)
                som.play()
                self.explosao = False
            imagem = pygame.image.load("imagens/explosao.png")
            self.ship.image = pygame.transform.scale(imagem,(100,120))
            self.over.desenhar()
        elif self.won_game:
            self.win.desenhar()
        else:
            self.dados.desenhar()
        pygame.display.flip()
