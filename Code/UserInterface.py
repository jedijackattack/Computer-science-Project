import pygame
import time
import math
import os
import sys
import Code.Simulation as Simulation
import Code.Component as Component
import Code.Entity as Entity
import Code.Managers as Managers
import Code.GameRenderer as GameRenderer
import random

def main(sim):

    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("minimal program")
    basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(basepath)
    GraphicsPath = os.path.join(basepath,"graphics")
    PanzerPath = os.path.join(GraphicsPath,"Panzer3Pixel.png")
    panzer = pygame.image.load(PanzerPath).convert()
    panzer2 = pygame.transform.scale(panzer,(36,18))

    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 72)
    FPS = 60
    text = font.render("Hello, World", True, (0, 128, 0))
    Update = 0
    GameWindow = GameRenderer.GameRender(0,0,720,720,36)
    GW = GameWindow.RenderMap(sim.MapManager)
    while running:
        """
        for y in range(0,20):
            for x in range(0,20):
                i = sim.MapManager.Tiles[y*20+x]
                #print(i)
                TYPE = i.GetComponentFromType(Component.Tile).TYPE
                #print(TYPE)
                if(TYPE == "."):
                    screen.fill((0,255,0),(x*36,y*36,36,36))
                elif (TYPE == "#"):
                    screen.fill((0,0,255),(x*36,y*36,36,36))
                elif (TYPE == "H"):
                    screen.fill((128,128,128),(x*36,y*36,36,36))
        """
        
        
        
        #screen.fill((255,255,255))
        #print(Update)
        if(Update %1 == 0):
            GW = GameWindow.RenderMap(sim.MapManager)
        
        screen.blit(GW,(GameWindow.pos))
        """
        screen.blit(panzer,(50,50))
        for x in range(0,1200,36):
            screen.blit(panzer2,(x,550))
        """
        #print(clock.get_fps())
        for tank in sim.TankManager.Tanks:
            pos = tank.GetComponentFromType(Component.Position).pos
            screen.blit(panzer2,(pos*36))
        #DisplayFPS = font.render(str(clock.get_fps())[0:2],True,(0,0,0))
        DisplayFPS = font.render(str(clock.get_fps()),True,(0,0,0))


        screen.blit(DisplayFPS,(0,0))


        #pygame.gfxdraw.textured_polygon([(100,400),(1200,400),(100,900),(1200,900)],pazner)
        
        pygame.display.flip()
           # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        if(Update == 60):
            sim.Attack(sim.TankManager.Tanks[0],sim.TankManager.Tanks[1])
            sim.EndTurn()
            Update =0
        else:
            Update+=1
        clock.tick(FPS+1)
        
    exit()
"""
if __name__=="__main__":
    # call the main function
    main()
"""
