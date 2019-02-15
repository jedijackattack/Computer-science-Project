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

def main(sim,FPS:int = 60):

    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("minimal program")

    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 72)
    Update = 0
    LastSelected = ""
    Selected = ""
    State = "None"
    GameWindow = GameRenderer.GameRender(0,0,720,720,36)
    mouse = pygame.mouse.get_pos()
    b = Button(pygame.math.Vector2(720,100),(200,100),"Button-1.png","MOVE","arial",M)
    while running:
        ###INPUT###
           # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        mousepos = pygame.mouse.get_pos()
        LeftMousePressed = pygame.mouse.get_pressed()[0]


        ############
        ############
     
        screen.blit(GameWindow.RenderMap(sim.MapManager),(GameWindow.pos))
        
        screen.blit(GameWindow.RenderTanks(sim.TankManager),(GameWindow.pos))
        

        g=GameWindow.Update(mousepos,LeftMousePressed,sim.TankManager,sim.MapManager)
        if(g!=None):
            #print(g)
            Selected = g
            
        #DisplayFPS = font.render(str(clock.get_fps())[0:2],True,(0,0,0))
        DisplayFPS = font.render(str(round(clock.get_fps())),True,(0,0,0))
        screen.blit(DisplayFPS,(0,0))
        screen.fill((114, 57, 8),((720,0),(1280-720,720)))
        MoveState = b.Update(mousepos,LeftMousePressed)
        if(MoveState != None):
            State = MoveState
            #print(State+"State")
        b.draw(screen)
        
        if(State == "None"):
            if(Selected != ""):
                LastSelected = Selected
                Selected = ""
        elif(State == "MOVE"):
            
            if(Selected != "" and LastSelected != ""):
                print(str(LastSelected) + " MOVE " + str(Selected[0])+","+str(Selected[1]))
                
                sim.InputActionCommand(str(LastSelected) + " MOVE " + str(Selected[0])+","+str(Selected[1]))
                State = "None"
            elif(type(LastSelected) != tuple):
                L = LastSelected.strip("TANK")
                L = int(L)
                t = sim.TankManager.Tanks[L]
                p = t.GetComponentFromType(Component.Position).pos
                movement = t.GetComponentFromType(Component.Gamestats).MoveSpeed
                m = sim.MapManager.AvalibleMovementTiles(p,movement)
                screen.blit(GameWindow.HighLight(m,(255,0,0)),(GameWindow.pos))
                
        if(Update == 20):
            #sim.Attack(sim.TankManager.Tanks[0],sim.TankManager.Tanks[1])
            #sim.InputActionCommand("TANK01 MOVE 2,4")
            #sim.InputActionCommand("TANK00 MOVE 3,1")
            print(str(LastSelected) + " "+str(Selected)+" " +str(State))
            sim.EndTurn()
            GameWindow.MapRendered = False
            Update =0
        else:
            Update+=1
        clock.tick(FPS+1)

############RENDER SCREEN#############
        pygame.display.flip()



########################
class Button(object):
    FONTS = {}
    TEXTURES ={}
    basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    GraphicsPath = os.path.join(basepath,"graphics")
    
    def __init__(self,POS,Size,texture,text,fontt,Function = lambda: print("BUTTON FIRED") ):
        self.POS = POS
        self.Size = Size
        self.texture = texture
        self.text = Button.textcreate(text,fontt,Size)
        self.fontt = fontt
        self.function = Function
        if(Function is callable):
            self.function = Function
        pass

    def draw(self,screen):
        Button.CreateTexture(self.texture,self.Size)
        screen.blit(Button.TEXTURES[self.texture+str(self.Size)],self.POS)
        s = self.text.get_size()
        offset = [0,0]
        offset[0] = (self.Size[0]-s[0])/2
        offset[1] = (self.Size[1]-s[1])/2
        screen.blit(self.text ,(self.POS[0]+offset[0],self.POS[1]+offset[1]))

    def Update(self,MousePos,lmousepress):
        if(MousePos[0] < self.POS[0]+self.Size[0] and MousePos[0] > self.POS[0]):
            if(MousePos[1] < self.POS[1]+self.Size[1] and MousePos[1] > self.POS[1]):
                if(lmousepress == 1):
                    
                    self.texture = "ButtonVeryDark-1.png"
                    return self.function()
                    #print("Function Fired")
                else:
                    self.texture = "ButtonDark-1.png"
            else:
                self.texture = "Button-1.png"
        else:
                self.texture = "Button-1.png"
            


    @staticmethod
    def textcreate(text,font,Size):
        Button.CreateFont(font,Size,text)
        img = Button.FONTS[font+str(Size)]
        t = img.render(text ,True, (0, 0, 0))
        return t
    
    @staticmethod
    def CreateTexture(texture,Size):
        i = texture+str(Size)
        if(texture not in Button.TEXTURES):
            Button.LoadTexture(texture,Size)

    @staticmethod
    def LoadTexture(texture,Size):
        name = texture+str(Size)
        TexturePath = os.path.join(Button.GraphicsPath,texture)
        RawImage = pygame.image.load(TexturePath).convert_alpha()
        ConvertedImage = pygame.transform.scale(RawImage,Size)
        Button.TEXTURES[name] = ConvertedImage
                    
    @staticmethod
    def CreateFont(fontt,Size,text):
        if(fontt+str(Size) not in Button.FONTS):
            Button.Loadfont(fontt,Size,text)

    @staticmethod
    def Loadfont(fontt,Size,text):
        i = 0
        x = 100
        while True:
            i = pygame.font.SysFont(fontt, x)
            if(i.size(text)[0] < Size[0] and i.size(text)[1] < Size[1]):
                break
            x -=5
        Button.FONTS[fontt+str(Size)] = pygame.font.SysFont(fontt, x-5)

def M():
    #print("Move!")
    return "MOVE"
    
    
        
