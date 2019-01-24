import pygame
import time
import math
import os
import sys

def main():

    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("minimal program")
    basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(basepath)
    fullpath = os.path.join(basepath,"graphics/PKW3.jpg")
    print(fullpath)
    panzer = pygame.image.load(fullpath).convert()

    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((255,255,255))
        screen.blit(panzer,(50,50))

        #pygame.gfxdraw.textured_polygon([(100,400),(1200,400),(100,900),(1200,900)],pazner)
        
        pygame.display.flip()
           # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                sys.exit()
        clock.tick(60)
                

if __name__=="__main__":
    # call the main function
    main()
    
