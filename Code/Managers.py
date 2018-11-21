import pygame
import math
import random
import Code.Entity as Entity
import Code.Component as Component

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
        print(p)
        player = Component.PlayerRef(PlayerID)
        self.Tanks.append(Entity.Entity(p,r,g,t,player))
        
        pass





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

    def ReadMAP(self,MapPath):
        pass

    

    
        

