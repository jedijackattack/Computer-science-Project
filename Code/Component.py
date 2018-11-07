import pygame

class Component(object):
    ID = 0
    LIST = []
    def __init__(self,):
        self.ID = Component.CreateID()
        Component.LIST.append(self)
        self.parent = 
        pass

    @staticmethod
    def CreateID():
        x = Component.ID
        Component.ID += 1
        return x
        pass


class Position(Component):

    LIST = []
    def __init__(self,x=0,y=0):
        Component.__init__(self)
        self.pos = pygame.math.Vector2(x,y)
        Position.LIST.append(self)

class Tile(Component):
    TileType = {}
    LIST = []
    def __init__(self, Type=None):
        Component.__init__(self)
        self.TYPE = Type
        Tile.LIST.append(self)


def RendererClient(Component):
    LIST = []
    def __init__(self, Renderer = None, img = None, Size = pygame.math.Vector2(0,0)):
        Component.__init__(self)
        self.Renderer = Renderer # render surface to be drawn on
        RenderClient.LIST.append(self)
        self.Img = img # path to the image
        self.Size = Size # in pixels for a 1080p display


def TankType(Component):
    LIST = []
    def __init__(self,Type):
        Component.__init__(self)
        self.Type = Type
        self.TankType.LIST.append(self)

def Gamestats(Component):
    LIST = []
    def __init__(self)
        Component.__init__(self)
        self.hp = 0
        self.armour = 0
        self.AttackPower = 0
        self.MoveSpeed = ArithmeticError
        self.MaxRange = 0
        pass


    

        


    
