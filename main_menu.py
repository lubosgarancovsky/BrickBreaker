import pygame
import texts


class Menu:
    def __init__(self):
        self.btnWidth = 200
        self.btnHeight = 50
        self.inMenu = True
        self.startBtn = pygame.Rect(200, 400, self.btnWidth, self.btnHeight)
        self.exitBtn = pygame.Rect(500, 400, self.btnWidth, self.btnHeight)
        self.menu_BG = pygame.image.load("Assets/menu_bg.png").convert_alpha()
        self.start_img = pygame.image.load("Assets/play_btn.png").convert_alpha()
        self.exit_img = pygame.image.load("Assets/exit_btn.png").convert_alpha()
        self.text_display = texts.Texts()
        self.AUTHOR_TEXT = self.text_display.author_font.render("Lubos Garancovsky -- 3. 2. 2022",False, (255, 255, 255))
        

    def draw(self, surface, color, FPS):
        run = True
        clock = pygame.time.Clock()
        while run:
            surface.fill(color)
            clock.tick(FPS)
            surface.blit(self.menu_BG,(0,0))
            surface.blit(self.AUTHOR_TEXT,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] >= 200 and mouse[0] <= 400 and mouse[1] >= 400 and mouse[1] <= 450:
                        self.inMenu = False
                    if mouse[0] >= 500 and mouse[0] <= 700 and mouse[1] >= 400 and mouse[1] <= 450:
                        pygame.quit()
                    
            
            self.draw_buttons(surface)
            
            

            if not self.inMenu:
                break

            pygame.display.update()
    
    def draw_buttons(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.startBtn)
        pygame.draw.rect(surface, (255, 255, 255), self.exitBtn)
        surface.blit(self.start_img, (self.startBtn.x, self.startBtn.y))
        surface.blit(self.exit_img, (self.exitBtn.x, self.exitBtn.y))