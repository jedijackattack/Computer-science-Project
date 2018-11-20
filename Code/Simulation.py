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

    def __init__(self,Simdata,Randomval:int = 0):
        #Init the variables the sim uses
        self.Simdata = Simdata
        self.MainRanVal = Randomval
        self.TankManager = Managers.TankStatManager()
        self.MapManager = None
        self.Battle = None
        # init the path to the sim data
        self.GetSimdata()
        self.CreateTankManagerTypes()

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

    """All of the following functions are to do with loading in data and as such are used in the init method
    to generate the inital simstate for the start of the game. As such """

    def GetSimdata(self):
        basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        print(basepath)
        self.fullpath = os.path.join(basepath, "Saves\CORE\Battles", str(self.Simdata))
        print(self.fullpath)
        self.Battle = ET.parse(self.fullpath)
        self.Battle = self.Battle.getroot()
        pass


    def CreateTankManagerTypes(self):
        TankList=self.Battle[2]
        
        for TankTYPE in TankList:
            attributes = []
            for data in TankTYPE:
                attributes.append(data.text)
                
            self.TankManager.CreateTankTypes(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4],attributes[5],attributes[6])

        pass

