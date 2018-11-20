import pygame
import math
import random
import Code.Entity as Entity
import Code.Component as Component

class TankStatManager(object):

    def __init__(self):
        self.Tanks = []
        
        self.TankTypes = {"T34/75":(3,3,3,5,4,5),
                          "Panzer II":(2,1,1,3,5,2),
                          "Panzer III": (3,2,2,4,4,3)}
        
        # Name: HP, Armour, FirePower, Range, MoveSpeed, ConsumptionRate
        self.DisplayStats = {}
        pass

    def CreateTankTypes(self):
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


class TileWorldManager(object):

    def __init__(self,Surface):
        self.Tiles = []
        self.TileTypes = {}
        self.Surface = Surface
        
        # Name: Walkable / MoveCost / AttackBonus / DefenceBonus / img
        pass

    def CreateTileType(self, Name:str, Walkable:bool = True, MoveCost:int = 1, AttackBonus:int = 0, DefenceBonus:int = 0):

        Stats = (Walkable, MoveCost, AttackBonus, DefenceBonus)
        self.TileTypes.update({Name:Stats})
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

    

    
        

