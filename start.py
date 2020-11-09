import pygame
import time
import random
from RayCaster import whole
pygame.init()
 
display_width = 1000
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,180,0)
block_color = (53,115,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Proyecto 2 Graficas')
clock = pygame.time.Clock()
 

 


 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 

    
    
 

    
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    oneclick = 0
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None and oneclick == 0:
            action()
            oneclick += 1         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
def quitgame():
    pygame.quit()
    quit()

def game_intro(action):
    pygame.mixer.music.load('coffin.wav')
    #pygame.mixer.music.play(-1)
    
    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("RayTracing", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("INICIAR",150,450,100,50,green,bright_green,action)
        button("SALIR",1050,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        

    
game_intro(whole)
    

  

