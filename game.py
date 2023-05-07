import pygame
import os
from PIL import Image
pygame.font.init()

WIDTH, HEIGHT, = 850, 950
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shooters")

WHITE = (255, 255, 255)
GLITTER = (240, 232, 255) # (RED, GREEN, BLUE)
BLACK = (0, 0, 0)
RED = (242, 74, 48)
BLUE = (29, 190, 240)

LINE = pygame.Rect(0, HEIGHT//2 + 5, WIDTH, 10)

HEALTH_FONT = pygame.font.SysFont('Arial', 40)
WINNER_FONT = pygame.font.SysFont('Arial', 100)

SHIP_WIDTH, SHIP_HEIGHT = 100, 100

def sketch_window(red, blue, blue_bullets, red_bullets, blue_health, red_health):
    WIN.blit(SPACE, (0,0 ))
    pygame.draw.rect(WIN, BLACK, LINE)
    red_health_text = HEALTH_FONT.render("Star Wolf's Health: " + str(red_health), 1, RED)
    blue_health_text = HEALTH_FONT.render("Star fox's Health: " + str(blue_health), 1, BLUE)
    WIN.blit(blue_health_text, (10, HEIGHT//2 + 20))
    WIN.blit(red_health_text, (10, 10))
    WIN.blit(BLUE_STARFOX_ROTATE, (blue.x, blue.y))
    WIN.blit(RED_STARFOX_ROTATE, (red.x, red.y))
    
    
    
    for bullet in blue_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, BLUE, bullet)
    pygame.display.update()
    

FPS = 60
VEL = 5
BULLET_SPD = 15
NUM_BULLETS = 2
BLUE_HIT = pygame.USEREVENT + 1 
RED_HIT = pygame.USEREVENT + 2

BLUE_STARFOX_IMAGE = pygame.image.load(
os.path.join('stuffies', 'star fox.png'))
BLUE_STARFOX_ROTATE = pygame.transform.rotate(pygame.transform.scale(
    BLUE_STARFOX_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT)), 270)
RED_STARFOX_IMAGE = pygame.image.load(
    os.path.join('stuffies', 'star wolf.png'))
RED_STARFOX_ROTATE = pygame.transform.rotate(pygame.transform.scale(
    RED_STARFOX_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('stuffies', 'space.png')), (WIDTH, HEIGHT))


def blue_key_movement(press_keys, blue):
    if press_keys[pygame.K_a] and blue.x - VEL > 0: #left
        blue.x -= VEL
    if press_keys[pygame.K_d] and blue.x + VEL + blue.width < WIDTH: #right
        blue.x += VEL
    if press_keys[pygame.K_w] and blue.y - VEL > HEIGHT/2 + 10: #up
        blue.y -= VEL
    if press_keys[pygame.K_s] and blue.y + VEL + blue.height < HEIGHT: #down
        blue.y += VEL 

def red_key_movement(press_keys, red):
    if press_keys[pygame.K_LEFT] and red.x - VEL > 0 - 15: #left
        red.x -= VEL
    if press_keys[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #right
        red.x += VEL
    if press_keys[pygame.K_UP] and red.y - VEL > 0: #up
        red.y -= VEL
    if press_keys[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT/2 + 15: #down
        red.y += VEL

def manage_bullets(blue_bullets, red_bullets, blue, red):
    for bullet in blue_bullets:
        bullet.y -= BULLET_SPD
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            blue_bullets.remove(bullet)
        elif bullet.y < 0:
            blue_bullets.remove(bullet)
        
            
    for bullet in red_bullets:
        bullet.y += BULLET_SPD
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            red_bullets.remove(bullet)
        elif bullet.y > HEIGHT:
            red_bullets.remove(bullet)

def sketch_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT
                         /2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(375, 25, SHIP_WIDTH, SHIP_HEIGHT)
    blue = pygame.Rect(400,825, SHIP_WIDTH, SHIP_HEIGHT)
    
    blue_bullets = []
    red_bullets = []
    
    red_health = 3
    blue_health = 3
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(blue_bullets) < NUM_BULLETS:
                    bullet = pygame.Rect(
                        blue.x + blue.width//2 + 4, blue.y, 2, 50
                    )
                    blue_bullets.append(bullet)

                if event.key == pygame.K_k and len(red_bullets) < NUM_BULLETS:
                    bullet = pygame.Rect(
                        red.x + red.width//2 + 9, red.y + red.height//2, 2, 50
                    )
                    red_bullets.append(bullet)
            
            if event.type == RED_HIT:
                red_health -= 1
                
            if event.type == BLUE_HIT:
                blue_health -= 1
        
        winner_text = ""
        if red_health <= 0:
            winner_text = "Star Fox Wins!"
            
        if blue_health <= 0:
            winner_text = "Star Wolf Wins!"
            
        if winner_text != " ":
            sketch_winner(winner_text)
            break
            
        press_keys = pygame.key.get_pressed()
        blue_key_movement(press_keys, blue)
        red_key_movement(press_keys, red)
        manage_bullets(blue_bullets, red_bullets, blue, red)
        sketch_window(red, blue, red_bullets, blue_bullets, blue_health, red_health)
        
        
    
    main()

if __name__ == "__main__":
    main()