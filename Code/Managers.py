import pygame
import math
import random
import Code.Entity as Entity
import Code.Component as Component


class TankStatManager(object):

    def __init__(self):
        self.Tanks = []
        
        self.TankTypes = {}
        
        # Name: HP, Armour, FirePower, Range, MoveSpeed, ConsumptionRate , img
        self.DisplayStats = {}
        
        pass

    def CreateTankTypes(self,Name,HP,Armour,FirePower,Range,MoveSpeed,ConsumptionRate,img):
        try:
            self.TankTypes[Name] = (int(HP),int(Armour),int(FirePower),int(Range),int(MoveSpeed),int(ConsumptionRate),str(img))
        except Exception as e:
            raise(e)
            exit()
        pass

    def AddTank(self, Type, PlayerID:int = 0, Pos = (0,0)):
        p = Component.Position(Pos[0],Pos[1])
        #print(self.TankTypes[Type][6])
        r = Component.RendererClient(self.TankTypes[Type][6],pygame.math.Vector2(1,1))
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
            #print(attributes)
            self.CreateTankTypes(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4],attributes[5],attributes[6],attributes[7])

        pass

    def GetTankPos(self,POS):
        exists = False
        for tank in self.Tanks:
            lpos = tank.GetComponentFromType(Component.Position).pos
            if(POS == lpos):
                exists = True
                return tank
        if(exists == False):
            return None

    def GenTanks(self,Battle):
        Tankset = Battle[3]

        for tank in Tankset:
            att = []
            for data in tank:
                att.append(data.text)
                pass
            if(att[3] in self.TankTypes):
                try:
                    self.AddTank(att[3],int(att[2]),(int(att[0]),int(att[1])))
                except Exception as e:
                    print("Invalid tank Creation {0},{1},{2},{3}".format(att[3],att[2],att[0],att[1]))


    def RemoveDeadTanks(self):
        for i in self.Tanks:
            t= i.GetComponentFromType(Component.Gamestats)
            if(t.HP <= 0 ):
                self.Tanks.remove(i)



###################################################################################

#THIS IS A DIFFERENT CLASS
##################################################################################


class TileWorldManager(object):
    MAPSIZE = 20

    def __init__(self,MAPSIZE = 20):
        self.Tiles = []
        self.TileTypes = {}
        self.ReaderRecord = {}
        self.MAPSIZE = MAPSIZE
        
        # Name: Walkable / MoveCost / AttackBonus / DefenceBonus / img
        pass

    def CreateTileTypes(self, Name:str, Walkable:str = False, MoveCost:int = 1, AttackBonus:int = 0, DefenceBonus:int = 0,Path:str = "NULL",idd:str = "!"):


        wa = None
        if(Walkable == "False"):
            wa = False
        elif(Walkable == "True"):
            wa = True
        else:
            print("ERROR Invalid File")
            exit()
        ## Ok so because python makes no sense the command bool() will return true if any none empty string is entered.
        ## so it required this rather than letting python handle the conversion.
            
        self.TileTypes[Name] = (wa, int(MoveCost), int(AttackBonus), int(DefenceBonus),str(Path))
        #print(Name,wa, int(MoveCost), int(AttackBonus), int(DefenceBonus),str(Path))
        self.ReaderRecord[idd] = (Name)
        pass

    def AddTile(self, Tipe:str, x:int = 0, y:int = 0):

        p = Component.Position(x,y)
        t = Component.Tile(Tipe)
        r = Component.RendererClient(self.TileTypes[self.ReaderRecord[Tipe]][4],pygame.math.Vector2(1,1))
        E = Entity.Entity(p,t,r)
        self.Tiles.append(E)
        pass


    def CreateTileManagerTypes(self, Battle):
        TileList=Battle[1]
        
        for TileTYPE in TileList:
            attributes = []
            for data in TileTYPE:
                attributes.append(data.text)

            self.CreateTileTypes(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4],attributes[5],TileTYPE.attrib["id"])

        pass

    def GetTile(self,POS):
        fx = POS[0]
        fy = POS[1]
        if(POS[0]< 0 or POS[0] > self.MAPSIZE-1 or POS[1]< 0 or POS[1] > self.MAPSIZE-1):
            return None
        try:
            out = self.Tiles[int(fy*self.MAPSIZE+fx)]
            return out
        except Exception as e:
            raise(e)
        pass

    def GetNeighbours(self,POS):
        tout =[]
        s = pygame.math.Vector2(0,1)
        n = pygame.math.Vector2(0,-1)
        e = pygame.math.Vector2(1,0)
        w = pygame.math.Vector2(-1,0)
        tout.append(self.GetTile((POS+s)))
        tout.append(self.GetTile((POS+n)))
        tout.append(self.GetTile((POS+e)))
        tout.append(self.GetTile((POS+w)))
        out = []
        for i in tout:
            if(i != None):
                out.append(i)
        return out
        

    def ReadMAP(self,Battle):
        MAP = Battle[0].text
        MAP = MAP.split("\n")
        
        for i in range(0,len(MAP)-1):
            MAP[i]=MAP[i].strip("\n")
            MAP[i]=MAP[i].strip(" ")
            MAP[i]=MAP[i].strip(" ")
            MAP[i]=MAP[i].strip("\t")
            
            if(len(MAP[i]) != self.MAPSIZE):
                MAP.pop(i)
            
        CorrectSize = True
        if(len(MAP) != self.MAPSIZE):
            CorrectSize = False
        for i in MAP:
            if(len(i) != self.MAPSIZE):
                CorrectSize = False

        if(CorrectSize == False):
            print("This file is not correctly formatted and may be corrupt.")
            exit()
        self.CreateMAPTiles(MAP,self.MAPSIZE,self.MAPSIZE)

    def CreateMAPTiles(self,MAP,Xsize,Ysize):
        for y in range(0,Ysize):
            for x in range(0,Xsize):
                self.AddTile(MAP[y][x],x,y)
                pass

    def AvalibleMovementTiles(self,POS,Movement):                                    
        WorkingList = []
        CompleteList = []
        WorkingList.append((POS,Movement))
        
        while (len(WorkingList) > 0):
            additions = []
    
            for x in WorkingList:
                neighbours = self.GetNeighbours(x[0])
                
                for i in neighbours:
                    thistype = i.GetComponentFromType(Component.Tile).TYPE
                    thisPOS = i.GetComponentFromType(Component.Position).pos
                    thiscost = self.TileTypes[self.ReaderRecord[thistype]][1]
                    thiswalkable = self.TileTypes[self.ReaderRecord[thistype]][0]
                    
                    if(thiswalkable == True and (x[1]-thiscost >= 0)):
                        additions.append((thisPOS,x[1]-thiscost))
                        
            for i in WorkingList:
                CompleteList.append(i)
                
            WorkingList = []
            if(len(additions) != 0):
                for i in additions:
                    WorkingList.append(i)
                    
        OutputList = []
        DefiniteMove = self.GetNeighbours(POS)
        for i in DefiniteMove:
            thistype = i.GetComponentFromType(Component.Tile).TYPE
            thiswalkable = self.TileTypes[self.ReaderRecord[thistype]][0]
            if(thiswalkable == True):
                additions.append((thisPOS,x[1]-thiscost))

        
        for i in CompleteList:
            OutputList.append(i[0])
        
        return RemoveDuplicates(OutputList)  

        pass


def RemoveDuplicates(x):
    list(x)
    out = []
    for i in x:
        if(i not in out):
            out.append(i)
    return out
    

    
        

