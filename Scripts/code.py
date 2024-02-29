import pygame
import random
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import image_types

pygame.init()
W ,H = 600 ,400
inv = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("окно Элизиума")
pygame.display.set_icon(pygame.image.load("icon.bmp"))
sc = pygame.display.set_mode((1000 ,1000))
a = 0
pygame.draw.rect(sc, (0 , 0 , 255) , (0,0,1000 , 1000) , a)
pygame.display.update()
x = 10
y = 10
gamer = pygame.draw.rect(sc,(255,0,0) , (500,500,50,20))
pygame.display.update()
speed = 5
count_of_grees = 100
inventory = []
class obg:
    def __init__(self , x , y , sx , sy ,give):
        self.x = x
        self.y = y
        self.give = give
        self.sx = sx
        self.sy = sy
        pygame.draw.rect(sc , (0 , 255 , 0) , (x , y , sx , sy) )
        pygame.display.update()

    def check (self , xp , yp) :
        if xp == self.x and yp == self.y :
            inventory.append(self.give)


stick = obg( 50 , 50 , 20 , 20 , "[wood stick]")
while 1 :



     for event in pygame.event.get() :
          if event.type == pygame.QUIT:
              exit()
          stick.check(x , y)
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                  pygame.draw.rect(sc, (0, 0, 0), (x, y, 5, 10), a)
                  x = x - speed
                  pygame.draw.rect(sc, (255, 0, 0), (x, y, 5, 10), a)
                  pygame.display.flip()
              elif event.key == pygame.K_RIGHT:
                  pygame.draw.rect(sc, (0, 0, 0), (x, y, 5, 10), a)
                  x = x + speed
                  pygame.draw.rect(sc, (255, 0, 0), (x, y, 5, 10), a)
                  pygame.display.flip()
              elif event.key == pygame.K_DOWN:
                  pygame.draw.rect(sc, (0, 0, 0), (x, y, 5, 10), a)
                  y = y + speed
                  pygame.draw.rect(sc, (255, 0, 0), (x, y, 5, 10), a)
                  pygame.display.flip()
              elif event.key == pygame.K_UP:
                  pygame.draw.rect(sc, (0, 0, 0), (x, y, 5, 10), a)
                  y = y - speed
                  pygame.draw.rect(sc, (255, 0, 0), (x, y, 5, 10), a)
                  pygame.display.flip()
              elif event.key == pygame.K_ESCAPE:
                  root = Tk()
                  root.title("Settings")
                  root.geometry("250x200")

                  val = IntVar(value=10)
                  ttk.Label(text="скорость:").pack(anchor=NW)
                  ttk.Label(textvariable=val).pack(anchor=NW)

                  horizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, variable=val)
                  horizontalScale.pack(anchor=NW)

                  root.mainloop()
              elif event.key == pygame.K_F4  :
                  inv = Tk()
                  inv.title("Инвентарь")
                  inv.geometry("1000x1000")
                  ttk.Label(text=inventory).pack(anchor=NW)
                  inv.mainloop()