import pygame
import os
from PIL import Image

WIDTH, HEIGHT, = 850, 950
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shooters")

GLITTER = (240, 232, 255) # (RED, GREEN, BLUE)

SHIP_WIDTH, SHIP_HEIGHT = 100, 100

def sketch_window(red, blue):
    WIN.fill(GLITTER)
    WIN.blit(BLUE_STARFOX_ROTATE, (blue.x, blue.y))
    WIN.blit(RED_STARFOX_ROTATE, (red.x, red.y))
    pygame.display.update()
    

FPS = 60

BLUE_STARFOX_IMAGE = pygame.image.load(
os.path.join('stuffies', 'star fox.png'))
BLUE_STARFOX_ROTATE = pygame.transform.rotate(pygame.transform.scale(
    BLUE_STARFOX_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT)), 270)
RED_STARFOX_IMAGE = pygame.image.load(
    os.path.join('stuffies', 'star wolf.png'))
RED_STARFOX_ROTATE = pygame.transform.rotate(pygame.transform.scale(
    RED_STARFOX_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT)), 270)


def main():
    red = pygame.Rect(375, 25, SHIP_WIDTH, SHIP_HEIGHT)
    blue = pygame.Rect(400,825, SHIP_WIDTH, SHIP_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                
        sketch_window(red, blue)
        
        
    
    pygame.quit()

if __name__ == "__main__":
    main()