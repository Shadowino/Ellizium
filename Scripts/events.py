import pygame
import random
import time
from inventory import *
Wsize = (1024, 720)
sc = pygame.display.set_mode(Wsize)
ooo = inven()
class events :
    count = 0
    def events():
        self.count = 0
        pass
    def partical_rain(self, count) :
        self.count = count
        while count != 0 :
            count = count - 1
            pygame.draw.rect(sc , (0,0,255) , [random.randint(0,1000) , random.randint(0,1000) , 5 , 10])
        
        ooo.write_hand()
        pygame.display.update()
        return self
        pass
    def partical_blink(self, timec) :
        self.timec = timec
        while timec != 0 :
            pygame.draw.rect(sc , (0,0,0) , (0 , 0 , 1000 , 1000))
            timec = timec - 1
        pygame.display.update()
        return self
        pass
    def partical_blink(self, timec) :
        self.timec = timec
        while timec != 0 :
            pygame.draw.rect(sc , (0,0,0) , (0 , 0 , 1000 , 1000))
            timec = timec - 1
        pygame.display.update()
        return self
        pass
        