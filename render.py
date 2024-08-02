if __name__ == "__main__":
    print("Error! run the 'main.py' file to use it.\n"
          "You can write a unit tests for this file and place it here ;)")
    exit()

import pygame as pg


def render(windowScreen: pg.surface.Surface):
    windowScreen.fill(pg.Color(0, 0, 0)) # clear the screen.
    # место для отрисовки всего
    pg.display.flip()
    pass
