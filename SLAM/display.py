import pygame
pygame.init()
class Display(object):
    def __init__(self,W,H):
        self.surface = pygame.Surface((W,H))
        self.display = pygame.display.set_mode((W,H))
    def paint(self,img):
        pygame.pixelcopy.array_to_surface(self.surface,img.swapaxes(0,1))
        



        self.display.blit(self.surface,(0,0))
        pygame.display.update()




