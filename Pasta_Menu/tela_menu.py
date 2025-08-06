import pygame, sys

class Menu:

    def __init__(self):
        pygame.init()
        #tela
        self.screen = pygame.display.set_mode((750, 500))
        self.background_image = pygame.image.load("tela_fundo_menu.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (750, 500))
    
        self.title_image = pygame.image.load("title_card.png")
        self.title_hover_image = pygame.image.load("title_card_hover.png")
        
        self.title_image = pygame.transform.scale(self.title_image, (400, 100))
        self.title_hover_image = pygame.transform.scale(self.title_hover_image,( 400, 100))

        self.title_rect = self.title_image.get_rect(midtop=(230, 0))
        self.title_hover_rect = self.title_hover_image.get_rect(midtop=(230, 0))

        self.menu_image = pygame.image.load("start.png")
        self.menu_image = pygame.transform.scale(self.menu_image, (200, 100))

        self.menu_hover = pygame.image.load("start_hover.png")
        self.menu_hover = pygame.transform.scale(self.menu_hover, (248, 100))

        self.menu_rect = self.menu_image.get_rect(bottomright=(600, 495))
        self.menu_hover_rect = self.menu_hover.get_rect(bottomright=(600, 495))
        
        self.start = False
        self.story = False

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        if self.title_rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.title_hover_image, self.title_hover_rect)
        else:
            self.screen.blit(self.title_image, self.title_rect)

        
        if self.menu_rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.menu_hover, self.menu_hover_rect)
        else:
            self.screen.blit(self.menu_image, self.menu_rect)


    def run (self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.menu_rect.collidepoint(event.pos):
                        self.start = 'start'
                        return self.start
                    if self.title_rect.collidepoint(event.pos):
                        self.story = 'historia'
                        return self.story


                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw()
            pygame.display.flip()
    
    
if __name__ == "__main__":
        menu = Menu()
        menu.run()