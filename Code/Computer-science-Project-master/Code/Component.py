import pygame

class Component(object):
    ID = 0
    LIST = []
    def __init__(self):
        self.ID = Component.CreateID()
        Component.LIST.append(self)
        pass

    def GetData(self):
        return None

    def SetData(self,*Data):
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

    def GetData(self):
        return self.pos

    def SetData(self, Npos):
        self.pos = Npos
        pass

class Tile(Component):
    TileType = {}
    LIST = []
    def __init__(self, Type=None):
        Component.__init__(self)
        self.TYPE = Type
        Tile.LIST.append(self)

    def GetData(self):
        return self.TYPE

    def SetData(self, NTYPE):
        self.TYPE = NTYPE
        pass

def RendererClient(Component):
    LIST = []
    def __init__(self,Renderer = None, img = None):
        Component.__init__(self)
        self.Renderer = Renderer
        self.img = img
        RenderClient.LIST.append(self)

    def GetData(self):
        return (self.Renderer,self.img)

    def SetData(self, NRenderer, Nimg):
        self.Renderer = NRenderer
        self.img = Nimg
        pass


    
