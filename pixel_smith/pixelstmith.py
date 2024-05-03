import pygame 
import sys

class Game:
    def __init__(self):
        
            pygame.init()

            pygame.display.set_caption('pixelsmith')
            self.screen = pygame.display.set_mode((190, 180))
            self.clock = pygame.time.Clock()
            self.img = pygame.image.load('data/tiles/01_grass_tile.png')
            self.img.set_colorkey((0, 0, 0,))
            self.movment = [False, False]
            self.img_pos = [20, 20]
            self.speed = 3
    def run (self):
            while True:
                self.screen.fill((14, 219, 248))
                self.img_pos[1] += (self.movment[1] - self.movment[0]) * self.speed
                self.screen.blit(self.img, self.img_pos)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            self.movment[0] = True
                        if event.key == pygame.K_s:
                            self.movment[1] = True
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w:
                            self.movment[0] = False
                        if event.key == pygame.K_s:
                            self.movment[1] = False
                    

                pygame.display.update()
                self.clock.tick(60)
Game().run()
