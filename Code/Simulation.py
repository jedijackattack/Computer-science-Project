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
        self.MapManager = Managers.TileWorldManager()
        self.Battle = None
        # init the path to the sim data
        self.GetSimdata()
        self.TankManager.CreateTankManagerTypes(self.Battle)
        self.MapManager.CreateTileManagerTypes(self.Battle)
        self.TankManager.GenTanks(self.Battle)
        self.MapManager.ReadMAP(self.Battle)
        self.PlayerCount = int(self.Battle[4].text)
        
        if(PlayerCount <= 1):
            print("ERROR FILE FORMAT CORRUPTED")
            exit()
            
        self.CurrentPlayer = 0
        self.CurrentPlayerTanks = []
        self.CurrentPlayerTankActions = []
        del self.Battle
        

        

    """
    0: is the battle map
    1: is the tile types
    2: is the tank types
    3: is the position of the tanks and there type
    4: is the player count
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
        self.fullpath = os.path.join(basepath, "Saves\CORE\Battles", str(self.Simdata))
        self.Battle = ET.parse(self.fullpath)
        self.Battle = self.Battle.getroot()
        pass

    def NextPlayer(self):
        if(self.CurrentPlayer >= self.PlayerCount):
            self.CurrentPlayer = 1
        else:
            self.CurrentPlayer +=1
            
    def GetPlayerTanks(self,PlayerNumber):
        out = []
        for i in self.TankManager.Tanks:
            p = i.GetComponentFromType(Component.PlayerRef)
            if(p.player == PlayerNumber):
                out.append(i)
        return out
        

    def DefineActions(self):
        
        print("DEBUG: {0} TURN INPUT ex000001".format(self.CurrentPlayer))
        PlayerPieces = self.GetPlayerTanks(self.CurrentPlayer)
        PlayerAction = []
        
        for i in PlayerPieces:
            PlayerAction.append(0)

            
        self.CurrentPlayerTanks = PlayerPieces
        self.CurrentPlayerTankActions = PlayerAction
        pass

    def EndTurn(self):
        self.NextPlayer()
        self.GetPlayerTanks(self.CurrentPlayer)
        self.DefineActions()
    

