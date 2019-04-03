import pygame
import math
import random
import Code.Entity as Entity
import Code.Component as Component
import Code.Managers as Managers
import Code.BOT as BOT
import xml.etree.ElementTree as ET
import os

class Simulation(object):

    def __init__(self,Simdata,Randomval:int = random.randint(0,10000000000000),Users = ["HUMAN","BOT"],save=[],Senario = ""):
        #Init the variables the sim uses
        self.Users = Users
        self.Senario = Senario
        self.TURN = 0
        self.RandomQueue = []
        self.Simdata = Simdata
        self.MainRanVal = Randomval
        if(self.MainRanVal ==0):
            self.MainRanVal = random.Randint(0,1000000000000000)
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
        self.Victory = None
        
        if(self.PlayerCount <= 1):
            print("ERROR FILE FORMAT CORRUPTED")
            exit()
        if(self.PlayerCount != len(Users)):
            print("ERROR INCORRECT AI PLAYER ASSIGNMENT")
            exit()
        self.CurrentPlayer = 0
        self.CurrentPlayerTanks = []
        self.CurrentPlayerTankActions = []
        self.commands = save
        self.replay = False
        if(len(self.commands)>0):
            self.replay = True

        del self.Battle
        self.EndTurn()
        if(self.replay == True):
            for i in self.commands:
                self.InputActionCommand(i)
                pass
        self.replay = False

        

    """
    0: is the battle map
    1: is the tile types
    2: is the tank types
    3: is the position of the tanks and there type
    4: is the player count
    """

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
        #print("DEBUG: {0} TURN INPUT ex{1} \n Player {2}".format(self.CurrentPlayer,self.TURN,self.CurrentPlayer))
        PlayerPieces = self.GetPlayerTanks(self.CurrentPlayer)
        PlayerAction = []
        
        for i in PlayerPieces:
            PlayerAction.append(i)

            
        self.CurrentPlayerTanks = PlayerPieces
        self.CurrentPlayerTankActions = PlayerAction
        pass
    

    def EndTurn(self):
        self.NextPlayer()
        self.TankManager.RemoveDeadTanks()
        self.GetPlayerTanks(self.CurrentPlayer)
        self.DefineActions()
        c = self.CheckForWin()
        #print("win condition met {0}".format(c))

        if(c != False):
            self.Victory = c
        else:
            if(self.replay == False):
                self.save()


        self.RandomQueue = self.GenerateRandom()
        #print(self.RandomQueue)

        if(self.Users[self.CurrentPlayer-1] == "BOT" and self.replay == False):
            actions = BOT.botAction(self.TankManager,self.MapManager,self.CurrentPlayerTanks)
            for action in actions:
                self.InputActionCommand(action)
                #print(action)



    def GenerateRandom(self):
        
        random.seed(hash(self.PlayerCount*(self.MainRanVal+self.TURN)))

    def CheckForWin(self):
        out = []
        for i in range(0,self.PlayerCount):
            if(len(self.GetPlayerTanks(i+1)) >=1):
                out.append(i+1)
        if(len(out) > 1):
            return False
        else:
            return out

    def Attack(self,Attacker,Defender):
        """This function is the attack method for the game and works as such
        Grab all of of the needed information at the start of the attack.
        Check if the attack is in range. if it is add the attack bonus from the tile as the base number of successes.
        Then for each point of fire power attack has roll a d6 and if it is a 5 or 6 it is a sucessful attack.
        Then roll armour the same way. damage then equals attack successes - defence sucesses.
        Apply damage or if it was out of range, print missed."""
        
        AttackStats = Attacker.GetComponentFromType(Component.Gamestats)
        DefenedStats = Defender.GetComponentFromType(Component.Gamestats)
        AttackPOS = Attacker.GetComponentFromType(Component.Position)
        DefendPOS = Defender.GetComponentFromType(Component.Position)
        Distance = AttackPOS.pos.distance_to(DefendPOS.pos)
        DefendTile = self.MapManager.GetTile(DefendPOS.pos).GetComponentFromType(Component.Tile).TYPE
        AttackTile = self.MapManager.GetTile(AttackPOS.pos).GetComponentFromType(Component.Tile).TYPE

        
        if(Distance <= AttackStats.MaxRange):
            
            AttackSuccesses = self.MapManager.TileTypes[self.MapManager.ReaderRecord[AttackTile]][2]
            for i in range(0,AttackStats.FirePower):
                x = random.randint(1,6)
                if(x >= 5):
                    AttackSuccesses +=1
                    
            DefenceSuccesses = self.MapManager.TileTypes[self.MapManager.ReaderRecord[DefendTile]][3]
            for i in range(0,DefenedStats.Armour):
                x = random.randint(1,6)
                if(x >= 5):
                    DefenceSuccesses +=1

            damage =AttackSuccesses - DefenceSuccesses
            if(damage > 0):
                Defender.GetComponentFromType(Component.Gamestats).HP -= damage
            #print(damage,AttackSuccesses,DefenceSuccesses,Defender.GetComponentFromType(Component.Gamestats).HP)
        else:
            #print("missed")
            pass
        self.TankManager.RemoveDeadTanks()

        
        
    def Move(self,POS,Mover):
        movestats = Mover.GetComponentFromType(Component.Gamestats).MoveSpeed
        #print(movestats)
        x = self.MapManager.AvalibleMovementTiles(Mover.GetComponentFromType(Component.Position).pos,movestats)

        if(POS in x):
            Mover.GetComponentFromType(Component.Position).pos = POS
        pass

    def InputActionCommand(self,ActionCommand):
        Commandkeys = ActionCommand.strip("\n")
        Commandkeys = Commandkeys.split(" ")
        if(self.replay == False):
            self.commands.append(ActionCommand)
        #So it should go TANKXX MOVE XX,XX
        #or along the lines of TANKXX FIRE TANKXX
        # where XX is a number of any length and then will be validated
        if(len(Commandkeys) < 3):
            Commandkeys.append("")
            Commandkeys.append("")
        ### ExampleCommand ###
        # TANK01 FIRE TANK00 #

        if(len(Commandkeys) > 0):
            
            if(Commandkeys[1] == "MOVE"):
                
                tankid = Commandkeys[0].strip("TANK")
                tankid = int(tankid)
                tanker = None
                try:
                    tanker = self.TankManager.Tanks[tankid]
                except Exception as e:
                    print(e)
                if(tanker == None):
                    print("invalid")
                else:
                    posstr = Commandkeys[2].split(",")
                    posx = int(posstr[0])
                    posy = int(posstr[1])
                    pos = pygame.math.Vector2(posx,posy)
                    #print(pos)
                    #print(tanker)
                    #print(self.CurrentPlayerTankActions)
                    if(self.TankManager.Tanks[tankid] in self.CurrentPlayerTankActions):
                        self.CurrentPlayerTankActions.remove(tanker)
                        self.Move(pos,self.TankManager.Tanks[tankid])
                        #print(self.TankManager.Tanks[tankid],pos,"Moved")
                    
            elif(Commandkeys[1] == "FIRE"):
                attackid = int(Commandkeys[0].strip("TANK"))
                defendid = int(Commandkeys[2].strip("TANK"))
                #print("FIRING")
                #print(attackid,"attack")
                #print(defendid,"defend")
                attack = None
                defend = None
                try:
                    attack = self.TankManager.Tanks[attackid]
                except Exception as e:
                    print(e)
                try:
                    defend = self.TankManager.Tanks[defendid]
                except Exception as e:
                    print(e)
                    
                if(attack ==None or defend == None):
                    print("invalid")
                else:
                    if(attack in self.CurrentPlayerTankActions):
                        self.CurrentPlayerTankActions.remove(attack)
                        self.Attack(attack,defend)

                pass
            elif(Commandkeys[0] == "ENDTURN"):
                self.EndTurn()
            else:
                print("Invalid Command Error ignoring input and returning to normal function.")
        else:
            print("Invalid Command doesn't exist despite entry. Front end pass through issue")


    def save(self):
        basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        fullpath = os.path.join(basepath,"Saves\\CORE\\USER\\autosave.xml")
        saver = ET.Element("save")

        ET.SubElement(saver,"Senario").text = self.Senario
        ET.SubElement(saver,"Count").text = self.Simdata

        Commands = ET.SubElement(saver,"Commands")
        if(len(self.commands)>0):
            for item in self.commands:
                ET.SubElement(Commands,"Command").text = item

        ET.SubElement(saver, "random").text = str(self.MainRanVal)

        root = ET.ElementTree(saver)
        root.write(fullpath)
        pass
