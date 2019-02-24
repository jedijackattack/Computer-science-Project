import Code.Component as Component
import Code.Entity as Entity
import Code.Managers as Managers
import pygame
import math

def botAction(tankmanager,mapmanager,bottanks):

    enemytanks = []
    out = []

    for i in tankmanager.Tanks:
        if (i not in bottanks):
            enemytanks.append(i)
            pass

    for tank in bottanks:

        fire = False

        for enemy in enemytanks:
            friendlypos = tank.GetComponentFromType(Component.Position).pos
            enemypos = enemy.GetComponentFromType(Component.Position).pos
            friendlyrange = tank.GetComponentFromType(Component.Gamestats).MaxRange

            if(friendlypos.distance_to(enemypos) <= friendlyrange):
                num = tankmanager.Tanks.index(tank)
                frendlyout = "TANK" + str(num)
                num = tankmanager.Tanks.index(enemy)
                enemyout = "TANK" + str(num)
                command = frendlyout + " FIRE " + enemyout
                out.append(command)
                fire = True
                break
        print(fire)
        if(fire == False):

            ClosestTarget = None
            ClosestDistance = math.inf

            for enemy in enemytanks:
                friendlypos = tank.GetComponentFromType(Component.Position).pos
                enemypos = enemy.GetComponentFromType(Component.Position).pos
                distance = friendlypos.distance_to(enemypos)

                if(distance < ClosestDistance):
                    ClosestDistance = distance
                    ClosestTarget = enemy


            print(ClosestTarget,tank)
            Targetpos = ClosestTarget.GetComponentFromType(Component.Position).pos
            TargetMoveRange = tank.GetComponentFromType(Component.Gamestats).MoveSpeed
            avalablemovement = mapmanager.AvalibleMovementTiles(tank.GetComponentFromType(Component.Position).pos,TargetMoveRange)

            ClosestDistance = math.inf
            ClosestTile = None
            for tile in avalablemovement:

                distance = Targetpos.distance_to(pygame.math.Vector2(tile))
                if(distance < ClosestDistance):
                    ClosestDistance = distance
                    ClosestTile = tile
            num = tankmanager.Tanks.index(tank)
            frendlyout = "TANK" + str(num)
            print(ClosestTile)
            text = frendlyout + " MOVE " + str(int(ClosestTile[0]))+","+str(int(ClosestTile[1]))
            out.append(text)

    out.append("ENDTURN")
    return out


    pass