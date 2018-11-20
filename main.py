import pygame
import Code.Component as Component
import Code.Entity as Entity
import Code.Managers as Managers
import Code.Simulation as Simulation
import os
import xml.etree.ElementTree
pygame.init()

g = Entity.Entity()
x = Entity.Entity()

y= 5
z = 10
x.AddComponent(z)
x.AddComponent(g)

o = x
o.AddComponent(y)



print(x.GetComponentFromType(Entity.Entity))
print(x.components)
print(x.id)

a = Entity.Entity()
print(a.id)

ri = pygame.math.Vector2(8,9)
rf = pygame.math.Vector2(4,6)
gg = (ri-rf)
print(gg.length())
print(ri,rf)
zz = Component.Component()
xx = Component.Position(2,2)

print(type(xx),type(zz))

basepath = os.path.dirname(os.path.realpath(__file__))
print(basepath)
fullpath = os.path.join(basepath,"Saves\CORE\Battles\Test1.xml")
print(fullpath)
"""
tree = xml.etree.ElementTree.parse(fullpath)
battle = tree.getroot()

for child in battle:
    print(child.tag,":",child.text)
    for element in child:
        print(element.tag,":",element.text)
        if(len(element) >= 2):
            for data in element:
                print(data.tag,":",data.text)


print(battle[0].text)
"""
s = Simulation.Simulation("Test1.xml")
s.CreateTankManagerTypes()
print(s.TankManager.TankTypes)
