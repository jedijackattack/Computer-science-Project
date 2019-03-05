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
import random

class wigit(object):
    TEXTURES = {}
    basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    GraphicsPath = os.path.join(basepath, "graphics")

    def __init__(self,POS,Size,texture):
        self.POS = POS
        self.Size = Size
        self.texture = texture

    def draw(self, screen, Goffset=pygame.math.Vector2(0, 0)):
        wigit.CreateTexture(self.texture, self.Size)
        screen.blit(wigit.TEXTURES[self.texture + str(self.Size)], self.POS + Goffset)

    @staticmethod
    def CreateTexture(texture, Size):
        i = texture + str(Size)
        if (texture not in Button.TEXTURES):
            wigit.LoadTexture(texture, Size)

    @staticmethod
    def LoadTexture(texture, Size):
        name = texture + str(Size)
        TexturePath = os.path.join(wigit.GraphicsPath, texture)
        RawImage = pygame.image.load(TexturePath).convert_alpha()
        ConvertedImage = pygame.transform.scale(RawImage, Size)
        wigit.TEXTURES[name] = ConvertedImage


class Button(object):
    FONTS = {}
    TEXTURES ={}
    basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    GraphicsPath = os.path.join(basepath,"graphics")
    
    def __init__(self,POS,Size,texture,text,fontt,Function = lambda: print("BUTTON FIRED") ):
        self.POS = POS
        self.Size = Size
        self.texture = texture
        self.text = Button.textcreate(text,fontt,Size)
        self.fontt = fontt
        self.function = Function
        self.pressed = False
        pass

    def draw(self,screen,Goffset = pygame.math.Vector2(0,0)):
        Button.CreateTexture(self.texture,self.Size)
        screen.blit(Button.TEXTURES[self.texture+str(self.Size)],self.POS+Goffset)
        s = self.text.get_size()
        offset = [0,0]
        offset[0] = (self.Size[0]-s[0])/2
        offset[1] = (self.Size[1]-s[1])/2
        screen.blit(self.text ,(self.POS[0]+offset[0],self.POS[1]+offset[1])+Goffset)

    def Update(self,MousePos,lmousepress):
        if(MousePos[0] < self.POS[0]+self.Size[0] and MousePos[0] > self.POS[0]):
            if(MousePos[1] < self.POS[1]+self.Size[1] and MousePos[1] > self.POS[1]):
                if(lmousepress == 1):
                    if(self.pressed == False):
                    
                        self.texture = "ButtonVeryDark-1.png"
                        self.pressed = True
                        #print(callable(self.function))
                        if (callable(self.function)): # edit to allow for return to be value or funciton call
                            return self.function()
                        else:
                            return self.function

                    #print("Function Fired")
                else:
                    self.texture = "ButtonDark-1.png"
                    self.pressed = False
            else:
                self.texture = "Button-1.png"
        else:
                self.texture = "Button-1.png"
            


    @staticmethod
    def textcreate(text,font,Size):
        Button.CreateFont(font,Size,text)
        img = Button.FONTS[font+str(Size)]
        t = img.render(text ,True, (0, 0, 0))
        return t
    
    @staticmethod
    def CreateTexture(texture,Size):
        i = texture+str(Size)
        if(texture not in Button.TEXTURES):
            Button.LoadTexture(texture,Size)

    @staticmethod
    def LoadTexture(texture,Size):
        name = texture+str(Size)
        TexturePath = os.path.join(Button.GraphicsPath,texture)
        RawImage = pygame.image.load(TexturePath).convert_alpha()
        ConvertedImage = pygame.transform.scale(RawImage,Size)
        Button.TEXTURES[name] = ConvertedImage
                    
    @staticmethod
    def CreateFont(fontt,Size,text):
        if(fontt+str(Size) not in Button.FONTS):
            Button.Loadfont(fontt,Size,text)

    @staticmethod
    def Loadfont(fontt,Size,text):
        i = 0
        x = 100
        while True:
            i = pygame.font.SysFont(fontt, x)
            if(i.size(text)[0] < Size[0] and i.size(text)[1] < Size[1]):
                break
            x -=5
        Button.FONTS[fontt+str(Size)] = pygame.font.SysFont(fontt, x-5)

def MOVEB():
    #print("Move!")
    return "MOVE"

def FIREB():
    return "FIRE"

def QUIT():
    return "QUIT"

def ENDB():
    return "END"

def HIGHB():
    return "HIGHLIGHT"
    
class UI(object):

    def __init__(self,pos,size,bg = (114, 57, 8)):
        self.pos = pos
        self.size = size
        self.items = []
        self.bg = bg
        pass

    def update(self,Mpos,Mpressed):
        out = []
        for i in self.items:
            try:
                out.append(i.Update(Mpos-self.pos,Mpressed))
                pass
            except Exception as e:
                #print(e)
                pass
        return out

    def draw(self,screen):
        screen.fill(self.bg, (self.pos, self.size))
        for i in self.items:
            try:
                i.draw(screen,self.pos)
            except Exception as e:
                #print(e)
                pass

    def move(self,x,y):
        self.pos = self.pos+pygame.math.Vector2(x,y)
        
"""
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def Handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def Update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
"""
