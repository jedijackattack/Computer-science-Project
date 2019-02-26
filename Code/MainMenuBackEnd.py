import pygame
import xml.etree.ElementTree as ET
import os
import configparser
import random
import Code.GameInstance as GameInstance
import Code.MainMenuFrontEnd as MMFE
import Code.Simulation as Simulation

pygame.init()

def main():


    CurrentSenario = None
    CurrentCount = 1
    SenariosFiles = FindSenarios()
    print(SenariosFiles)

    Senarios = LoadSenarioData(SenariosFiles)
    print(Senarios)

    resolution,FPS,debug = Loadconfig()
    print(resolution,FPS)

    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Project Salient")


    NextScreen = MMFE.StartScreen(screen,resolution,FPS)
    screen.fill((0,0,0))
    print(NextScreen)

    if(NextScreen == "QUIT"):
        exit()
    elif(NextScreen == "NEW GAME"):
        print(Senarios)
        NextScreen = MMFE.NewGameScreen(screen,resolution,Senarios)

        if(NextScreen == "BACK"):
            main()
        else:
            senario = Senarios[NextScreen]
            sim = senario[2][0]
            newsim = Simulation.Simulation(sim,Senario=NextScreen)
            Game = GameInstance.main(newsim, screen, resolution, FPS=FPS)
            VictoryDefeat(NextScreen, sim, Game, screen, resolution,Senarios,FPS)
            pass
        
    elif(NextScreen == "LOAD GAME"):

        autosave = LoadAutoSave()
        battlefile = autosave[1]
        print(battlefile)
        newsim = Simulation.Simulation(battlefile, Randomval=autosave[3], save=autosave[2],Senario=autosave[0])
        Game = GameInstance.main(newsim,screen,resolution,FPS=FPS)

        VictoryDefeat(autosave[0],battlefile,Game,screen,resolution,Senarios,FPS)
    else:
        print("ERROR BETWEEN MENU GUI AND MENU HANDLER EXCEPTION {0},{1}".format(hash(NextScreen),NextScreen))



    pass

def GetBasePath():
    basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return basepath

def GetSavePath():
    fullpath = os.path.join(GetBasePath(), "Saves/CORE/Senarios")
    return fullpath

def FindSenarios():

    Senarios = []
    fullpath = GetSavePath()
    files = os.listdir(fullpath)

    for i in files:
        if(".xml" in i):
            Senarios.append(i)
    return Senarios

def LoadSenarioData(SenariosFiles:list):

    Senarios = {}

    for Senario in SenariosFiles:

        datapath = os.path.join(GetSavePath(),Senario)
        data = ET.parse(datapath)
        data = data.getroot()

        battles = []
        for i in data[2]:
            battles.append(str(i.text))

        name = str(data[0].text)
        count = int(data[1].text)
        desc = str(None)
        if(len(data) > 3):
            desc = str(data[3].text)
        print(name,count,desc,battles)
        Senarios[name] = (count,desc,battles)

    return Senarios

def Loadconfig():
    resolution = (0,0)
    basepath = GetBasePath()
    fullpath = os.path.join(basepath,"config.xml")
    data = ET.parse(fullpath)
    data = data.getroot()
    currentres = None

    if(len(data) >= 4 ):
        currentres=data[0].text
    else:
        print("An Error has occured in the config file. Please redownload the file from source or reinstall the application")
        exit()

    FPS = int(data[1].text)
    valid = False

    for i in data[2]:
        if(i.text == currentres):
            valid = True

    if(valid):
        res = currentres.split("x")
        resolution = (int(res[0]),int(res[1]))
        return resolution,FPS,data[3].text
    else:
        print("Error invalid resolution")
        exit()


def LoadAutoSave():
    basepath = GetBasePath()
    fullpath = os.path.join(basepath,"Saves/CORE/USER/autosave.xml")
    data = ET.parse(fullpath)
    data = data.getroot()
    if(len(data) == 4):
        senarioname = data[0].text
        progress = data[1].text
        commands = []
        random = int(data[3].text)
        for i in data[2]:
            commands.append(i.text)
        return (senarioname,progress,commands,random)
    else:
        print("Error Invalid Auto Save, corrupted,damaged")
        exit()
    pass

def VictoryDefeat(Senario,Currentbattle,VD,screen,resolution,Senarios,FPS = 60):

    if(VD == "VICTORY"):
        vic = MMFE.VictoryScreen(screen,resolution)
        if(vic == "CONTINUE"):
            print(Senario)
            finder = Senarios[Senario]
            battles = finder[2]
            index = battles.index(Currentbattle)
            if(len(battles)-1 > index):
                index+=1
                newbattle = battles[index]
                newsim = Simulation.Simulation(newbattle, Senario=Senario)
                Game = GameInstance.main(newsim, screen, resolution, FPS=FPS)
                VictoryDefeat(Senario, newbattle, Game, screen, resolution, Senarios,FPS)
        else:
            quit()
    elif(VD == "DEFEAT"):
        MMFE.DefeatScreen(screen,resolution)
    else:
        print("ERROR invalid Victory/Defeat command")
        exit()



    pass

























main()
#MMFE.VictoryScreen(pygame.display.set_mode((1280,720)),(1280,720))
