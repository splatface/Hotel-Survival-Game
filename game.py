import pygame, sys
from pygame.locals import *

pygame.init()

# Clock Setup
FPS = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 710))

#assortment of variables
night = False
run_one = True
count = 0 # for animation movements
count2 = 0 # for the duration of lights_off text box
count3 = 0 # for the ghost goal part
wait = 0 # wait for the key pressed to exit the room
stall = 0 # separates the time from inventory opened and closed
walk2 = 0
enter = True
hit = False
first_enter = True
key_in = False
bait_received = False
inventory_open = 0
bait_used = False
first_time = True
end = False


black = (0, 0, 0)
white = (255, 255, 255)



# character settings
CHARACTER_WIDTH = 219
CHARACTER_HEIGHT = 333

character_front = pygame.image.load("mc_front.png")
character_front = pygame.transform.scale(character_front, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

character_back = pygame.image.load("mc_back.png")
character_back = pygame.transform.scale(character_back, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

character_walking1 = pygame.image.load("mc_side.png") # walking right
character_walking1 = pygame.transform.scale(character_walking1, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

character_walking2 = pygame.image.load("mc_walking2.png") # walking right
character_walking2 = pygame.transform.scale(character_walking2, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

character_walking1_1 = pygame.transform.flip(character_walking1, True, False) # walking left
character_walking1_1 = pygame.transform.scale(character_walking1_1, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

character_walking1_2 = pygame.transform.flip(character_walking2, True, False) # walking left
character_walking1_2 = pygame.transform.scale(character_walking1_2, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

character_rect = character_front.get_rect()
move_speed = 5




#current room
room = 0

# loading the images into variables so they can be displayed later
first = pygame.image.load('1.jpg')  #11
second = pygame.image.load('2.jpg')  #12
third = pygame.image.load('3.jpg')  #13

# loading night images (variable names mean room # + night)
first_n = pygame.image.load('9.jpg')
second_n = pygame.image.load('10.jpg')
third_n = pygame.image.load('11.jpg')
fourth_n = pygame.image.load('12.jpg')
fifth_n = pygame.image.load('13.jpg')
sixth_n = pygame.image.load('14.jpg')
opened = pygame.image.load('6_1.jpg')

# other images
in_room = pygame.image.load('in_room.jpg')  #8
in_room_d = pygame.image.load('in_room_d.jpg')  #8
title = pygame.image.load('title_screen.jpg')  #0
dead = pygame.image.load('dead.jpg')
next = pygame.image.load('next.png')
get_key = pygame.image.load('pick up key.png')
go_in = pygame.image.load('Go_in.png')
go_out = pygame.image.load('Go_out.png')
goal = pygame.image.load('goal.jpg')
message = pygame.image.load('message.png')
lights_off = pygame.image.load('lights_off.png')
key = pygame.image.load('key.png')
key_used = pygame.image.load('key_used.png')
key_not_found = pygame.image.load('key_not_found.png')
leave = pygame.image.load('leave.png')
hotel_man = pygame.image.load('hotel_front.png')
hotel_sad = pygame.image.load('hotel_sad.png')
bait = pygame.image.load('bait.png')
get_bait = pygame.image.load('pick_up_bait.png')
inventory = pygame.image.load('inventory.jpg')
bait = pygame.transform.scale(bait, (300, 200))
use = pygame.image.load('use.png')
exit = pygame.image.load('exit.png')
end_screen = pygame.image.load('end_screen.jpg')
help = pygame.image.load('help.png')
help = pygame.transform.scale(help, (50, 50))
instructions = pygame.image.load('instructions.jpg')

# dialogues
d1 = pygame.image.load('dialogue_1.jpg')  #1
d2 = pygame.image.load('dialogue_2.jpg')  #2
d3 = pygame.image.load('creepy_dude.jpg')  #3

ghost = pygame.image.load('ghost.png')




# character movements + items +
class mc:
  x = 200
  y = 200

  hitbox = pygame.Rect(x, y, 180, 310)

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def movements(self):
    global count # for the walking animation (same for walk2)
    global walk2
    global room
    global enter
    global hit
    global count3
    global first_enter
    global bait_received
    global bait_used
    global first_time
    global inventory_open
    global end

    keys = pygame.key.get_pressed()
    x_movement = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT] + keys[pygame.K_d] - keys[pygame.K_a]
    y_movement = keys[pygame.K_DOWN] - keys[pygame.K_UP] + keys[pygame.K_s] - keys[pygame.K_w]
    # x/y_movement will return -1, 0, or 1 based on if no press (0), d or s (1), a or w (-1)
    # is based on the closeness to the upper left corner of the screen

    # Update character position based on input
    character_rect.x += x_movement * move_speed
    character_rect.y += y_movement * move_speed


    # room settings where the character movements affect the result
    if room == 25:
      if bait_used == False:
        screen.blit(hotel_man, (300, 400))
        hotel_man_rect = pygame.Rect(300, 400, 225, 325)
        screen.blit(leave, (450, 370))

        if character_rect.colliderect(hotel_man_rect) == True:
          character_rect.x -= 5
      
      if bait_used == True and (inventory_open == 0 or inventory_open == 2) and end == False:
        screen.blit(hotel_sad, (300, 400))

      if first_enter == True:
        character_rect.x = 75
        first_enter = False
      
      if character_rect.x >= 800:
        screen.blit(exit, (750, 50))

        if keys[pygame.K_e] == 1:
          end = True
      
    if room == 16:
      first_enter = True

    if room == 22:
      if enter == True:
        character_rect.topleft = (100, 200)
        enter = False
    
      ghost = pygame.Rect(560, 340, CHARACTER_WIDTH, CHARACTER_HEIGHT)
      if character_rect.colliderect(ghost) == True:
        screen.blit(goal, (0, 0))
        count3 += 1

        if count3 >= 150:
          room = 12
          hit = True



    # changing the room
    
    if room != 22 and room != 23 and room != 24 and room != 25:
      if character_rect.x >= 900:
        if room < 16:
          room += 1
          character_rect.x = 0

        if room == 16:
          character_rect.x -= 5

      if character_rect.x <= -100:
        if room > 11:
          room -= 1
          character_rect.x = 850

        if room == 11:
          character_rect.x += 5
    
    else:
      if character_rect.x >= 900:
        character_rect.x -= 5
      if character_rect.x <= -100:
        character_rect.x += 5




    # character will not be able to climb the walls
    if character_rect.y <= 180:
      character_rect.y += 5

    if character_rect.y >= 550:
      character_rect.y -= 5
    
    if keys[pygame.K_d] == 1 or keys[pygame.K_RIGHT]:
      count += 1

      if count >= 10:
        walk2 = 1 - walk2
        count = 0


      if walk2 == 1:
        screen.blit(character_walking2, character_rect.topleft)

      else:
        screen.blit(character_walking1, character_rect.topleft)

    elif keys[pygame.K_w] == 1 or keys[pygame.K_UP]:
      screen.blit(character_back, character_rect.topleft)

    elif keys[pygame.K_s] == 1 or keys[pygame.K_DOWN]:
      screen.blit(character_front, character_rect.topleft)

    elif keys[pygame.K_a] == 1 or keys[pygame.K_LEFT]:
      count += 1

      if count >= 10:
        walk2 = 1 - walk2
        count = 0


      if walk2 == 1:
        screen.blit(character_walking1_2, character_rect.topleft)

      else:
        screen.blit(character_walking1_1, character_rect.topleft)

    else:
      screen.blit(character_front, character_rect.topleft)



  # use collidepoint/colliderect method to see if the character runs into the obstacle
  def obstacles(self):
    global room
    global night

    self.ob_one = pygame.Rect(450, 475, 160, 50)
    self.ob_two = pygame.Rect(60, 660, 250, 100)
    self.ob_three = pygame.Rect(680, 670, 250, 100)
    self.ob_four = pygame.Rect(267, 640, 65, 50) 

    self.ob_five = pygame.Rect(60, 475, 70, 30)
    self.ob_six = pygame.Rect(435, 475, 40, 100)
    self.ob_seven = pygame.Rect(600, 475, 70, 30)
    self.ob_eight = pygame.Rect(900, 675, 100, 100)


    self.hitbox = pygame.Rect(character_rect.x + 55, character_rect.y + 280, 100, 30)

    if room == 13 or room == 15:
      if self.hitbox.colliderect(self.ob_one) == True or self.hitbox.colliderect(self.ob_two) == True or self.hitbox.colliderect(self.ob_three) == True or self.hitbox.colliderect(self.ob_four) == True:
        room = 20
    
    if room == 12 and night == True:
      if self.hitbox.colliderect(self.ob_five) == True or self.hitbox.colliderect(self.ob_six) == True or self.hitbox.colliderect(self.ob_seven) == True or self.hitbox.colliderect(self.ob_eight) == True:
        room = 20

character_rect.topleft = (100, 300)
character = mc(50, 250)

def main():
  global room
  global hit
  global night
  global enter
  global count2
  global key_in
  global bait_received
  global inventory_open
  global stall
  global bait_used
  global bait
  first_enter = True
  key_received = False
  title_screen = True
  on_instruction = False
  wait = 0

  screen.blit(title, (0, 0))
  start = pygame.Rect(450, 280, 302, 170)
  rules = pygame.Rect(365, 540, 335, 80)
  back = pygame.Rect(0, 0, 150, 100)
  question = pygame.Rect(920, 10, 50, 50)

  # The main game loop
  while True:
    keys = pygame.key.get_pressed()
    x, y = pygame.mouse.get_pos()

    # Get inputs
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        left, middle, right = pygame.mouse.get_pressed()
        if left == True:
          if room == 0:
            if rules.collidepoint(x, y) == True:
              screen.blit(instructions, (0, 0))
              title_screen = False

            elif back.collidepoint(x, y) == True:
              screen.blit(title, (0, 0))
              title_screen = True

            elif start.collidepoint(x, y) == True and title_screen == True:
              room = 1
              wait += 1

          if question.collidepoint(x, y) == True:
            screen.blit(instructions, (0, 0))
            on_instruction = True
          
          if on_instruction == True and back.collidepoint(x, y) == True:
            on_instruction = False

          
          if room == 20:
            room = 11
            night = False
            enter = True
            hit = False
            key_received = False
            first_enter = True
            bait_received = False
            bait_used = False
            key_in = False

          if room == 1:
            if wait >= 2:
              room += 1
              wait = 0
            wait += 1
            
          if room == 2:
            if wait >= 2:
              room += 1
              wait = 0
            wait += 1

          if room == 3:
            if wait >= 2:
              room += 1
            wait += 1
            
    if room == 1: #cutscene rooms
      screen.blit(d1, (0, 0))
      screen.blit(next, (0, 0))
    elif room == 2:
      screen.blit(d2, (0, 0))
      screen.blit(next, (0, 0))
    elif room == 3:
      screen.blit(d3, (0, 0))
      screen.blit(next, (0, 0))
    elif room == 4:
      room = 11

    # inventory
    if keys[pygame.K_i] == 1 and room != 0 and room != 1 and room != 2 and room != 3 and on_instruction == False:
      stall += 1
      # io = 0 means closed, io = 1 means open, io = 2 means no trigger again
    
      if inventory_open == 0: # opens inventory
        screen.blit(inventory, (0, 0))
        inventory_open = 1

        if key_received == True:
          screen.blit(key, (230, 250))
          screen.blit(use, (510, 250))
        
        if bait_received == True:
          bait = pygame.transform.scale(bait, (200, 125))
          screen.blit(bait, (188, 415))
          screen.blit(use, (510, 415))
    
      elif inventory_open == 1 and stall >= 8: # closes inventory
        inventory_open = 2
        stall = 0
      
      elif inventory_open == 2 and stall >= 8: # makes the delay for closing the inventory
        inventory_open = 0
        stall = 0
    
    if inventory_open == 1 and key_received == True and keys[pygame.K_u] == 1 and room == 16:
      key_in = True

    if inventory_open == 1 and bait_received == True and keys[pygame.K_u] == 1 and room == 25:
      bait_used = True

    if on_instruction == False and (inventory_open == 2 or inventory_open == 0):
      if room == 11: #starter room
        if night == True:
          screen.blit(first_n, (0, 0))
        else:
          screen.blit(first, (0, 0))

      elif room == 12:
        if night == True:
          screen.blit(second_n, (0, 0))
        else:
          screen.blit(second, (0, 0))
      
        if character_rect.x >= 650 and hit == False:
          screen.blit(go_in, (60, 600))

          if keys[pygame.K_y] == 1:
            room = 22
        
        if character_rect.x <= 250:
          screen.blit(go_in, (60, 600))

          if keys[pygame.K_y] == 1:
            room = 26

      elif room == 13:
        if night == True:
          screen.blit(third_n, (0, 0))
        else:
          screen.blit(third, (0, 0))

      elif room == 14:
        night = True
        screen.blit(fourth_n, (0, 0))
        count2 += 1
        first_enter = True

        if count2 <= 150:
          screen.blit(lights_off, (25, 25))
        
        if character_rect.x <= 250:
          screen.blit(go_in, (60, 600))

          if keys[pygame.K_y] == 1:
            room = 23
        
        if character_rect.x >= 550 and character_rect.x <= 830:
          screen.blit(go_in, (60, 600))

          if keys[pygame.K_y] == 1:
            room = 24

      elif room == 15:
        screen.blit(fifth_n, (0, 0))
      
      elif room == 16:
        if key_in == False:
          screen.blit(sixth_n, (0, 0))
          if character_rect.x >= 300 and character_rect.x <= 500:
            screen.blit(key_not_found, (60, 600))


        elif key_in == True:
          screen.blit(opened, (0, 0))

          if character_rect.x >= 300 and character_rect.x <= 500:
            screen.blit(go_in, (60, 600))

            if keys[pygame.K_y] == 1:
              room = 25
      

      # interior of rooms
      if room == 22:
        if night == True:
          screen.blit(in_room_d, (0, 0))
        else:
          screen.blit(in_room, (0, 0))
        screen.blit(ghost, (560, 340))
        screen.blit(message, (710, 320))
      
      if room == 23:
        screen.blit(in_room_d, (0, 0)) #can only enter this room after night becomes true

        if character_rect.x <= 250:
          screen.blit(go_out, (60, 600))
          paused = True

          if keys[pygame.K_x] == 1 and paused == True:
            room = 14
            paused = False
      
      if room == 24:
        screen.blit(in_room_d, (0, 0))

        if key_received == False:
          screen.blit(key, (900, 200))

        if first_enter == True:
          character_rect.x = 60
          first_enter = False

        if character_rect.x <= 250:
          screen.blit(go_out, (60, 600))
          paused = True

          if keys[pygame.K_x] == 1:
            room = 14
            character_rect.x = 690
            paused = False
        
        if character_rect.x >= 780 and key_received == False:
          screen.blit(get_key, (0, 0))
        
          if keys[pygame.K_y] == 1:
            key_received = True
        
      if room == 25:
        screen.blit(in_room_d, (0, 0))

        if character_rect.x <= 250:
          screen.blit(go_out, (60, 600))

          if keys[pygame.K_x] == 1:
            room = 16
      
      if room == 26:
        if night == True:
          screen.blit(in_room_d, (0, 0))
        else:
          screen.blit(in_room, (0, 0))
        
        if bait_received == False:
          screen.blit(bait, (500, 150))
      
          if character_rect.x >= 300 and character_rect.x <= 600:
            screen.blit(get_bait, (300, 50))

            if keys[pygame.K_y] == 1:
              bait_received = True
        
        if character_rect.x <= 250:
          screen.blit(go_out, (60, 600))

          if keys[pygame.K_x] == 1:
            room = 12



    if room != 0 and room != 1 and room != 2 and room != 3:
      screen.blit(help, (920, 10))

    if end == True:
      screen.blit(end_screen, (0, 0))

    if room == 20: #death
      screen.blit(dead, (0, 0))


    # running the other functions
    if room != 0 and room != 1 and room != 2 and room != 3 and room != 20 and (inventory_open == 0 or inventory_open == 2) and end != True and on_instruction == False:
      character.movements()
    
    if room == 13 or room == 15 or room == 12:
      character.obstacles()
    

    pygame.display.flip()
    fpsClock.tick(FPS)

  print("the end")


main()