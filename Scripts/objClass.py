from pygame import *
from vec2 import *

class drawObj:
    """
    класс содержит в себе базовые свойства обьекта.
    должен быть родительским классом для всех остальных обьектов.
    предназначен для обработки разнородных обьектов группой
    """
    posX = 0
    posY = 0
    sprite = ""
    spriteSurf: Surface

    # def draw(self):
    #   TODO: drawing most be move here and use for overload in child classes
    def hover(self):
        return self.__class__

    def __init__(self, X: int, Y: int, sprite):
        self.posX = X
        self.posY = Y
        self.sprite = sprite
        self.spriteSurf = image.load(sprite) # возможно сделали х**ню...
        # возможно не стоит хранить копью спрайта в КАЖДОМ обьекте...
        # возможно... не понятно как сделать лучше

class tree(drawObj):
    def __init__(self, X: int, Y: int):
        super().__init__(X, Y, "tree.bmp")
        pass

class item(drawObj):
    id = "cocos"
    pass

class player_t(drawObj):
    health = 100
    oxygen = 100
    inv: list[item] = []
    move = [0, 0, 0, 0]
    speed = 3

    def __init__(self, posX=0, posY=0):
        self.mov = vec2()
        # self.posX = posX
        # self.posY = posY
        super().__init__(posX, posY, "player.bmp")
        # self.col = [200, 150, 50]
        pass
    pass