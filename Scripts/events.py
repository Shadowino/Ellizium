import pygame
import random
import time
Wsize = (1024, 720)
sc = pygame.display.set_mode(Wsize)

class events :
    count = 0
    def events_partical():
        self.count = 0
        pass
    def partical_rain(self, count) :
        self.count = count
        while count != 0 :
            count = count - 1
            pygame.draw.rect(sc , (0,0,255) , [random.randint(0,1000) , random.randint(0,1000) , 5 , 10])
        pygame.display.update()
        return self
        pass
    def partical_thunder():
        pygame.draw.rect(sc , (0,0,255) , [ 500,  500, 50 , 500])
        pygame.display.update()
        pass
    def partical_fire():
        pygame.draw.rect(sc , (255,0,0) , [500 , 500 , 20 , 20])
        pygame.display.update()
        pass
    
        
