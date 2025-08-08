import pygame
import random

class Placa:
    def __init__(self):
        self.image = pygame.image.load('Projeto_de_IP/ChatGPT Image Aug 7, 2025 at 02_41_11 PM.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 30))
        self.rect = self.image.get_rect()
        self.largura_tela = 750
        self.altura_tela = 500
        self.tempo_geracao = 10000
        self.velocidade.y = 1
        self.placas = []
        self.ultimo_spawn = pygame.time.get_ticks()
        self.contador = 0

    def atualizar(self, jogador):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_spawn > self.tempo_geracao:
            x_spawn = random.randint(0, self.largura_tela - self.image.get_width())
            nova_placa = self.image.get_rect(topleft=(x_spawn, -50))
            self.placas.append(nova_placa)
            self.ultimo_spawn = agora

        novas_placas = []
        for placa in self.placas:
            placa.y += self.velocidade.y

            if placa.y < self.altura_tela and jogador.rect.colliderect(placa):
                self.contador += 1
            elif placa.y < self.altura_tela:
                novas_placas.append(placa)

        self.placas = novas_placas

        if self.contador >= 10:
            return 'Fase concluída'
        return None

    def desenhar(self, tela):
        for placa in self.placas:
            tela.blit(self.image, placa)



class Combustivel(pygame.sprite.Sprite):

    def __init__(self, largura, altura, ai_game):
        super().__init__()

        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("galao_transparente.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(40,45))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura - self.rect.width)
       
        self.rect.y = random.randint(10, 100)

        self.velocidade_y= 3

        if 0 < self.rect.x < largura / 2:
            self.velocidade_x = 3

        elif self.rect.x == largura / 2:
            self.velocidade_x = random.randint(-1, 1)
        else:
            self.velocidade_x = -3