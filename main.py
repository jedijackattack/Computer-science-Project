import pygame
import Code.Component as Component
import Code.Entity as Entity
import Code.Managers as Managers

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

t = Managers.TankStatManager()

t.AddTank("T34/75", 3, (3,5))
g = t.Tanks[0]
f = g.GetComponentFromType(Component.PlayerRef)
print(f.player)
print(t.Tanks[0])
print(g.components)

