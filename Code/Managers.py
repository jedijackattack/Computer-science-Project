import pygame
import math
import random
import Code.Entity as Entity
import Code.Component as Component
import xml.etree.ElementTree as ET
import asyncio
import os


class TankStatManager(object):

    def __init__(self):
        self.Tanks = []
        
        self.TankTypes = {}
        
        # Name: HP, Armour, FirePower, Range, MoveSpeed, ConsumptionRate
        self.DisplayStats = {}
        
        pass

    def CreateTankTypes(self,Name,HP,Armour,FirePower,Range,MoveSpeed,ConsumptionRate):
        self.TankTypes[Name] = (int(HP),int(Armour),int(FirePower),int(Range),int(MoveSpeed),int(ConsumptionRate))
        pass

    def AddTank(self, Type, PlayerID:int = 0, Pos = (0,0)):
        p = Component.Position(Pos[0],Pos[1])
        r = Component.RendererClient()
        g = Component.Gamestats(self.TankTypes[Type])
        t = Component.Tank(Type,g)
        player = Component.PlayerRef(PlayerID)
        self.Tanks.append(Entity.Entity(p,r,g,t,player))
        
        pass

    def CreateTankManagerTypes(self, Battle):
        TankList=Battle[2]
        
        for TankTYPE in TankList:
            attributes = []
            for data in TankTYPE:
                attributes.append(data.text)
                
            self.CreateTankTypes(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4],attributes[5],attributes[6])

        pass

    def GenTanks(self,Battle):
        Tankset = Battle[3]

        for tank in Tankset:
            att = []
            for data in tank:
                att.append(data.text)
                pass
            self.AddTank(att[3],int(att[2]),(int(att[0]),int(att[1])))


    def RemoveDeadTanks(self):
        for i in self.Tanks:
            t= i.GetComponentFromType(Component.Gamestats)
            if(t.HP <= 0 ):
                self.Tanks.remove(i)



###################################################################################

#THIS IS A DIFFERENT CLASS
##################################################################################


class TileWorldManager(object):

    def __init__(self):
        self.Tiles = []
        self.TileTypes = {}
        self.ReaderRecord = {}
        
        # Name: Walkable / MoveCost / AttackBonus / DefenceBonus / img
        pass

    def CreateTileTypes(self, Name:str, Walkable:bool = True, MoveCost:int = 1, AttackBonus:int = 0, DefenceBonus:int = 0,id:str = "!"):

        self.TileTypes[Name] = (bool(Walkable), int(MoveCost), int(AttackBonus), int(DefenceBonus))
        self.ReaderRecord[Name] = (id)
        pass

    def AddTile(self, Tipe:str, x:int = 0, y:int = 0):

        p = Component.Position(x,y)
        t = Component.Tile(Tipe)
        r = Component.RendererClient(None,None,pygame.math.Vector2(54,54))
        E = Entity.Entity(p,t,r)
        self.Tiles.append(E)
        pass


    def CreateTileManagerTypes(self, Battle):
        TileList=Battle[1]
        
        for TileTYPE in TileList:
            attributes = []
            for data in TileTYPE:
                attributes.append(data.text)
                
            self.CreateTileTypes(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4],TileTYPE.attrib["id"])

        pass

    def ReadMAP(self,Battle):
        
        MAP = Battle[0].text
        MAP = MAP.split("\n")
        
        for i in range(0,len(MAP)-1):
            MAP[i]=MAP[i].strip("\n")
            MAP[i]=MAP[i].strip(" ")
            MAP[i]=MAP[i].strip(" ")
            MAP[i]=MAP[i].strip("\t")
            
            if(len(MAP[i]) != 20):
                MAP.pop(i)
            
        CorrectSize = True
        if(len(MAP) != 20):
            CorrectSize = False
        for i in MAP:
            if(len(i) != 20):
                CorrectSize = False

        if(CorrectSize == False):
            print("This file is not correctly formatted and may be corrupt.")
            exit()
        self.CreateMAPTiles(MAP,20,20)

    def CreateMAPTiles(self,MAP,Xsize,Ysize):
        for y in range(0,Ysize):
            for x in range(0,Xsize):
                self.AddTile(MAP[y][x],x,y)
                pass
    
    

    
        

