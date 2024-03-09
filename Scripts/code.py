import pygame
import random
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import image_types
from array import *

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
inventory = []
cords = 0
reapet_trees = 50
tres = []
player_surf = pygame.image.load('player.bmp')
while reapet_trees != 0 :
    reapet_trees = reapet_trees - 1
    tres.append((random.randint(0,1000) , (random.randint(0,1000))))

count_tree = len(tres)
tree_surf = pygame.image.load('tree.bmp')
tree_rect = tree_surf.get_rect(bottomright=(30,50 ) , center=(200, 150))
sc.blit(tree_surf, tree_rect)
pygame.display.update()
chundra_surf = pygame.image.load('chundra.bmp')
chundra_count = 1

chundra = []
while chundra_count != 0 :
    chundra_count = chundra_count - 1
    chundra.append((random.randint(0,1000) , (random.randint(0,1000))))

chundra_max = len(chundra)
chundra_rect = chundra_surf.get_rect( bottomright = (10,20 ) , center= (tres[(count_tree - 1)]) )

player_rect = player_surf.get_rect(bottomright=(10,20 ) , center=(200, 150))
sc.blit(player_surf, player_rect)
pygame.display.update()

while count_tree != 0 :
    tree_surf = pygame.image.load('tree.bmp')
    count_tree = count_tree - 1

    tree_rect = tree_surf.get_rect( bottomright = (30,50 ) , center= (tres[count_tree]) )
    sc.blit(tree_surf, tree_rect)
    pygame.display.update()
count_tree = len(tres)
while chundra_max != 0 :
    chundra_surf = pygame.image.load('chundra.bmp')
    chundra_max = chundra_max - 1

    chundra_rect = chundra_surf.get_rect( bottomright = (30,50 ) , center= (tres[count_tree - 1]) )
    sc.blit(tree_surf, tree_rect)
    pygame.display.update()
chundra_max = len(chundra)
class obg:
    def __init__(self , ox , oy , osx , osy ,give):
        self.ox = ox
        self.oy = oy
        self.give = give
        self.osx = osx
        self.osy = osy
        pygame.draw.rect(sc , (0 , 255 , 0) , (self.ox , self.oy , self.osx , self.osy) )
        pygame.display.update()
    def update_obg(self):
        pygame.draw.rect(sc, (0, 255, 0), (self.ox, self.oy, self.osx, self.osy))
        pygame.display.update()
    def check (self , xp , yp) :
        if xp == self.ox and yp == self.oy :
            inventory.append(self.give)


stick = obg( 50 , 50 , 20 , 20 , "[wood stick]")
while 1 :


     def update(count_tree ,tree_surf , tree_rect , tres , chundra_max , x , y) :
         pygame.draw.rect(sc, (0, 0, 255), (0, 0, 1000, 1000), a)

         stick.update_obg()
         while count_tree != 0:
             tree_surf = pygame.image.load('tree.bmp')
             count_tree = count_tree - 1

             tree_rect = tree_surf.get_rect(bottomright=(30, 50), center=(tres[count_tree]))
             sc.blit(tree_surf, tree_rect)
         while chundra_max != 0:
             chundra_surf = pygame.image.load('chundra.bmp')
             chundra_max = chundra_max - 1
             xc ,yc = chundra[chundra_max]
             if x << xc :
                 del chundra[chundra_max]
                 xc = xc + 1
                 chundra.append((yc , xc))
             if x >> xc :
                 del chundra[chundra_max]
                 xc = xc - 1
                 chundra.append((yc , xc))
             if y << yc :
                 del chundra[chundra_max]
                 yc = yc - 1
                 chundra.append((yc , xc))
             if y >> yc :
                 del chundra[chundra_max]
                 yc = yc + 1
                 chundra.append((yc , xc))
             chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(chundra[chundra_max]))
             sc.blit(chundra_surf, chundra_rect)
             pygame.display.update()
         chundra_max = len(chundra)

         count_tree = len(tres)
         pygame.display.update()

         pygame.display.update()
     for event in pygame.event.get() :
          if event.type == pygame.QUIT:
              exit()
          stick.check(x , y)
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                  update(count_tree ,tree_surf , tree_rect , tres , chundra_max , x , y)
                  x = x - speed
                  player_rect = player_surf.get_rect(bottomright=(10, 20), center=(x, y))
                  sc.blit(player_surf, player_rect)
                  pygame.display.update()
              elif event.key == pygame.K_RIGHT:
                  update(count_tree ,tree_surf , tree_rect , tres , chundra_max , x , y)
                  x = x + speed
                  player_rect = player_surf.get_rect(bottomright=(10, 20), center=(x, y))
                  sc.blit(player_surf, player_rect)
                  pygame.display.update()
              elif event.key == pygame.K_DOWN:
                  update(count_tree ,tree_surf , tree_rect , tres , chundra_max , x , y)
                  y = y + speed
                  player_rect = player_surf.get_rect(bottomright=(10, 20), center=(x, y))
                  sc.blit(player_surf, player_rect)
                  pygame.display.update()
              elif event.key == pygame.K_UP:
                  update(count_tree ,tree_surf , tree_rect , tres , chundra_max , x , y)
                  y = y - speed
                  player_rect = player_surf.get_rect(bottomright=(10, 20), center=(x, y))
                  sc.blit(player_surf, player_rect)
                  pygame.display.update()
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
              else :
                  while chundra_max != 0:
                      chundra_surf = pygame.image.load('chundra.bmp')
                      chundra_max = chundra_max - 1
                      xc, yc = chundra[chundra_max]
                      if (x * 5) >= xc:
                          del chundra[chundra_max]
                          xc = xc + 1
                          chundra.append((yc, xc))
                          chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(chundra[chundra_max]))
                          sc.blit(chundra_surf, chundra_rect)
                          pygame.display.update()
                      if (x * 5) <= xc:
                          del chundra[chundra_max]
                          xc = xc - 1
                          chundra.append((yc, xc))
                          chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(chundra[chundra_max]))
                          sc.blit(chundra_surf, chundra_rect)
                          pygame.display.update()
                      if (y * 5) >= yc:
                          del chundra[chundra_max]
                          yc = yc - 1
                          chundra.append((yc, xc))
                          chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(chundra[chundra_max]))
                          sc.blit(chundra_surf, chundra_rect)
                          pygame.display.update()
                      if (y * 5) <= yc:
                          del chundra[chundra_max]
                          yc = yc + 1
                          chundra.append((yc, xc))
                          chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(chundra[chundra_max]))
                          sc.blit(chundra_surf, chundra_rect)
                          pygame.display.update()
                      chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(chundra[chundra_max]))
                      sc.blit(chundra_surf, chundra_rect)
                      pygame.display.update()
                  chundra_max = len(chundra)