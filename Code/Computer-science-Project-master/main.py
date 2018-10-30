import pygame
import Code.Component as Component
import Code.Entity as Entity

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

zz = Component.Component()
xx = Component.Position(2,2)

print(type(xx),type(zz))
