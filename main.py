import pygame
import Code.Component as Component
import Code.Entity as Entity
import Code.Managers as Managers
import Code.Simulation as Simulation
import os
import xml.etree.ElementTree
import random
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
print(ri,rf,rf[0])
zz = Component.Component()
xx = Component.Position(2,2)

print(type(xx),type(zz))

basepath = os.path.dirname(os.path.realpath(__file__))
print(basepath)
fullpath = os.path.join(basepath,"Saves\CORE\Battles\Test1.xml")
print(fullpath)

s = Simulation.Simulation("Test1.xml",random.randint(1,10000))
for f in range(0,10):
    s.EndTurn()
    s.Attack(s.TankManager.Tanks[1],s.TankManager.Tanks[0])




