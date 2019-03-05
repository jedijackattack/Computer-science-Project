Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x= []
>>> len(x)
0
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 4, in <module>
    import Code.Managers as Managers
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 128
    def GetNeighbours(self,POS)
                              ^
SyntaxError: invalid syntax
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x04B01CF0>
[10, <Code.Entity.Entity object at 0x04B01CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x0567C5B0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x0567C550>]
[False]
None
0 2 2 5
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovement(POS,Mover)
AttributeError: 'TileWorldManager' object has no attribute 'AvalibleMovement'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x05C79910>
[10, <Code.Entity.Entity object at 0x05C79910>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x064E6CB0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x064DB5B0>]
[False]
None
2 2 0 3
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 181, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 130, in GetNeighbours
    out.append(self.GetTile(POS[0],POS[1]-1))
UnboundLocalError: local variable 'out' referenced before assignment
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x02D11CF0>
[10, <Code.Entity.Entity object at 0x02D11CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x057E7D10>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x057DB7D0>]
[False]
None
2 3 1 3
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 181, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 130, in GetNeighbours
    tout.append(self.GetTile(POS[0],POS[1]-1))
TypeError: 'int' object is not subscriptable
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x053E9910>
[10, <Code.Entity.Entity object at 0x053E9910>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05A27CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x05A1B7D0>]
[False]
None
0 1 1 5
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 181, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 130, in GetNeighbours
    tout.append(self.GetTile((POS[0],POS[1]-1)))
TypeError: 'int' object is not subscriptable
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py 
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 4, in <module>
    import Code.Entity as Entity
ModuleNotFoundError: No module named 'Code'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x02D01CF0>
[10, <Code.Entity.Entity object at 0x02D01CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x054A6CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x0549C7B0>]
[False]
None
2 3 1 3
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 182, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 130, in GetNeighbours
    print(POS[0],POS[1]+1)
TypeError: 'int' object is not subscriptable
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x02EA1CF0>
[10, <Code.Entity.Entity object at 0x02EA1CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05D57D10>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x05D4B7D0>]
[False]
None
1 1 0 4
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 182, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 130, in GetNeighbours
    print(POS[0],POS[1])
TypeError: 'int' object is not subscriptable
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py 
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 4, in <module>
    import Code.Entity as Entity
ModuleNotFoundError: No module named 'Code'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x04DD98F0>
[10, <Code.Entity.Entity object at 0x04DD98F0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05417CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x0540B7B0>]
[False]
None
0 1 1 5
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 182, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 130, in GetNeighbours
    print(POS[0])
TypeError: 'int' object is not subscriptable
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x04A41CF0>
[10, <Code.Entity.Entity object at 0x04A41CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x055D7CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x055CC7D0>]
[False]
None
3 3 0 2
4
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 182, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 131, in GetNeighbours
    tout.append(self.GetTile((POS[0],POS[1]-1)))
TypeError: 'int' object is not subscriptable
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py 
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 4, in <module>
    import Code.Entity as Entity
ModuleNotFoundError: No module named 'Code'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x02CC1CF0>
[10, <Code.Entity.Entity object at 0x02CC1CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05957D10>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x0594D7D0>]
[False]
None
0 2 2 5
[(4, <Vector2(3, 3)>)]
4
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 183, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 131, in GetNeighbours
    tout.append(self.GetTile((POS[0],POS[1]-1)))
TypeError: 'int' object is not subscriptable
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py 
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 4, in <module>
    import Code.Entity as Entity
ModuleNotFoundError: No module named 'Code'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x05801CF0>
[10, <Code.Entity.Entity object at 0x05801CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x06397CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x0638C7B0>]
[False]
None
4 4 0 1
[(<Vector2(3, 3)>, 4)]
[3, 3]
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 186, in AvalibleMovementTiles
    thistype = i.GetComponentFromType(Component.Type)
AttributeError: module 'Code.Component' has no attribute 'Type'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py 
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 4, in <module>
    import Code.Entity as Entity
ModuleNotFoundError: No module named 'Code'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x059C98B0>
[10, <Code.Entity.Entity object at 0x059C98B0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05FFD5B0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x05FFD550>]
[False]
None
4 4 0 1
[(<Vector2(3, 3)>, 4)]
[3, 3]
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 186, in AvalibleMovementTiles
    thistype = i.GetComponentFromType(Component.Tile).Type
AttributeError: 'Tile' object has no attribute 'Type'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x03581CF0>
[10, <Code.Entity.Entity object at 0x03581CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05D37CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x05D2D7B0>]
[False]
None
1 1 0 4
[(<Vector2(3, 3)>, 4)]
[3, 3]
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 192, in AvalibleMovementTiles
    additions.append(thisPOS,x[1]-thiscost)
TypeError: append() takes exactly one argument (2 given)
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
 
>>> 
<Code.Entity.Entity object at 0x057E98F0>
[10, <Code.Entity.Entity object at 0x057E98F0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 41, in <module>
    basepath = os.path.dirname(os.path.realpath(__file__))
NameError: name '__file__' is not defined
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x05599910>
[10, <Code.Entity.Entity object at 0x05599910>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05BCD610>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x05BCD650>]
[False]
None
1 1 0 4
[(<Vector2(3, 3)>, 4)]
[3, 3]
<Code.Component.Position object at 0x05CCF6B0>
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 183, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 131, in GetNeighbours
    tout.append(self.GetTile((POS[0],POS[1]-1)))
TypeError: 'Position' object does not support indexing
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py 
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 4, in <module>
    import Code.Entity as Entity
ModuleNotFoundError: No module named 'Code'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x05E098F0>
[10, <Code.Entity.Entity object at 0x05E098F0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x0643C5D0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x0643C570>]
[False]
None
3 3 0 2
[(<Vector2(3, 3)>, 4)]
3.0
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 183, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 130, in GetNeighbours
    print(POS[0])
TypeError: 'Position' object does not support indexing
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 4, in <module>
    import Code.Managers as Managers
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 136
    tout.append(self.GetTile((POS+n))
       ^
SyntaxError: invalid syntax
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x05071CF0>
[10, <Code.Entity.Entity object at 0x05071CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05C07CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x05BFC7B0>]
[False]
None
4 4 0 1
[(<Vector2(3, 3)>, 4)]
[3, 3]
<Code.Component.Position object at 0x05CF5AB0>
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 187, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 135, in GetNeighbours
    tout.append(self.GetTile((POS+s)))
TypeError: unsupported operand type(s) for +: 'Position' and 'pygame.math.Vector2'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x05119910>
[10, <Code.Entity.Entity object at 0x05119910>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05756D10>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x0574D7D0>]
[False]
None
1 2 1 4
[(<Vector2(3, 3)>, 4)]
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 187, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 134, in GetNeighbours
    POS = pygame.math.Vector2(POS)
ValueError: Vector2 must be initialized with 2 real numbers or a sequence of 2 real numbers
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x035E1CF0>
[10, <Code.Entity.Entity object at 0x035E1CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x06266D10>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x0625D7F0>]
[False]
None
2 2 0 3
[(<Vector2(3, 3)>, 4)]
[3, 3]
<Code.Component.Position object at 0x06346AB0>
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 188, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 135, in GetNeighbours
    POS = pygame.math.Vector2(POS)
ValueError: Vector2 must be initialized with 2 real numbers or a sequence of 2 real numbers
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x055C1CF0>
[10, <Code.Entity.Entity object at 0x055C1CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x06176CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x0616D7B0>]
[False]
None
1 2 1 4
[(<Vector2(3, 3)>, 4)]
3.0
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 188, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 134, in GetNeighbours
    print(POS[0])
TypeError: 'Position' object does not support indexing
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x059A98B0>
[10, <Code.Entity.Entity object at 0x059A98B0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x06217CD0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x0620C790>]
[False]
None
0 2 2 5
[(<Vector2(3, 3)>, 4)]
3.0
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 189, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 135, in GetNeighbours
    print(t[0])
TypeError: 'Position' object does not support indexing
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x02C71CF0>
[10, <Code.Entity.Entity object at 0x02C71CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x058F6CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x058ED7B0>]
[False]
None
1 2 1 4
[(<Vector2(3, 3)>, 4)]
<class 'pygame.math.Vector2'>
<class 'Code.Component.Position'>
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 188, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 135, in GetNeighbours
    POS = pygame.math.Vector2(POS)
ValueError: Vector2 must be initialized with 2 real numbers or a sequence of 2 real numbers
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x05909910>
[10, <Code.Entity.Entity object at 0x05909910>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05F48CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x05F3D7B0>]
[False]
None
1 1 0 4
[(<Vector2(3, 3)>, 4)]
[3, 3]
<class 'pygame.math.Vector2'>
<Code.Component.Position object at 0x06026AB0>
<class 'Code.Component.Position'>
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 188, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 135, in GetNeighbours
    tout.append(self.GetTile((POS+s)))
TypeError: unsupported operand type(s) for +: 'Position' and 'pygame.math.Vector2'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x050F1CF0>
[10, <Code.Entity.Entity object at 0x050F1CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05C76CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x05C6C7B0>]
[False]
None
1 3 2 4
[3, 3] x
<class 'pygame.math.Vector2'>
<Code.Component.Position object at 0x05D54AB0> x
<class 'Code.Component.Position'>
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 186, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 135, in GetNeighbours
    tout.append(self.GetTile((POS+s)))
TypeError: unsupported operand type(s) for +: 'Position' and 'pygame.math.Vector2'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x04FA1CF0>
[10, <Code.Entity.Entity object at 0x04FA1CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05B76CF0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x05B6C7B0>]
[False]
None
2 3 1 3
[3, 3] WHYYY
[3, 3] x
<class 'pygame.math.Vector2'>
<Code.Component.Position object at 0x05C55A90> x
<class 'Code.Component.Position'>
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 188, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 135, in GetNeighbours
    tout.append(self.GetTile((POS+s)))
TypeError: unsupported operand type(s) for +: 'Position' and 'pygame.math.Vector2'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x05421CF0>
[10, <Code.Entity.Entity object at 0x05421CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x05FC6CB0>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x05FBC5B0>]
[False]
None
3 4 1 2
[3, 3] <class 'pygame.math.Vector2'> WHYYY
[3, 3] x
<class 'pygame.math.Vector2'>
<Code.Component.Position object at 0x060A5AF0> x
<class 'Code.Component.Position'>
Traceback (most recent call last):
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py", line 50, in <module>
    s.Move(pygame.math.Vector2(3,3),4)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Simulation.py", line 162, in Move
    self.MapManager.AvalibleMovementTiles(POS,Mover)
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 188, in AvalibleMovementTiles
    neighbours = self.GetNeighbours(x[0])
  File "N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Code\Managers.py", line 135, in GetNeighbours
    tout.append(self.GetTile((POS+s)))
TypeError: unsupported operand type(s) for +: 'Position' and 'pygame.math.Vector2'
>>> 
 RESTART: N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\main.py 
<Code.Entity.Entity object at 0x02C61CF0>
[10, <Code.Entity.Entity object at 0x02C61CF0>, 5]
1
2
5.0
[8, 9] [4, 6] 4.0
<class 'Code.Component.Position'> <class 'Code.Component.Component'>
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master
N:\Downloads\Computer-science-Project-master\Computer-science-Project-master\Saves\CORE\Battles\Test1.xml
DEBUG: 1 TURN INPUT ex1
win condition met False
[<Code.Entity.Entity object at 0x058F6D10>]
[False]
None
DEBUG: 2 TURN INPUT ex2
win condition met False
[<Code.Entity.Entity object at 0x058ED7D0>]
[False]
None
3 3 0 2
[3, 3] <class 'pygame.math.Vector2'> WHYYY
[3, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 4] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 2] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[4, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[2, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 5] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[4, 4] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[2, 4] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 1] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[4, 2] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[2, 2] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[4, 4] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[4, 2] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[5, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[2, 4] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[2, 2] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[1, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[(<Vector2(3, 3)>, 4), (<Vector2(3, 4)>, 2), (<Vector2(3, 2)>, 2), (<Vector2(4, 3)>, 2), (<Vector2(2, 3)>, 2), (<Vector2(3, 5)>, 0), (<Vector2(3, 3)>, 0), (<Vector2(4, 4)>, 0), (<Vector2(2, 4)>, 0), (<Vector2(3, 3)>, 0), (<Vector2(3, 1)>, 0), (<Vector2(4, 2)>, 0), (<Vector2(2, 2)>, 0), (<Vector2(4, 4)>, 0), (<Vector2(4, 2)>, 0), (<Vector2(5, 3)>, 0), (<Vector2(3, 3)>, 0), (<Vector2(2, 4)>, 0), (<Vector2(2, 2)>, 0), (<Vector2(3, 3)>, 0), (<Vector2(1, 3)>, 0)]
DEBUG: 1 TURN INPUT ex3
win condition met False
[<Code.Entity.Entity object at 0x058F6D10>]
[False]
None
1 3 2 1
[3, 3] <class 'pygame.math.Vector2'> WHYYY
[3, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 4] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 2] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[4, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[2, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 5] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[4, 4] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[2, 4] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 1] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[4, 2] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[2, 2] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[4, 4] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[4, 2] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[5, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[2, 4] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[2, 2] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[3, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[1, 3] <class 'pygame.math.Vector2'> x
<class 'pygame.math.Vector2'>
[(<Vector2(3, 3)>, 4), (<Vector2(3, 4)>, 2), (<Vector2(3, 2)>, 2), (<Vector2(4, 3)>, 2), (<Vector2(2, 3)>, 2), (<Vector2(3, 5)>, 0), (<Vector2(3, 3)>, 0), (<Vector2(4, 4)>, 0), (<Vector2(2, 4)>, 0), (<Vector2(3, 3)>, 0), (<Vector2(3, 1)>, 0), (<Vector2(4, 2)>, 0), (<Vector2(2, 2)>, 0), (<Vector2(4, 4)>, 0), (<Vector2(4, 2)>, 0), (<Vector2(5, 3)>, 0), (<Vector2(3, 3)>, 0), (<Vector2(2, 4)>, 0), (<Vector2(2, 2)>, 0), (<Vector2(3, 3)>, 0), (<Vector2(1, 3)>, 0)]
>>> 
