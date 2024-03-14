from pygame import *

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

    def __init__(self, X: int, Y: int, sprite):
        self.posX = X
        self.posY = Y
        self.sprite = sprite
        self.spriteSurf = image.load(sprite)
