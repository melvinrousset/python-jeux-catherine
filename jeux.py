import pygame
import asyncio


import screen_frame


class Player():
        
        
    def __init__(self,name,screen,tab_Rect,
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
    image_background,
    image_box):
        
        self._name = name
        self._screen = screen
        self._tab_Rect = tab_Rect
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
        self._image_box = image_box
        self.area_01 = screen_frame.Area(1,screen,image_background,box_image
        ,tab_Rect,tab_door,door)
    

    
 
    
    def talk(self):
        print(self._name)
        
        
         

    def up(self,x,y):
        print(self._name)
        move_y = 0
        print(self._name)
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_up_1,(x,y-move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_up_2,(x,y-move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_up_3,(x,y-move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        

    def down(self,x,y):
        move_y = 0
        print(self._name)
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_down_1,(x,y+move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_down_2,(x,y+move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_down_3,(x,y+move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        
    def left(self,x,y):
        print(self._name)
        move_x = 0
        print(self._name)
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_left_1,(x-move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
        
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_left_2,(x-move_x,y+10))
        pygame.display.flip()
        pygame.time.wait(100)
        
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_left_3,(x-move_x,y+10))
        pygame.display.flip()
        pygame.time.wait(100)
        

    def right(self,x,y):
      
        move_x = 0
        print(self._name)
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_right_1,(x+move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
        
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_right_2,(x+move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
        
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_right_3,(x+move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
        


    async def up_push(self,x,y):
        print(self._name)
        move_y = 0
        print(self._name)
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_up_1,(x,y-move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_up_2,(x,y-move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_up_3,(x,y-move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)

    async def down_push(self,x,y):
        move_y = 0
        print(self._name)
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_down_1,(x,y+move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_down_2,(x,y+move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)
        move_y += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_down_3,(x,y+move_y))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)
    
    async def left_push(self,x,y):
        print(self._name)
        move_x = 0
        print(self._name)
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_left_1,(x-move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_left_2,(x-move_x,y+10))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_left_3,(x-move_x,y+10))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)

    async def right_push(self,x,y):
      
        move_x = 0
        print(self._name)
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_right_1,(x+move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_right_2,(x+move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)
        move_x += 3
        self.area_01.refresh_arena()
        self._screen.blit(self._image_right_3,(x+move_x,y))
        pygame.display.flip()
        pygame.time.wait(100)
        await asyncio.sleep(0.1)


    async def up_grab(self,x,y):
        move_y = 0
        print(self._name)
        for i in range(3):
            move_y += 13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_down_1,(x,y-move_y))
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            move_y += 13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_down_2,(x,y-move_y))
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            move_y += 13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_down_3,(x,y-move_y))
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)

    async def down_grab(self,x,y):
        move_y = 0
        print(self._name)
        for i in range (3):
            move_y += 13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_up_1,(x-4,y+move_y))
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            move_y += 13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_up_2,(x-4,y+move_y))
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            move_y += 13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_up_3,(x-4,y+move_y))
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
    
    async def left_grab(self,x,y):
        print(self._name)
        move_x = 0
        print(self._name)
        for i in range(3):
            move_x += 13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_right_3,(x-move_x,y))
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            move_x += 13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_right_2,(x-move_x,y))
            pygame.display.flip()
            
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            move_x += 13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_right_1,(x-move_x,y))
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            

    async def right_grab(self,x,y):
      
        move_x = 0
        print(self._name)
        for i in range(3):
            move_x +=13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_left_1,(x+move_x,y-3))
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            move_x +=13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_left_2,(x+move_x,y+4))
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            move_x +=13
            self.area_01.refresh_arena()
            self._screen.blit(self._image_left_3,(x+move_x,y-2))
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)


    
          
            
    

    def jump(self):
        print(self._name)

    async def push_box(self,choice,index):

        if choice == "RIGHT":
            for i in range(3):
                        tab_Rect[index].x += 10
                        area_01.refresh_arena()
                        pygame.display.flip()
                        pygame.time.wait(100)
                        await asyncio.sleep(0.1)
                        tab_Rect[index].x += 11
                        area_01.refresh_arena()
                        pygame.display.flip()
                        pygame.time.wait(100)
                        await asyncio.sleep(0.1)
                        tab_Rect[0].x += 11
                        area_01.refresh_arena()
                        pygame.display.flip()
                        pygame.time.wait(100)
                        await asyncio.sleep(0.1)
     

        if choice == "LEFT":
            for i in range(3):
                        tab_Rect[index].x -= 10
                        area_01.refresh_arena()
                        pygame.display.flip()
                        pygame.time.wait(100)
                        await asyncio.sleep(0.1)
                        tab_Rect[index].x -= 11
                        area_01.refresh_arena()
                        pygame.display.flip()
                        pygame.time.wait(100)
                        await asyncio.sleep(0.1)
                        tab_Rect[index].x -= 11
                        area_01.refresh_arena()
                        pygame.display.flip()
                        pygame.time.wait(100)
                        await asyncio.sleep(0.1)
      

        if choice == "UP":
            for i in range(2):
                                tab_Rect[index].y -= 8
                                area_01.refresh_arena()
                                pygame.display.flip()
                                pygame.time.wait(100)
                                await asyncio.sleep(0.1)
                                tab_Rect[index].y -= 8
                                area_01.refresh_arena()
                                pygame.display.flip()
                                pygame.time.wait(100)
                                await asyncio.sleep(0.1)
                                tab_Rect[index].y -= 8
                                area_01.refresh_arena()
                                pygame.display.flip()
                                pygame.time.wait(100)
                                await asyncio.sleep(0.1)

            tab_Rect[index].y -= 8
            area_01.refresh_arena()
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            tab_Rect[index].y -= 8
            area_01.refresh_arena()
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            tab_Rect[index].y -= 9
            area_01.refresh_arena()
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)

        if choice == "DOWN":
            for i in range(2):
                        tab_Rect[index].y += 8
                        area_01.refresh_arena()
                        pygame.display.flip()
                        pygame.time.wait(100)
                        await asyncio.sleep(0.1)
                        tab_Rect[index].y += 8
                        area_01.refresh_arena()
                        pygame.display.flip()
                        pygame.time.wait(100)
                        await asyncio.sleep(0.1)
                        tab_Rect[index].y += 8
                        area_01.refresh_arena()
                        pygame.display.flip()
                        pygame.time.wait(100)
                        await asyncio.sleep(0.1)

            tab_Rect[index].y += 8
            area_01.refresh_arena()
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            tab_Rect[index].y += 8
            area_01.refresh_arena()
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)
            tab_Rect[index].y += 9
            area_01.refresh_arena()
            pygame.display.flip()
            pygame.time.wait(100)
            await asyncio.sleep(0.1)



pygame.init()

tab_Rect = []
tab_door = []
police = pygame.font.SysFont("monospace" ,80)
image_texte = police.render ( "YOU WIN!!!", 1 , (255,0,0) )
pressed_keys = pygame.key.get_pressed ()



"""

define the window

"""

resolution = (1200,700)

pygame.display.set_caption("Reprise Catherine")

screen = pygame.display.set_mode(resolution)

"""

song

"""

musique_game = pygame.mixer.Sound("Musique\ost_01.mp3")

musique_game.play()


"""

load images

"""


background_image = pygame.image.load("grass.png").convert_alpha()

player_image = pygame.image.load("player_sprite\player_3_1.png").convert_alpha()

box_image = pygame.image.load("final_box.png").convert_alpha()



player_up_1 = pygame.image.load("player_sprite\player_4_1.png").convert_alpha()
player_up_2 = pygame.image.load("player_sprite\player_4_2.png").convert_alpha()
player_up_3 = pygame.image.load("player_sprite\player_4_3.png").convert_alpha()
player_down_1 = pygame.image.load("player_sprite\player_1_1.png").convert_alpha()
player_down_2 = pygame.image.load("player_sprite\player_1_2.png").convert_alpha()
player_down_3 = pygame.image.load("player_sprite\player_1_3.png").convert_alpha()
player_left_1 = pygame.image.load("player_sprite\player_2_1.png").convert_alpha()
player_left_2 = pygame.image.load("player_sprite\player_2_2.png").convert_alpha()
player_left_3 = pygame.image.load("player_sprite\player_2_3.png").convert_alpha()
player_right_1 = pygame.image.load("player_sprite\player_3_3.png").convert_alpha()
player_right_2 = pygame.image.load("player_sprite\player_3_2.png").convert_alpha()
player_right_3 = pygame.image.load("player_sprite\player_3_3.png").convert_alpha()


door_image_01 = pygame.image.load("door_sprite\door_sprite_01.png").convert_alpha()
door_image_02 = pygame.image.load("door_sprite\door_sprite_02.png").convert_alpha()
door_image_03 = pygame.image.load("door_sprite\door_sprite_03.png").convert_alpha()
door_image_04 = pygame.image.load("door_sprite\door_sprite_04.png").convert_alpha()

door = (door_image_01,door_image_02,door_image_03,door_image_04)

"""

define Rect

"""


charactere_rect = pygame.Rect(400,400,37,38)



"""

create object

"""


player_01 = Player(
"Melvin",
screen,
tab_Rect,
player_up_1,
player_up_2,
player_up_3,
player_down_1,
player_down_2,
player_down_3,
player_left_1,
player_left_2,
player_left_3,
player_right_1,
player_right_2,
player_right_3,
background_image,
box_image
)





area_01 = screen_frame.Area(1,screen,background_image,box_image,tab_Rect,tab_door,door)

area_01.create_arena()




pygame.draw.rect(screen,"red",tab_Rect[0])

pygame.draw.rect( screen,"red",charactere_rect)

screen.blit(player_image,(400,370))

pygame.display.flip()


print(tab_Rect[0])


async def pull(direction,index):
    if direction == "LEFT":
        print("lalalalalal")


        
        task_grab = asyncio.create_task(player_01.left_grab(charactere_rect.x,charactere_rect.y-35))
        
        task_box = asyncio.create_task(player_01.push_box("LEFT",index))

        await asyncio.gather(task_grab,task_box)

        



        

    if direction == "RIGHT":
        task_grab = asyncio.create_task(player_01.right_grab(charactere_rect.x,charactere_rect.y-35))
        
        task_box = asyncio.create_task(player_01.push_box("RIGHT",index))

        await asyncio.gather(task_grab,task_box)
        


    if direction == "UP":

        task_grab = asyncio.create_task(player_01.up_grab(charactere_rect.x,charactere_rect.y-35))
        
        task_box = asyncio.create_task(player_01.push_box("UP",index))

        await asyncio.gather(task_grab,task_box)
        

    if direction == "DOWN":

        task_grab = asyncio.create_task(player_01.down_grab(charactere_rect.x,charactere_rect.y-35))
        
        task_box = asyncio.create_task(player_01.push_box("DOWN",index))

        await asyncio.gather(task_grab,task_box)

async def push(direction,index):
    if direction == "LEFT":
        print("lalalalalal")


        
        task_grab = asyncio.create_task(player_01.left_push(charactere_rect.x,charactere_rect.y-35))
        
        task_box = asyncio.create_task(player_01.push_box("LEFT",index))

        await asyncio.gather(task_grab,task_box)

        



        

    if direction == "RIGHT":
        task_grab = asyncio.create_task(player_01.right_push(charactere_rect.x,charactere_rect.y-35))
        
        task_box = asyncio.create_task(player_01.push_box("RIGHT",index))

        await asyncio.gather(task_grab,task_box)
        


    if direction == "UP":

        task_grab = asyncio.create_task(player_01.up_push(charactere_rect.x,charactere_rect.y-35))
        
        task_box = asyncio.create_task(player_01.push_box("UP",index))

        await asyncio.gather(task_grab,task_box)
        

    if direction == "DOWN":

        task_grab = asyncio.create_task(player_01.down_push(charactere_rect.x,charactere_rect.y-35))
        
        task_box = asyncio.create_task(player_01.push_box("DOWN",index))

        await asyncio.gather(task_grab,task_box)
        





launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

        pygame.draw.rect(screen,"red",tab_Rect[0])
        pygame.draw.rect(screen,"red",tab_Rect[1])
        pygame.draw.rect(screen,"red",tab_door[0])
        
        

        pygame.draw.rect( screen,"red",charactere_rect)

        

        pygame.display.flip()

        

    
        
        if event.type == pygame.KEYDOWN:
             
                pygame.draw.rect(screen,"red",charactere_rect)
                pygame.display.flip()
                pressed_keys = pygame.key.get_pressed ()

                if pressed_keys[pygame.K_z] and pressed_keys[pygame.K_RIGHT]:
                    charactere_rect.x -= 10
                    index = charactere_rect.collidelist(tab_Rect)
                    if not index:
                        
                        asyncio.run(pull("RIGHT",index))
                        charactere_rect.x += 115

                    charactere_rect.x += 20
                    index = charactere_rect.collidelist(tab_Rect)
                    if not index:
                        
                        asyncio.run(push("RIGHT",index))
                        charactere_rect.x += 115
                        
                        charactere_rect.x = tab_Rect[index].x - 30
                        

                
                        
                        
           
                elif pressed_keys[pygame.K_z] and pressed_keys[pygame.K_LEFT]:
                    charactere_rect.x += 10
                    index = charactere_rect.collidelist(tab_Rect)
                    if not index:

                        charactere_rect.x += 10
                        asyncio.run(pull("LEFT",0))
                        charactere_rect.x -= 115


                    charactere_rect.x -= 10
                    index = charactere_rect.collidelist(tab_Rect)
                    if not index:

                        charactere_rect.x += 20
                        asyncio.run(push("LEFT",0))
                        charactere_rect.x -= 115
                        charactere_rect.x = tab_Rect[index].x + 30
                       


                elif pressed_keys[pygame.K_z] and pressed_keys[pygame.K_UP]:
                    charactere_rect.y += 10
                    index = charactere_rect.collidelist(tab_Rect)
                    if not index:
                        asyncio.run(pull("UP",0))
                        charactere_rect.y -= 115

                    charactere_rect.y -= 20
                    index = charactere_rect.collidelist(tab_Rect)
                    if not index:
                        print("lolo")
                        asyncio.run(push("UP",0))
                        charactere_rect.y -= 115
                        charactere_rect.y = tab_Rect[index].y + 60
                        


                elif pressed_keys[pygame.K_z] and pressed_keys[pygame.K_DOWN]:
                    charactere_rect.y -= 10
                    index = charactere_rect.collidelist(tab_Rect)
                    if not index:
                        asyncio.run(pull("DOWN",0))
                        charactere_rect.y += 115

                    charactere_rect.y += 20
                    index = charactere_rect.collidelist(tab_Rect)
                    if not index:
                        asyncio.run(push("DOWN",0))
                        charactere_rect.y += 115
                        charactere_rect.y = tab_Rect[index].y - 60
                        

                    



                
                """
                for direction
                """

                if event.key == pygame.K_RIGHT:

                    charactere_rect.x += 10
                    
                    if not charactere_rect.collidelist(tab_Rect):
                        print("trop tard")
                        print(charactere_rect.x)
                        charactere_rect.x -= 10

                    else :
                        print("droite")
                        player_01.right(charactere_rect.x,charactere_rect.y-35)
                        print(charactere_rect.x)
                        charactere_rect.x += 9

                elif event.key == pygame.K_LEFT:

                    charactere_rect.x -= 10
                    
                    if not charactere_rect.collidelist(tab_Rect):
                        print("trop tard")
                        print(charactere_rect.x)
                        charactere_rect.x += 10

                    else:
                        print("gauche")
                        player_01.left(charactere_rect.x,charactere_rect.y-35)
                        print(charactere_rect.x)
                        charactere_rect.x -= 9
            
                elif event.key == pygame.K_UP:

                    charactere_rect.y -= 10
                    
                    if not charactere_rect.collidelist(tab_Rect):
                        print("trop tard")
                        print(charactere_rect.y)
                        charactere_rect.y += 10
                        


                    else :
                        print("haut")
                        player_01.up(charactere_rect.x,charactere_rect.y-35)
                        print(charactere_rect.y)
                        charactere_rect.y -= 9
                        charactere_rect.x += 5
            
                elif event.key == pygame.K_DOWN:

                    charactere_rect.y += 10
                    
                    if not charactere_rect.collidelist(tab_Rect):
                        print("trop tard")
                        print(charactere_rect.y)
                        charactere_rect.y -= 10
                        pygame.draw.rect(screen,"red",tab_Rect[0])
                        pygame.display.flip()

                    else:
                        print("bas")
                        player_01.down(charactere_rect.x,charactere_rect.y-35)
                        print(charactere_rect.y)
                        charactere_rect.y += 9


                if not charactere_rect.collidelist(tab_door):

                    if event.key == pygame.K_z:
                    
                        area_01.refresh_arena(0)
                        pygame.display.flip()
                        pygame.time.wait(500)
                        
                        area_01.refresh_arena(1)
                        pygame.display.flip()
                        pygame.time.wait(500)
                        
                        area_01.refresh_arena(2)
                        pygame.display.flip()
                        pygame.time.wait(500)
                        
                        area_01.refresh_arena(3)
                        pygame.display.flip()
                        pygame.time.wait(500)
                        screen.blit(image_texte, (320,240))
                        pygame.display.flip()


                
                    

                    

                
                            
                    

                       



                    


                    


                    



          
                


                
            
    
    