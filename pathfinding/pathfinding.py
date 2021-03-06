import pygame
W = 1920//2
H = 1080//2

color = (0,0,0)
fill = (255,255,255)
def main():
    global surface

    pygame.init()
    surface = pygame.display.set_mode((W,H))
    surface.fill(fill)
    while True:
        drawGrid()

def drawGrid():
    blocksize = 20
    for x in range(W):
        for y in range(H):
            rect = pygame.Rect(x*blocksize, y*blocksize, blocksize, blocksize)
            pygame.draw.rect(surface, color, rect, 1)
            
    pygame.display.update()
main()
