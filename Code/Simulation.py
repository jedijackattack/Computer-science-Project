import pygame
import math
import random
import Code.Entity as Entity
import Code.Component as Component
import Code.Managers as Managers
import xml.etree.ElementTree as ET
import os

class Simulation(object):

    def __init__(self,Simdata,Randomval:int = 0):
        #Init the variables the sim uses
        self.TURN = 0
        self.RandomQueue = []
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
        
        if(self.PlayerCount <= 1):
            print("ERROR FILE FORMAT CORRUPTED")
            exit()
            
        self.CurrentPlayer = 0
        self.CurrentPlayerTanks = []
        self.CurrentPlayerTankActions = []
        del self.Battle
        self.EndTurn()
        

        

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
        self.TURN +=1
        print("DEBUG: {0} TURN INPUT ex{1}".format(self.CurrentPlayer,self.TURN))
        PlayerPieces = self.GetPlayerTanks(self.CurrentPlayer)
        PlayerAction = []
        
        for i in PlayerPieces:
            PlayerAction.append(False)

            
        self.CurrentPlayerTanks = PlayerPieces
        self.CurrentPlayerTankActions = PlayerAction
        pass
    

    def EndTurn(self):
        self.NextPlayer()
        self.TankManager.RemoveDeadTanks()
        self.GetPlayerTanks(self.CurrentPlayer)
        self.DefineActions()
        c = self.CheckForWin()
        print("win condition met {0}".format(c))
        print(self.CurrentPlayerTanks)
        print(self.CurrentPlayerTankActions)
        self.RandomQueue = self.GenerateRandom()
        print(self.RandomQueue)

    def GenerateRandom(self):
        
        random.seed(self.PlayerCount*(self.MainRanVal+self.TURN))

    def CheckForWin(self):
        out = []
        for i in range(1,self.PlayerCount):
            if(len(self.GetPlayerTanks(i)) <=0):
                out.append(i)
        if(len(out) <= 0):
            return False
        else:
            return out

    @staticmethod
    def Attack(Attacker,Defender,TileManager):
        
        AttackStats = Attacker.GetComponentFromType(Component.Gamestats)
        DefenedStats = Defender.GetComponentFromType(Component.Gamestats)
        AttackPOS = Attacker.GetComponentFromType(Component.Position)
        DefendPOS = Defender.GetComponentFromType(Component.Position)
        Distance = AttackPOS.pos.distance_to(DefendPOS.pos)
        print(DefendPOS.pos)
        DefendTile = TileManager.GetTile(DefendPOS.pos)
        AttackTile = TileManager.GetTile(AttackPOS.pos)

        print(DefendTile)
        print(AttackTile)

        
        if(Distance <= AttackStats.MaxRange):
            
            AttackSuccesses = 0
            for i in range(0,AttackStats.FirePower):
                x = random.randint(1,6)
                if(x >= 5):
                    AttackSuccesses +=1
                    
            DefenceSuccesses = 0
            for i in range(0,DefenedStats.Armour):
                x = random.randint(1,6)
                if(x >= 5):
                    DefenceSuccesses +=1

            damage =AttackSuccesses - DefenceSuccesses
            if(damage > 0):
                Defender.GetComponentFromType(Component.Gamestats).HP -= damage
            print(damage,AttackSuccesses,DefenceSuccesses,Defender.GetComponentFromType(Component.Gamestats).HP)
        else:
            print("missed")
        
        
    @staticmethod
    def Move(Mover,POS):
        pass
