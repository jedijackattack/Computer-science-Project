import pygame
import math
import random
import Code.Entity as Entity
import Code.Component as Component
import Code.Managers as Managers
import xml.etree.ElementTree as ET
import asyncio
import os


class Simulation(object):

    def __init__(self,Simdata,Randomval):
        self.Simdata = Simdata
        self.MainRanVal = Randomval
        self.TankManager = None
        self.MapManager = None
        basepath = os.path.dirname(os.path.realpath(__file__))
        print(basepath)
        self.fullpath = os.path.join(basepath, "Saves\CORE\Battles\\", str(Simdata))
        print(self.fullpath)
        self.Battle = ET.parse(self.fullpath)
        self.Battle = self.Battle.getroot()

        pass

"""
0: is the battle map
1: is the tile types
2: is the tank types
3: is the position of the tanks and there type

"""

    def GetRandom(self):
        random.seed(self.MainRanVal)
        x = random.randint(1,6)
        self.MainRanVal = x
        return x

    def CreateTankManagerTypes(self):

        pass