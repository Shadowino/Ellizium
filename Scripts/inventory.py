import pygame
Wsize = (1024, 720)
sc = pygame.display.set_mode(Wsize)
class inven :
    def write_hand(self) :
        pygame.draw.rect(sc,(255,255,255) , (0 , 0 , 100 , 100) )
        pygame.draw.rect(sc,(255,255,255) , (924 , 0 , 100 , 100))
        pygame.display.update()
    def right_arm_give(self,img) :
        self.img = img
        right_arm_surf = pygame.image.load(img)
        right_arm_rect = right_arm_surf.get_rect(bottomright=(10, 20), center=(5, 5))
    def right_arm_give(self,img) :
        self.img = img
        left_arm_surf = pygame.image.load(img)
        left_arm_rect = left_arm_surf.get_rect(bottomright=(10, 20), center=(924, 5))
        
        