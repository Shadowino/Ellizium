from tkinter import *
from tkinter import ttk
from objClass import *
from events import *
from inventory import *

# import pygame
# import time
# from tkinter import image_types
# from array import *
# инициализация всякого
pygame.init()
Wsize = (1024, 720)  # размеры окна, вместо магических чисел
# x = 500
# y = 500
# хорактеристики перса
# hp = random.randint(1, 100)
# oxi = random.randint(1, 100)
gen = random.randint(1, 3)
patolagies = []
count_patolagies = random.randint(1, 3)
while count_patolagies != 0:
    patolagies.append(random.randint(1, 3))
    count_patolagies = count_patolagies - 1
# speed = 5 # больше не используеться см класс player_t в objClass.py
cords = 0


# отрисовка травы из граф примов
def DrawGrass(x, y):
    # self.x = x
    # self.y = y
    pygame.draw.polygon(sc, (0, 255, 0),
                        [(x, y), (x + 1.5, y + 1.5), (x - 1.5, y + 1.5)])
    # [(x1, y1), (x2, y2), (x3, y3)]
    # pygame.draw.polygon(sc,(0,255,0),(((x,y)),((x-3,y-3),(x,y-3))))


# инициализация окна
pygame.display.set_caption("окно Элизиума")
pygame.display.set_icon(pygame.image.load("icon.bmp"))
sc = pygame.display.set_mode(Wsize)
sc.fill((0, 0, 255))
pygame.display.update()

player: player_t = player_t()

# здесь все surf
player_surf = pygame.image.load('player.bmp')
cupper_surf = pygame.image.load("cupper.bmp")
tree_surf = pygame.image.load('tree.bmp')
chundra_surf = pygame.image.load('chundra.bmp')
castle_surf = pygame.image.load('castle.bmp')

# стартовые массивы для генерации
tres = []
cuppers = []
castles = []
chundra = []
grass = []

# ээээ ок
reapet_trees = 1000
reapet_cupper = 100
reapet_castles = 100
chundra_count = 0  # все люди как люди. а ты чундра коунт
reapet_grass = 1000

# генерация
while reapet_trees != 0:
    reapet_trees = reapet_trees - 1
    tres.append((random.randint(-2000, 2000), (random.randint(-2000, 2000))))
while reapet_cupper != 0:
    reapet_cupper = reapet_cupper - 1
    cuppers.append((random.randint(-2000, 2000), (random.randint(-2000, 2000))))
while reapet_castles != 0:
    reapet_castles = reapet_castles - 1
    castles.append((random.randint(-2000, 2000), (random.randint(-2000, 2000))))
while chundra_count != 0:
    chundra_count = chundra_count - 1
    chundra.append((random.randint(0, 1000), (random.randint(0, 1000))))
while reapet_grass != 0:
    reapet_grass = reapet_grass - 1
    DrawGrass(random.randint(-10000, 10000), random.randint(-10000, 10000))
# -_-
count_tree = len(tres)
count_cupper = len(cuppers)
count_castle = len(castles)
chundra_max = len(chundra)

# rect всех мастей
chundra_rect = chundra_surf.get_rect(bottomright=(10, 20), center=(tres[(count_tree - 1)]))  # причем тут count_tree?
tree_rect = tree_surf.get_rect(bottomright=(30, 50), center=(200, 150))
player_rect = player_surf.get_rect(bottomright=(10, 20), center=(500, 500))

Gobj: list[drawObj] = []  # список всех обьектов
# загрузка обьектов в общий список всего
for i in tres:
    Gobj.append(tree(i[0], i[1]))
for i in cuppers:
    Gobj.append(drawObj(i[0], i[1], "cupper.bmp"))
for i in castles:
    Gobj.append(drawObj(i[0], i[1], "castle.bmp"))


def phisicsUpdate():
    """
    занимаеться обработкой игровых событий
    :return:
    """
    npos = vec2(0, 0)
    if player.move[0]:
        npos.y -= 1
    if player.move[1]:
        npos.x += 1
    if player.move[2]:
        npos.y += 1
    if player.move[3]:
        npos.x -= 1

    npos += npos.norm() * player.speed
    # npos = player.mov.norm() * player.speed
    player.posX += npos.x
    player.posY += npos.y
    pass


# инвентарь
ooo = inven()
left_arm = ""
right_arm = "tree.bmp"

reve = events()

# функция открисовки обьектов из списка Gobj
def drawUPD(x, y):
    """
    функция открисовки всего, замена для update \n
    **warning работает с глобальной `sc`** \n
    TODO: **переписать** `update` сюда \n
    """
    sc.fill((0, 255, 255))  # правильная очистка экрана..
    # pygame.draw.rect(sc, (0, 255, 255), (0, 0, 1000, 1000), a)  # очистка экрана..
    Mrect = pygame.draw.rect(sc, [255, 255, 255], [mouse.get_pos(), (3, 3)], 2)
    # player_rect =
    sc.blit(player_surf, player_surf.get_rect(bottomright=(10, 20), center=(500, 500)))
    for iObj in Gobj:
        ox, oy = (iObj.posX - x, iObj.posY - y)
        sp = iObj.spriteSurf
        rec = sc.blit(sp, (ox, oy))
        if Mrect.colliderect(rec):
            pygame.draw.rect(sc, [255, 255, 255], pygame.Rect(ox, oy, sp.get_width(), sp.get_height()), 2)

        # pygame.draw.rect(sc, [255, 255, 255], pygame.Rect(ox, oy, sp.get_width(), sp.get_height()), 2)
        # tree_surf = pygame.image.load(i.sprite)
        # tree_rect = tree_surf.get_rect(bottomright=(30, 50), center=(ox, oy))
        pass
    interface(player)
    drawText("build:debug", 10, 10)
    drawText("mouse:" + str(mouse.get_pos()), 10, 20)
    pygame.display.update()  # необходимо для самостоятельной работы функции

    phisicsUpdate()
    # events.rain(1000)
    # reve.partical_rain(1000)
    # hand_write
    ooo.right_arm_give(right_arm)
    pass


def drawText(text: str, posX, posY):
    """
    функция открисовки текста \n
    !warning работает с глобальной `sc`!
    """
    text1 = pygame.font.SysFont("consolas", 15).render(text, True, (10, 10, 10))
    sc.blit(text1, (posX, posY))


def interface(pl: player_t):
    hp = pl.health
    oxi = pl.oxygen
    # oxi = round(time.time()*1000.0) % 100; # TEST
    pygame.draw.rect(sc, (oxi*2, oxi*2, 255), (900, 644, oxi, 6))
    pygame.draw.rect(sc, (255, 0, 0), (900, 650, hp, 20))
    pygame.display.update()


def update(chundraNb, x, y):
    sc.fill((0, 255, 255))  # ПРАВИЛЬНАЯ очистка экрана
    drawUPD(x, y)  # заменяет весь закоментированный ниже код
    # я не буду к этому прикасаться!!!
    while chundraNb != 0:
        chundra_surf = pygame.image.load('chundra.bmp')
        chundraNb = chundraNb - 1
        xc, yc = chundra[chundraNb]
        if x << xc:
            del chundra[chundraNb]
            xc = xc + 1
            chundra.append((yc, xc))
        if x >> xc:
            del chundra[chundraNb]
            xc = xc - 1
            chundra.append((yc, xc))
        if y << yc:
            del chundra[chundraNb]
            yc = yc - 1
            chundra.append((yc, xc))
        if y >> yc:
            del chundra[chundraNb]
            yc = yc + 1
            chundra.append((yc, xc))
        chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(chundra[chundraNb]))
        sc.blit(chundra_surf, chundra_rect)
        pygame.display.update()
    chundraNb = len(chundra)
    # count_tree = len(tres)
    pygame.display.update()  # много дупликатов
    drawText("FPS" + str(15), 15, 0)


while 1:
    # drawUPD(x, y)  # постоянная отрисовка. по хорошому должна быть тредом
    update(chundra_max, player.posX,
           player.posY)
    # update(count_castle, count_cupper, cupper_surf, count_tree, tree_surf, tree_rect, tres, chundra_max, x,
    #        y, hp)
    time.sleep(0.005)  # оптимизация производительности

    # г.. ниже НЕОБХОДИМО вынести в отдельную функцию
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            pass
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_UP:
                    player.move[0] = 0
                    pass
                case pygame.K_DOWN:
                    player.move[2] = 0
                    pass
                case pygame.K_LEFT:
                    player.move[3] = 0
                    pass
                case pygame.K_RIGHT:
                    player.move[1] = 0
                    pass
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    player.move[0] = 1
                    pass
                case pygame.K_DOWN:
                    player.move[2] = 1
                    pass
                case pygame.K_LEFT:
                    player.move[3] = 1
                    pass
                case pygame.K_RIGHT:
                    player.move[1] = 1
                    pass
            if event.key == pygame.K_ESCAPE:
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
                ttk.Label(text="inventory").pack(anchor=NW)
                inv.mainloop()
            else:
                # здесь была открисовка игрока
                # print(chundra_max)
                while chundra_max != 0:
                    chundra_surf = pygame.image.load('chundra.bmp')
                    chundra_max = chundra_max - 1
                    xc, yc = chundra[chundra_max]
                    if (player.posX * 5) >= xc:
                        del chundra[chundra_max]
                        xc = xc + 1
                        chundra.append((yc, xc))
                        chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(chundra[chundra_max]))
                        sc.blit(chundra_surf, chundra_rect)
                        pygame.display.update()
                    if (player.posX * 5) <= xc:
                        del chundra[chundra_max]
                        xc = xc - 1
                        chundra.append((yc, xc))
                        chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(chundra[chundra_max]))
                        sc.blit(chundra_surf, chundra_rect)
                        pygame.display.update()
                    if (player.posY * 5) >= yc:
                        del chundra[chundra_max]
                        yc = yc - 1
                        chundra.append((yc, xc))
                        chundra_rect = chundra_surf.get_rect(bottomright=(30, 50), center=(chundra[chundra_max]))
                        sc.blit(chundra_surf, chundra_rect)
                        pygame.display.update()
                    if (player.posY * 5) <= yc:
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
