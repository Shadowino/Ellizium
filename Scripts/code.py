import pygame
import random
# import tkinter
from tkinter import *
from tkinter import ttk
# from tkinter import image_types
# from array import *

# инициализация всякого
pygame.init()
Wsize = (800, 600)  # размеры окна, вместо магических чисел
a = 0  # safdasd
x = 500
y = 500
speed = 5
inventory = []
cords = 0
reapet_trees = 1000
reapet_cupper = 100
tres = []
# inv = pygame.display.set_mode((100, 100)) # что это?
pygame.display.set_caption("окно Элизиума")
pygame.display.set_icon(pygame.image.load("icon.bmp"))
sc = pygame.display.set_mode(Wsize)
pygame.draw.rect(sc, (0, 0, 255), (0, 0, Wsize[0], Wsize[1]), a)
# gamer = pygame.draw.rect(sc, (255, 0, 0), (150, 150, 50, 20)) # не используеться!
pygame.display.update()

player_surf = pygame.image.load('player.bmp')
cupper_surf = pygame.image.load("cupper.bmp")
cuppers = []
castles = []
reapet_castles = 10
while reapet_trees != 0:
    reapet_trees = reapet_trees - 1
    tres.append((random.randint(-2000, 2000), (random.randint(-2000, 2000))))
while reapet_cupper != 0:
    reapet_cupper = reapet_cupper - 1
    cuppers.append((random.randint(-2000, 2000), (random.randint(-2000, 2000))))
while reapet_castles != 0:
    reapet_castles = reapet_castles - 1
    castles.append((random.randint(-2000, 2000), (random.randint(-2000, 2000))))

count_tree = len(tres)
tree_surf = pygame.image.load('tree.bmp')
tree_rect = tree_surf.get_rect(bottomright=(30, 50), center=(200, 150))
sc.blit(tree_surf, tree_rect)
pygame.display.update()
chundra_surf = pygame.image.load('chundra.bmp')
chundra_count = 0
castle_surf = pygame.image.load('castle.bmp')
chundra = []

while chundra_count != 0:
    chundra_count = chundra_count - 1
    chundra.append((random.randint(0, 1000), (random.randint(0, 1000))))

chundra_max = len(chundra)
chundra_rect = chundra_surf.get_rect(bottomright=(10, 20), center=(tres[(count_tree - 1)]))

player_rect = player_surf.get_rect(bottomright=(10, 20), center=(500, 500))
sc.blit(player_surf, player_rect)
pygame.display.update()


count_tree = len(tres)
count_cupper = len(cuppers)
count_castle = len(castles)
while chundra_max != 0:
    chundra_surf = pygame.image.load('chundra.bmp')
    chundra_max = chundra_max - 1

    chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(tres[count_tree - 1]))

    sc.blit(tree_surf, tree_rect)
    pygame.display.update()
chundra_max = len(chundra)

while 1:

    def drawText(text: str, posX, posY):
        """
        функция открисовки текста \n
        !warning работает с глобальной `sc`!
        """
        text1 = pygame.font.Font(None, 36).render(text, 1, (100, 0, 0))
        sc.blit(text1, (posX, posY))

    def update(count_castle, count_cupper, cupper_surf, count_tree, tree_surf, tree_rect, tres, chundra_max, x, y):
        pygame.draw.rect(sc, (0, 255, 255), (0, 0, 1000, 1000), a)  # очистка экрана..
        drawText("FPS" + str(15), 15, 0)
        while count_tree != 0:
            ox, oy = (tres[(count_tree - 1)])
            ox = ox - x
            oy = oy - y
            tree_surf = pygame.image.load('tree.bmp')
            count_tree = count_tree - 1
            tree_rect = tree_surf.get_rect(bottomright=(30, 50), center=(ox, oy))
            sc.blit(tree_surf, tree_rect)
        while count_cupper != 0:
            ocx, ocy = (cuppers[(count_cupper - 1)])
            ocx = ocx - x
            ocy = ocy - y
            cupper_surf = pygame.image.load('cupper.bmp')
            count_cupper = count_cupper - 1
            cupper_rect = cupper_surf.get_rect(bottomright=(20, 20), center=(ocx, ocy))
            sc.blit(cupper_surf, cupper_rect)
        while count_castle != 0:
            ocax, ocay = (castles[(count_castle - 1)])
            ocax = ocax - x
            ocay = ocay - y
            castle_surf = pygame.image.load('castle.bmp')
            count_castle = count_castle - 1
            castle_rect = castle_surf.get_rect(bottomright=(20, 20), center=(ocax, ocay))
            sc.blit(castle_surf, castle_rect)
        while chundra_max != 0:
            chundra_surf = pygame.image.load('chundra.bmp')
            chundra_max = chundra_max - 1
            xc, yc = chundra[chundra_max]
            if x << xc:
                del chundra[chundra_max]
                xc = xc + 1
                chundra.append((yc, xc))
            if x >> xc:
                del chundra[chundra_max]
                xc = xc - 1
                chundra.append((yc, xc))
            if y << yc:
                del chundra[chundra_max]
                yc = yc - 1
                chundra.append((yc, xc))
            if y >> yc:
                del chundra[chundra_max]
                yc = yc + 1
                chundra.append((yc, xc))
            chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(chundra[chundra_max]))
            sc.blit(chundra_surf, chundra_rect)
            pygame.display.update()
        chundra_max = len(chundra)
        count_tree = len(tres)
        pygame.display.update()  # много дупликатов


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # странное решение => вызывать update при событиях event
                update(count_castle, count_cupper, cupper_surf, count_tree, tree_surf, tree_rect, tres, chundra_max, x,
                       y)
                x = x - speed
                player_rect = player_surf.get_rect(bottomright=(10, 20), center=(500, 500))
                sc.blit(player_surf, player_rect)

                # pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                update(count_castle, count_cupper, cupper_surf, count_tree, tree_surf, tree_rect, tres, chundra_max, x,
                       y)
                x = x + speed
                player_rect = player_surf.get_rect(bottomright=(10, 20), center=(500, 500))
                sc.blit(player_surf, player_rect)
                pygame.display.update()
            elif event.key == pygame.K_DOWN:
                update(count_castle, count_cupper, cupper_surf, count_tree, tree_surf, tree_rect, tres, chundra_max, x,
                       y)
                y = y + speed
                player_rect = player_surf.get_rect(bottomright=(10, 20), center=(500, 500))
                sc.blit(player_surf, player_rect)
                pygame.display.update()
            elif event.key == pygame.K_UP:
                update(count_castle, count_cupper, cupper_surf, count_tree, tree_surf, tree_rect, tres, chundra_max, x,
                       y)
                y = y - speed
                player_rect = player_surf.get_rect(bottomright=(10, 20), center=(500, 500))
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
            elif event.key == pygame.K_F4:
                inv = Tk()
                inv.title("Инвентарь")
                inv.geometry("1000x1000")
                ttk.Label(text=inventory).pack(anchor=NW)
                inv.mainloop()
            else:
                # здесь была открисовка игрока
                print(chundra_max)
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
