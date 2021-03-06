import time
import math
import os
import sys
import Code.Simulation as Simulation
import Code.Component as Component
import Code.Entity as Entity
import Code.Managers as Managers
import random
import pygame


basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
GraphicsPath = os.path.join(basepath,"graphics")

class GameRender(object):

    def __init__(self,x,y,w,h,TileSize = 36):
        self.Textures = {}
        self.pos = (x,y)
        self.size = (w,h)
        
        self.TileSize = TileSize
        self.TileWidth = int(w/TileSize)
        self.TileHeight = int(h/TileSize)
        
       # print((int(self.TileWidth*TileSize),int(self.TileHeight*TileSize)))
       # print(self.size)
       # print(self.TileWidth)
        
        self.BackGround = pygame.Surface((int(self.TileWidth*TileSize),int(self.TileHeight*TileSize)))
        self.MapRendered = False

        #The Colour 255,0,191 or bright hot pink will not be able to be used as it is used to render transparency.
        self.TankScreen = pygame.Surface((int(self.TileWidth*TileSize),int(self.TileHeight*TileSize)))
        self.TankScreen.set_colorkey((255, 0, 191))

        self.Highlights = pygame.Surface((int(self.TileWidth*TileSize),int(self.TileHeight*TileSize)))
        self.Highlights.set_alpha(80)
        

    def RenderMap(self,MapManager):
        if(self.MapRendered == False):
            self.BackGround.fill((255,255,255))
            for y in range(0,self.TileHeight):
                for x in range(0,self.TileWidth):
                    i = MapManager.Tiles[y*20+x]
                    #print(i)
                    TYPE = i.GetComponentFromType(Component.Tile).TYPE
                    #print(TYPE)
                    imager = i.GetComponentFromType(Component.RendererClient)
                    
                    self.BackGround.blit(self.GetTexture(imager.Img,imager.size),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))

                    

                    """
                    if(TYPE == "."):
                        self.BackGround.blit(self.GetTexture("Plains-1.png"),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                        #self.BackGround.fill((0,255,0),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                    elif (TYPE == "#"):
                        self.BackGround.blit(self.GetTexture("River-1.png"),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                        #self.BackGround.fill((0,0,255),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                    elif (TYPE == "H"):
                        self.BackGround.blit(self.GetTexture("Bridge-1.png"),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                        #self.BackGround.fill((128,128,128),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                    """
            self.MapRendered = True
        return self.BackGround


        

    def RenderTanks(self,TankManager):
        self.TankScreen.fill((255, 0, 191))
        for tank in TankManager.Tanks:
            pos = tank.GetComponentFromType(Component.Position).pos
            img = tank.GetComponentFromType(Component.RendererClient).Img
            imgSize = tank.GetComponentFromType(Component.RendererClient).size
            #print(img)
            TTexture = self.GetTexture(img,imgSize)
            self.TankScreen.blit(TTexture,(pos*self.TileSize))
        return self.TankScreen

    def GetTexture(self,TextureName,imgSize):
        
        if(str(TextureName)+str(imgSize) not in self.Textures):
            self.LoadTexture(TextureName,imgSize)
        return self.Textures[str(TextureName)+str(imgSize)]

    def LoadTexture(self,TextureName,imgSize):
        TexturePath = os.path.join(GraphicsPath,TextureName)
        RawImage = pygame.image.load(TexturePath).convert()
        ConvertedImage = pygame.transform.scale(RawImage,(int(self.TileSize*imgSize[0]),int(self.TileSize*imgSize[1])))
        self.Textures[str(TextureName)+str(imgSize)] = ConvertedImage
        pass

    def HighLight(self,ListPOS,colour):
        self.Highlights.fill((0,0,0))
        for i in ListPOS:
            self.Highlights.fill(colour,(i*int(self.TileSize),(int(self.TileSize),int(self.TileSize))))
        
        return self.Highlights

    

    def Update(self,Mousepos,lmousepress,TankManager,MapManager):
        if(Mousepos[0] < self.pos[0]+self.size[0] and Mousepos[0] > self.pos[0]):
            if(Mousepos[1] < self.pos[1]+self.size[1] and Mousepos[1] > self.pos[1]):
                if(lmousepress == 1):
                    displayx = (Mousepos[0]-self.pos[0])//self.TileSize
                    displayy = (Mousepos[1]-self.pos[1])//self.TileSize
                    #print(displayx,displayy)
                    tank = TankManager.GetTankPos(pygame.math.Vector2(displayx,displayy))
                    if(tank!= None):
                        num = TankManager.Tanks.index(tank)
                        out = "TANK"+str(num)
                        return out
                    else:
                        return(displayx,displayy)
        return None
                    

                    


                    
