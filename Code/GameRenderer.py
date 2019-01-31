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



class GameRender(object):

    def __init__(self,x,y,w,h,TileSize = 36):
        self.textures = {}
        self.pos = (x,y)
        self.size = (w,h)
        
        self.TileSize = TileSize
        self.TileWidth = int(w/TileSize)
        self.TileHeight = int(h/TileSize)
        
        print((int(self.TileWidth*TileSize),int(self.TileHeight*TileSize)))
        print(self.size)
        print(self.TileWidth)
        
        self.BackGround = pygame.Surface((int(self.TileWidth*TileSize),int(self.TileHeight*TileSize)))
        self.MapRendered = False

        #The Colour 255,0,191 or bright hot pink will not be able to be used as it is used to render transparency.
        self.TankScreen = pygame.Surface((int(self.TileWidth*TileSize),int(self.TileHeight*TileSize)))
        self.TankScreen.set_colorkey((255, 0, 191))
        
        self.plain = pygame.Surface((TileSize,TileSize))
        self.plain.fill((0,255,0))
        self.bridge = pygame.Surface((TileSize,TileSize))
        self.bridge.fill((128,128,128))
        self.river = pygame.Surface((TileSize,TileSize))
        self.river.fill((0,0,255))
        
        pass

    def RenderMap(self,MapManager):
        if(self.MapRendered == False):
            self.BackGround.fill((255,255,255))
            for y in range(0,self.TileHeight):
                for x in range(0,self.TileWidth):
                    i = MapManager.Tiles[y*20+x]
                    #print(i)
                    TYPE = i.GetComponentFromType(Component.Tile).TYPE
                    #print(TYPE)
                    if(TYPE == "."):
                        self.BackGround.blit(self.plain,(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                        #self.BackGround.fill((0,255,0),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                    elif (TYPE == "#"):
                        self.BackGround.blit(self.river,(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                        #self.BackGround.fill((0,0,255),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                    elif (TYPE == "H"):
                        self.BackGround.blit(self.bridge,(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                        #self.BackGround.fill((128,128,128),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
            self.MapRendered = True
        return self.BackGround
        

    def RenderTanks(self,TankManager,panzer2):
        self.TankScreen.fill((255, 0, 191))
        for tank in TankManager.Tanks:
            pos = tank.GetComponentFromType(Component.Position).pos
            self.TankScreen.blit(panzer2,(pos*self.TileSize))
        return self.TankScreen
