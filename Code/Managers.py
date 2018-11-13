import pygame
import math
import random
import Entity
import Component
import configparser

class TankStatManager(object):

    def __init__(self):
        self.Tanks = {}
        self.TankTypes = {"T34":(3,3,3,5,5,2)}
        # Name: HP, Armour, FirePower, Range, MoveSpeed, ConsumtionRate
        self.DisplayStats = {}
        pass

    def CreateTankTypes(self):
        pass

    def AddTank(self,Type):
        pass


class TileWorldManager(object):

    def __init__(self,Surface):
        self.Tiles = []
        self.TileTypes = {}
        self.Surface = Surface
        
        # Name: Walkable / MoveCost / AttackBonus / DefenceBonus / img
        pass

    def CreateTileType(self, Name:str, Walkable:bool = True, MoveCost:int = 1, AttackBonus:int = 0, DefenceBonus:int = 0, img):

        Stats = (Walkable, MoveCost, AttackBonus, DefenceBonus, img)
        self.TileTypes.update({Name:Stats})
        pass

    def AddTile(self,x:int = 0, y:int = 0,Tipe:str):

        p = Component.Position(x,y)
        t = Component.Tile(Tipe)
        i = self.TileTypes[Tipe]
        r = Component.RendererClient(self.Surface,i[4],pygame.math.Vector2(54,54))
        E = Entity.Entity(p,t,r)
        self.Tiles.append(E)
        pass

    def ReadMAP(self,MapPath):
        pass

    

    
        

