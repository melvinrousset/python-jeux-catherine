from dataclasses import dataclass
import pygame
import screen_frame


"""
@dataclass
class Player():
    name : str
    screen : pygame.Surface
    image_up_1 : pygame.Surface
    image_up_2 : pygame.Surface
    image_up_3 : pygame.Surface
    image_down_1 : pygame.Surface
    image_down_2 : pygame.Surface
    image_down_3 : pygame.Surface
    image_left_1 : pygame.Surface
    image_left_2 : pygame.Surface
    image_left_3 : pygame.Surface
    image_right_1 : pygame.Surface
    image_right_2 : pygame.Surface
    image_right_3 : pygame.Surface
    image_background : pygame.Surface
    

 
   
    area_01 = screen_frame.Area(1,screen,image_background)

"""
import pygame




pygame.init()

tab_Rect = []

box_image = pygame.image.load("final_box.png").convert_alpha()

class Player():
        
        
    def __init__(self,name,screen,
    image_up_1,
    image_up_2,
    image_up_3,
    image_down_1,
    image_down_2,
    image_down_3,
    image_left_1,
    image_left_2,
    image_left_3,
    image_right_1,
    image_right_2,
    image_right_3,
    image_background):
        
        self._name = name
        self._screen = screen
        self._image_up_1 = image_up_1
        self._image_up_2 = image_up_2
        self._image_up_3 = image_up_3
        self._image_down_1 = image_down_1
        self._image_down_2 = image_down_2
        self._image_down_3 = image_down_3
        self._image_left_1 = image_left_1
        self._image_left_2 = image_left_2
        self._image_left_3 = image_left_3
        self._image_right_1 = image_right_1
        self._image_right_2 = image_right_2
        self._image_right_3 = image_right_3
        self._image_background = image_background
        self.area_01 = screen_frame.Area(1,screen,image_background,box_image
        ,tab_Rect)
    

    

    
    def talk(self):
        print(self._name)
        
        
        

    def up(self,x,y):
        print(self._name)
        move_y = 0
        print(self._name)
        move_y += 5
        self.area_01.refresh_arena()
        self._screen.blit(self._image_up_1,(x,y-move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        move_y += 10
        self.area_01.refresh_arena()
        self._screen.blit(self._image_up_2,(x,y-move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        move_y += 10
        self.area_01.refresh_arena()
        self._screen.blit(self._image_up_3,(x,y-move_y))
        pygame.display.flip()
        pygame.time.wait(100)

    def down(self,x,y):
        move_y = 0
        print(self._name)
        move_y += 5
        self.area_01.refresh_arena()
        self._screen.blit(self._image_down_1,(x,y+move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        move_y += 10
        self.area_01.refresh_arena()
        self._screen.blit(self._image_down_2,(x,y+move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        move_y += 10
        self.area_01.refresh_arena()
        self._screen.blit(self._image_down_3,(x,y+move_y))
        pygame.display.flip()
        pygame.time.wait(100)
    
    def left(self,x,y):
        print(self._name)
        move_x = 0
        print(self._name)
        move_x += 5
        self.area_01.refresh_arena()
        self._screen.blit(self._image_left_1,(x-move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
        move_x += 10
        self.area_01.refresh_arena()
        self._screen.blit(self._image_left_2,(x-move_x,y+10))
        pygame.display.flip()
        pygame.time.wait(100)
        move_x += 10
        self.area_01.refresh_arena()
        self._screen.blit(self._image_left_3,(x-move_x,y+10))
        pygame.display.flip()
        pygame.time.wait(100)

    def right(self,x,y):
      
        move_x = 0
        print(self._name)
        move_x += 5
        self.area_01.refresh_arena()
        self._screen.blit(self._image_right_1,(x+move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
        move_x += 10
        self.area_01.refresh_arena()
        self._screen.blit(self._image_right_2,(x+move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
        move_x += 10
        self.area_01.refresh_arena()
        self._screen.blit(self._image_right_3,(x+move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
          
            
    

    def jump(self):
        print(self._name)

    def grab(self):
        print(self._name)

