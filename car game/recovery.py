import pygame
import random
pygame.init()
# GLobel variable 
SCREEN_WIDTH = 580
SCREEN_HIGHT = 650
message= pygame.image.load('sour/img/message.png')
player = pygame.image.load('sour/img/player.jpg')
back = pygame.image.load('sour/img/ba.jpg')
GAME_SPRITES = {}
playerx = 275
playery = 500
display_surface= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
pygame.display.set_caption('road trip')
running= True 
while running:
    # pressed = pygame.key.get_pressed()
    display_surface.blit(back,(0,0))
    display_surface.blit(player,(playerx,playery))
    display_surface.blit(message,(100,40))
    for event in pygame.event.get() :
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT :
            # deactivates the pygame library
            pygame.quit()
            # quit the program.
            quit()
        if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    playerx += 14
                elif event.key==pygame.K_LEFT:
                    playerx -= 14
                elif event.key==pygame.K_UP:
                    playery -= 14
                elif event.key==pygame.K_DOWN:
                    playery += 14   
        # Draws the surface object to the screen.  
    pygame.display.update() 
