import pygame, sys
from tela_menu import Menu


def imagens_sequenciais(tela, lista_imagens, avancar_img, avancar_rect, voltar_img, voltar_rect, start_img, start_rect, start_hover_img, start_hover_rect, start):
    idx = 0
    clock = pygame.time.Clock()
    start = False

    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if avancar_rect.collidepoint(event.pos): 
                    idx += 1
                    if idx >= len(lista_imagens):
                        idx = len(lista_imagens) - 1
                elif voltar_rect.collidepoint(event.pos):
                    # if idx > 0:
                        idx -= 1
                        if idx == -1:
                            idx = 0
                            return 'voltar_menu'
                            
                elif idx == len(lista_imagens)-1 and start_hover_rect.collidepoint(event.pos): 
                        return 'start'
                        


        tela.blit(lista_imagens[idx], (0, 0))

        if idx <= 3:
            tela.blit(avancar_img, avancar_rect)
        # if idx > 0:
        tela.blit(voltar_img, voltar_rect)

        
        if idx == len(lista_imagens)-1:
            mouse_pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(mouse_pos):
                tela.blit(start_hover_img, start_hover_rect)
            else:
                tela.blit(start_img, start_rect)
                


        pygame.display.flip()
        clock.tick(60)

classe = Menu()
# historia = classe.story 
start = False
resultado = classe.run()
spacin = None

while True:
    
    if spacin == 'voltar_menu':
        resultado = classe.run()
    elif spacin == 'start':
        resultado = 'start'

    if resultado == 'historia':
        screen = pygame.display.set_mode((750, 500))

        imagens = [
            pygame.image.load("card_1.png"),
            pygame.image.load("card_2.png"),
            pygame.image.load("card_3.png"),
            pygame.image.load("card_4.png"),
            pygame.image.load("card_5.png"),
        ]

        imagens = [pygame.transform.scale(img, (750, 500)) for img in imagens]

        avancar_img = pygame.image.load("avancar.png")
        avancar_img = pygame.transform.scale(avancar_img, (40, 20))  
        avancar_rect = avancar_img.get_rect(topright=(740, 10))

        voltar_img = pygame.image.load("voltar.png")
        voltar_img = pygame.transform.scale(voltar_img, (40, 20))
        voltar_rect = voltar_img.get_rect(topleft=(10, 10))

        start_img = pygame.image.load("start.png")
        start_img = pygame.transform.scale(start_img, (350, 200))
        start_rect = start_img.get_rect(center=(375, 350))

        start_hover_img = pygame.image.load("start_hover.png")
        start_hover_img = pygame.transform.scale(start_hover_img, (398, 200))
        start_hover_rect = start_hover_img.get_rect(center=(375, 350))


        spacin = imagens_sequenciais(screen, imagens, avancar_img, avancar_rect, voltar_img, voltar_rect, start_img, start_rect, start_hover_img, start_hover_rect, start)

            
    elif resultado == 'start':
        start = 'start'
        break