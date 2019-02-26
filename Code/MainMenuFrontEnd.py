import pygame
import os
import Code.UserInterface as UI

def returnNewGame():
    return "NEW GAME"

def returnLoadGame():
    return "LOAD GAME"

def StartScreen(screen,resolution,FPS = 60):

    running = True
    buttonsize = (int(resolution[0]/3),int(resolution[1]/10))
    buttonpos = (int(resolution[0]/2-buttonsize[0]/2),int(resolution[1]/2-buttonsize[1]/2))
    Interface = UI.UI(pygame.math.Vector2(0,0),resolution)

    Interface.items.append(UI.Button(buttonpos,buttonsize,"Button-1.png","NEW GAME","arial",returnNewGame ))
    Interface.items.append(UI.Button((buttonpos[0],int(buttonpos[1]+buttonsize[1]*1.25)), buttonsize, "Button-1.png", "CONTINUE GAME", "arial",returnLoadGame))
    Interface.items.append(UI.Button((buttonpos[0], int(resolution[1] - buttonsize[1] * 1.25)), buttonsize, "Button-1.png", "QUIT","arial",UI.QUIT))

    clock = pygame.time.Clock()



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

        buttoninput = Interface.update(mousepos,LeftMousePressed)
        for i in buttoninput:
            if(i != None):
                running = False
                return i

        Interface.draw(screen)

        pygame.display.flip()
        clock.tick(FPS + 1)



def NewGameScreen(screen,resolution,senarios,FPS = 60):
    
    running = True
    buttonsize = (int(resolution[0]/5),int(resolution[1]/18))
    startbuttonpos = (int(buttonsize[0]),int(buttonsize[1]))
    SenarioList = UI.UI(pygame.math.Vector2(0,0),resolution)
    SenarioButtons = UI.UI(pygame.math.Vector2(0,0),resolution)

    x= 0
    
    maxcharlength = 24
    for i in senarios:
        newpos = (startbuttonpos[0],int(startbuttonpos[1]+x*buttonsize[1]*1.1))
        text = i
        if(len(i) > maxcharlength):
            text = i[0:maxcharlength]+str("...")
        y = UI.Button(newpos,buttonsize,"Button-1.png",text,"arial",lambda:print(text))
        SenarioList.items.append(y)
        x+=1
    
    clock = pygame.time.Clock()
    

    z = 1
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
        
        buttoninput = SenarioList.update(mousepos,LeftMousePressed)
        for i in buttoninput:
            if(i != None):
                running = False

        SenarioList.move(0,1)
        
        SenarioList.draw(screen)

        pygame.display.flip()
        clock.tick(FPS + 1)

    pass