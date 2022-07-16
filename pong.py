import pygame, math
import time

pygame.init()

ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

FENSTERBREITE = 1200
FENSTERHOEHE = 900


screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))

pygame.display.set_caption("Simple Pong Game")


clock = pygame.time.Clock()

ballpos_x = 300
ballpos_y = 230

player_x = 20
player_y = 250
BALL_DURCHMESSER = 20

bewegung_x = 10
bewegung_y = 10
spielaktiv = True
def restart():
    spielaktiv = False

counter = 0
font = pygame.font.SysFont('Consolas', 30)

while spielaktiv:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False

   

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_w]: 
        player_y -= 14 
    if keys[pygame.K_s]: 
        player_y += 14 
   
    screen.fill(SCHWARZ)

  
    pygame.draw.ellipse(screen, WEISS, [ballpos_x, ballpos_y, BALL_DURCHMESSER, BALL_DURCHMESSER])
    pygame.draw.rect(screen, WEISS, [player_x, player_y, 15, 150])

 
    ballpos_x += bewegung_x
    ballpos_y += bewegung_y
    
    a = -1
    if ballpos_y > FENSTERHOEHE - BALL_DURCHMESSER or ballpos_y < 0:
        bewegung_y = bewegung_y * a

    if ballpos_x > FENSTERBREITE - BALL_DURCHMESSER or ballpos_x < 0:
        bewegung_x = bewegung_x * a

    
    if player_x < ballpos_x + BALL_DURCHMESSER and player_x + 15 > ballpos_x and player_y < ballpos_y + BALL_DURCHMESSER and 150 + player_y > ballpos_y:
        
        counter = counter +1  
       
        bewegung_x = bewegung_x * a
    
    if ballpos_x == 0:
        print("Your Score was: ", counter)
        time.sleep(3);
        pygame.quit()
        quit()
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()

