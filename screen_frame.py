import pygame
from dataclasses import dataclass


@dataclass
class Area():
    id : int
    screen : pygame.Surface
    background_image : pygame.Surface
    box : pygame.Surface
    list_box : pygame.Rect
    list_door : pygame.Rect
    door : tuple


    def draw_area(self):
        backround_limit_01 = 0
        backround_limit_02 = 0

        for i in range (2):
    
            for j in range(4):
                self.screen.blit(self.background_image,(backround_limit_01,backround_limit_02))
                backround_limit_01 += 384
                j += 1
            backround_limit_01 = 0
            backround_limit_02 += 384
            i+= 1


    def create_box(self,x,y):
        self.list_box.append(pygame.Rect(x,y,98,63))

    def draw_box(self):
        for box in self.list_box:
                self.screen.blit(self.box,(box.x-83,box.y-77))


    def create_door(self,x,y):
        self.list_door.append(pygame.Rect(x,y,50,50))


    def draw_door(self,level_door):
        for door in self.list_door:
                self.screen.blit(self.door[level_door],(door.x-10,door.y-50))



    def create_arena(self):
        if self.id == 1 :
            self.draw_area()
            self.create_box(500,273)
            self.create_box(500,200)
            self.create_box(700,573)
            self.create_box(100,150)
            self.create_door(200,330)
            self.draw_box()
            self.draw_door(0)

    def refresh_arena(self,level_door = 0):
        self.draw_area()
        self.draw_box()
        self.draw_door(level_door)


