import pygame

class Component():
    ID = 0
    LIST = []
    def __init__(self):
        self.ID = Component.CreateID()
        Component.LIST.append(self)
        self.parent = None
        pass

    @staticmethod
    def CreateID():
        x = Component.ID
        Component.ID += 1
        return x
        pass


class Position(Component):

    LIST = []
    def __init__(self, x:int = 0, y:int =0):
        """
        :param x:
        :param y:
        """
        Component.__init__(self)
        self.pos = pygame.math.Vector2(x,y)
        Position.LIST.append(self)


class Tile(Component):
    LIST = []
    def __init__(self, Type=None):
        """

        :param Type:
        """
        Component.__init__(self)
        self.TYPE = Type
        Tile.LIST.append(self)


class RendererClient(Component):

    LIST = []
    def __init__(self, img = None, size = pygame.math.Vector2(0,0)):
        """

        :param img:
        :param size:
        """
        Component.__init__(self)
        self.Img = img      # path to the image
        RendererClient.LIST.append(self)



class Tank(Component):
    LIST = []
    def __init__(self,Type,stats):
        """

        :param Type:
        :param stats:
        """
        Component.__init__(self)
        self.Type = Type
        Tank.LIST.append(self)
        self.stats = stats

class Gamestats(Component):
    LIST = []
    def __init__(self, Mstats:tuple):
        """

        :param Mstats:
        """
        Component.__init__(self)
        self.HP = Mstats[0]
        self.Armour = Mstats[1]
        self.FirePower = Mstats[2]
        self.MoveSpeed = Mstats[4]
        self.MaxRange = Mstats[3]
        self.ConsumptionRate = Mstats[5]
        Gamestats.LIST.append(self)
        pass


class PlayerRef(Component):

    def __init__(self, p:int = 0):
        """

        :param p:
        """
        Component.__init__(self)
        self.player = p
        pass

    
