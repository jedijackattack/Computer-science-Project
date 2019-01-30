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
        self.GameScreen = pygame.Surface((int(self.TileWidth*self.size[0]),int(self.TileHeight*self.size[1])))
        self.MapRendered = False
        self.TankScreen = pygame.Surface((int(self.TileWidth*self.size[0]),int(self.TileHeight*self.size[1])))
        self.plain = pygame.Surface((TileSize,TileSize))
        self.plain.fill((0,255,0))
        self.bridge = pygame.Surface((TileSize,TileSize))
        self.bridge.fill((128,128,128))
        self.river = pygame.Surface((TileSize,TileSize))
        self.river.fill((0,0,255))
        
        pass

    def RenderMap(self,MapManager):
        if(self.MapRendered == False):
            self.GameScreen.fill((255,255,255))
            for y in range(0,self.TileHeight):
                for x in range(0,self.TileWidth):
                    i = MapManager.Tiles[y*20+x]
                    #print(i)
                    TYPE = i.GetComponentFromType(Component.Tile).TYPE
                    #print(TYPE)
                    if(TYPE == "."):
                        self.GameScreen.blit(self.plain,(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                        #self.GameScreen.fill((0,255,0),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                    elif (TYPE == "#"):
                        self.GameScreen.blit(self.river,(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                        #self.GameScreen.fill((0,0,255),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                    elif (TYPE == "H"):
                        self.GameScreen.blit(self.bridge,(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
                        #self.GameScreen.fill((128,128,128),(x*self.TileSize,y*self.TileSize,self.TileSize,self.TileSize))
            self.MapRendered = True
        return self.GameScreen
        

    def RenderTanks(self,TankManager,panzer2,screen):
        for tank in TankManager.Tanks:
            pos = tank.GetComponentFromType(Component.Position).pos
            screen.blit(panzer2,(pos*self.TileSize))
        pass
