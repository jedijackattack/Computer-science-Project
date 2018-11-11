class Entity(object):

    """This is the bases for all other classes in the project.
    They all use this as a base and add components to it using the components list."""


    ID = 0
    LIST = []

    def __init__(self, *Components):
        self.id = Entity.CreateID()
        self.components = []
        for i in Components :
            self.AddComponent(i)
        pass
        Entity.LIST.append(self)

    def AddComponent(self, Component):
        """Allows you to add a components to Entities"""
        self.components.append(Component)
        pass

    def GetComponentFromType(self, Component):
        """Allows you to get a Component back to use later. Same component can't be used twice"""
        for item in self.components:
            if (type(item) == Component): #Checks if the same type of component is present
                return self.components[self.components.index(item)]
        else:
            return None


    @staticmethod
    def CreateID():
        x = Entity.ID
        Entity.ID +=1
        return x
        pass

