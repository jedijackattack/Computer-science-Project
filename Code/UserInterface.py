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

    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 72)
    FPS = 60
    text = font.render("Hello, World", True, (0, 128, 0))
    Update = 0
    GameWindow = GameRenderer.GameRender(0,0,720,720,36)
    b = Button(pygame.math.Vector2(720,100),pygame.math.Vector2(200,100),"Plains-1.png","TEST TEXT","arial")
    while running:
     
        screen.blit(GameWindow.RenderMap(sim.MapManager),(GameWindow.pos))
        
        screen.blit(GameWindow.RenderTanks(sim.TankManager),(GameWindow.pos))

        #DisplayFPS = font.render(str(clock.get_fps())[0:2],True,(0,0,0))
        DisplayFPS = font.render(str(round(clock.get_fps())),True,(0,0,0))
        screen.blit(DisplayFPS,(0,0))
        screen.fill((114, 57, 8),((720,0),(1280-720,720)))
        b.draw(screen)
        pygame.display.flip()
           # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        
                
        if(Update == 60):
            #sim.Attack(sim.TankManager.Tanks[0],sim.TankManager.Tanks[1])
            print(sim.TankManager.GetTankPos(pygame.math.Vector2(2,2)),"GOT IT")
            sim.InputActionCommand("TANK01 MOVE 2,4")
            sim.InputActionCommand("TANK00 MOVE 3,1")
            
            sim.EndTurn()
            GameWindow.MapRendered = False
            Update =0
            print("update")
        else:
            Update+=1
        clock.tick(FPS+1)
        

class Button(object):
    FONTS = {}
    TEXTURES ={}
    basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    GraphicsPath = os.path.join(basepath,"graphics")
    
    def __init__(self,POS,Size,texture,text,fontt):
        self.POS = POS
        self.Size = Size
        self.texture = texture
        self.text = Button.textcreate(text,fontt)
        self.fontt = fontt
        pass

    def draw(self,screen):
        screen.blit(Button.TEXTURES[self.texture],self.POS)
        screen.blit(self.text ,self.POS)





    @staticmethod
    def textcreate(text,font):
        Button.CreateFont(font)
        img = Button.FONTS[font]
        print(img)
        t = img.render(text ,True, (0, 0, 0))
        return t
    
    @staticmethod
    def CreateTexture(texture,Size):
        i = texture+Size
        if(texture not in Button.TEXTURES):
            Button.LoadTexture(texture,Size)

    @staticmethod
    def LoadTexture(texture,Size):
        name = texture+Size
        TexturePath = os.path.join(Button.GraphicsPath,TextureName)
        RawImage = pygame.image.load(TexturePath).convert()
        ConvertedImage = pygame.transform.scale(RawImage,Size)
        self.Textures[name] = ConvertedImage
                    
    @staticmethod
    def CreateFont(fontt):
        if(fontt not in Button.FONTS):
            Button.Loadfont(fontt)

    @staticmethod
    def Loadfont(fontt):
        i = pygame.font.SysFont(fontt, 72)
        Button.FONTS[fontt] = i

        
