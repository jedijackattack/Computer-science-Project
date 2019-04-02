import pygame
import time
import math
import os
import sys
import Code.Simulation as Simulation
import Code.Component as Component
import Code.Entity as Entity
import Code.Managers as Managers
import Code.GameRenderer as GameRenderer
import Code.UserInterface as UI
import random

basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
GraphicsPath = os.path.join(basepath,"graphics")


def main(sim, screen,resolution,FPS:int = 60,Victory:bool = False,User:int = 1):

    # define a variable to control the main loop
    running = True
    # create a clock

    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 72)

    # for checking updates for the renderer
    Update = 0
    # the selected and state values
    LastSelected = ""
    Selected = ""
    State = "None"
    # creates the game renderer
    GameWindow = GameRenderer.GameRender(0, 0, 720, 720, 36)
    #TexturePath = os.path.join(GraphicsPath, "Panzer3Pixel.png")
    #RawImage = pygame.image.load(TexturePath).convert()
    #setting up UI
    Interface = UI.UI(pygame.math.Vector2(int(resolution[0]*(9/16)),0),pygame.math.Vector2(int(resolution[0]-resolution[1]),int(resolution[1])))
    Interface.items.append(UI.Button(pygame.math.Vector2(int(Interface.size[0]*0.05), int(Interface.size[1]*0.05)), (int(Interface.size[0]*0.4), int(Interface.size[1]*0.15)), "Button-1.png", "END TURN", "arial", UI.ENDB))
    Interface.items.append(UI.Button(pygame.math.Vector2(int(Interface.size[0]*0.05), int(Interface.size[1]*0.25)), (int(Interface.size[0]*0.4), int(Interface.size[1]*0.05)), "Button-1.png", "MOVE", "arial", UI.MOVEB))
    Interface.items.append(UI.Button(pygame.math.Vector2(int(Interface.size[0]*0.05), int(Interface.size[1]*0.35)), (int(Interface.size[0]*0.4), int(Interface.size[1]*0.05)), "Button-1.png", "FIRE", "arial", UI.FIREB))
    Interface.items.append(UI.Button(pygame.math.Vector2(int(Interface.size[0]*0.75), int(Interface.size[1]*0.9 )), (int(Interface.size[0]*0.2), int(Interface.size[1]*0.05)), "Button-1.png", "QUIT", "arial", UI.QUIT))
    #Interface.items.append(RawImage)



    ###Main Loop###
    while running:

        ###INPUT###
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        mousepos = pygame.mouse.get_pos()
        LeftMousePressed = pygame.mouse.get_pressed()[0]
        if (pygame.mouse.get_pressed()[1] == 1 ):
            State = "None"

        g = GameWindow.Update(mousepos, LeftMousePressed, sim.TankManager, sim.MapManager)
        if (g != None):
            # print(g)
            Selected = g

        ButtonsInputs = Interface.update(mousepos,LeftMousePressed)
        for i in ButtonsInputs:
            if(i != None):
                State = i



        ###States###
        HILI = None
        if (State == "None"):
            if (Selected != ""):
                LastSelected = Selected
                Selected = ""
        elif (State == "MOVE"):

            if (Selected != "" and LastSelected != "" and type(Selected) == tuple and type(LastSelected) != tuple):

                sim.InputActionCommand(str(LastSelected) + " MOVE " + str(Selected[0]) + "," + str(Selected[1]))
                State = "None"
            elif (type(LastSelected) != tuple and LastSelected != ""):
                L = LastSelected.strip("TANK")
                L = int(L)
                t = sim.TankManager.Tanks[L]
                p = t.GetComponentFromType(Component.Position).pos
                movement = t.GetComponentFromType(Component.Gamestats).MoveSpeed
                m = sim.MapManager.AvalibleMovementTiles(p, movement)
                HILI = GameWindow.HighLight(m, (255, 0, 0))
            elif (LastSelected == ""):
                State = "None"

        elif (State == "FIRE"):
            if (Selected != "" and LastSelected != "" and type(Selected) != tuple and type(LastSelected) != tuple):

                State = "None"
                sim.InputActionCommand(str(LastSelected) + " FIRE " + str(Selected))
            elif (LastSelected != "" and type(LastSelected) != tuple):
                L = LastSelected.strip("TANK")
                L = int(L)
                t = sim.TankManager.Tanks[L]
                p = t.GetComponentFromType(Component.Position).pos
                r = t.GetComponentFromType(Component.Gamestats).MaxRange
                canhit = []
                for i in sim.TankManager.Tanks:
                    if (i != t):
                        m = i.GetComponentFromType(Component.Position).pos
                        distance = p.distance_to(m)
                        if (distance <= r):
                            canhit.append(m)
                HILI = GameWindow.HighLight(canhit, (255, 0, 0))


        elif (State == "END"):
            # print("END")
            sim.InputActionCommand("ENDTURN")
            State = "None"


        elif (State == "QUIT"):
            running = False
        ###End of States###


        if (Update == FPS):
            # sim.Attack(sim.TankManager.Tanks[0],sim.TankManager.Tanks[1])
            # sim.InputActionCommand("TANK01 MOVE 2,4")
            # sim.InputActionCommand("TANK00 MOVE 3,1")
            #print(str(LastSelected) + " "+str(Selected)+" " +str(State))
            # sim.EndTurn()
            GameWindow.MapRendered = False
            Update = 0
        else:
            Update += 1

        ############RENDER SCREEN#############
        screen.blit(GameWindow.RenderMap(sim.MapManager), (GameWindow.pos))

        screen.blit(GameWindow.RenderTanks(sim.TankManager), (GameWindow.pos))

        if(HILI != None):
            screen.blit(HILI,GameWindow.pos)

        Interface.draw(screen)

        DisplayFPS = font.render(str(round(clock.get_fps())), True, (0, 0, 0))
        screen.blit(DisplayFPS, (0, 0))
        ############Display Rendered Screen####
        pygame.display.flip()

        ###Check For victory###
        if (sim.Victory != None):
            if (sim.Victory[0] == User):
                return "VICTORY"
            else:
                return "DEFEAT"
            running = False

        clock.tick(FPS + 1)
