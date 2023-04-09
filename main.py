###############################
#        Racecar Runner       #
# Developed by Josh and Kelan #
#   Version 0.3 Dev Build     #
###############################

###########  
# IMPORTS #
###########

import pygame
import random
from pygame.locals import*

#############  
# Variables #
#############

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (14, 204, 27)
GRAY = (87, 84, 89)
YELLOW = (246, 255, 0)
GREY = (23, 204, 43)
BLUE = (24, 65, 245)
RED = (156, 36, 52)

# Images
img = pygame.image.load('car.png')
img1 = pygame.image.load('nails.png')
img2 = pygame.image.load('title.png')
img3 = pygame.image.load('wrench.png')
img4 = pygame.image.load('done.png')
img5 = pygame.image.load('glitch.png')
img6 = pygame.image.load('tree.png')

# Road Lines

line_y1 = -300
line_y2 = -100
line_change_y1 = 5
line_change_y2 = 5

# Car Health
car_hitpoints = 100

# Car Fix
car_fix = 20

# Speed
speed = 150

# Glitch Color
color = GREEN

# Music
music = 'background.wav'


#################
# Player Sprite #
#################
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(player, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        player.image = pygame.transform.scale(img,(75,150))
        screen.blit(player.image,(x,y))
 
        # Make our top-left corner the passed-in location.
        player.rect = player.image.get_rect()
        player.rect.x = x
        player.rect.y = y
 
        # -- Attributes
        # Set speed vector
        player.change_x = 0
        player.change_y = 0
 
    def changespeed(player, x, y):
        """ Change the speed of the player"""
        player.change_x += x
 
    def update(player):
        """ Find a new position for the player"""
        player.rect.x += player.change_x

################
# Nails Sprite #
################
class Nails(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(nails, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        nails.image = pygame.transform.scale(img1,(40,40))
        screen.blit(nails.image,(x,y))
 
        # Make our top-left corner the passed-in location.
        nails.rect = nails.image.get_rect()
        nails.rect.x = random.randrange(200,560)
        nails.rect.y = random.randrange(-2000,-1000)
 
        # -- Attributes
        # Set speed vector
        nails.change_x = 0
        nails.change_y = 3
 
    def changespeed(nails, x, y):
        """ Change the speed of the player"""
        nails.change_x += x
        nails.change_y += y
 
    def update(nails):
        """ Find a new position for the player"""
        nails.rect.x += nails.change_x
        nails.rect.y += nails.change_y

#################
# Wrench Sprite #
#################

class Wrench(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(wrench, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        wrench.image = pygame.transform.scale(img3,(100,50))
        screen.blit(wrench.image,(x,y))
 
        # Make our top-left corner the passed-in location.
        wrench.rect = wrench.image.get_rect()
        wrench.rect.x = random.randrange(200,550)
        wrench.rect.y = random.randrange(-5000,-4000)
 
        # -- Attributes
        # Set speed vector
        wrench.change_x = 0
        wrench.change_y = 2
 
    def changespeed(wrench, x, y):
        """ Change the speed of the player"""
        wrench.change_x += x
        wrench.change_y += y
 
    def update(wrench):
        """ Find a new position for the player"""
        wrench.rect.x += wrench.change_x
        wrench.rect.y += wrench.change_y

#################
# Glitch Sprite #
#################
class Glitch(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(glitch, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        glitch.image = pygame.transform.scale(img5,(60,60))
        screen.blit(glitch.image,(x,y))
 
        # Make our top-left corner the passed-in location.
        glitch.rect = glitch.image.get_rect()
        glitch.rect.x = random.randrange(200,550)
        glitch.rect.y = random.randrange(-5000,-4000)
 
        # -- Attributes
        # Set speed vector
        glitch.change_x = 0
        glitch.change_y = 2
 
    def changespeed(glitch, x, y):
        """ Change the speed of the player"""
        glitch.change_x += x
        glitch.change_y += y
 
    def update(glitch):
        """ Find a new position for the player"""
        glitch.rect.x += glitch.change_x
        glitch.rect.y += glitch.change_y

###############
# Tree Sprite #
###############
class Tree(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(tree, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        tree.image = pygame.transform.scale(img6,(175,300))
        screen.blit(tree.image,(x,y))
 
        # Make our top-left corner the passed-in location.
        tree.rect = tree.image.get_rect()
        tree.rect.x = random.randrange(0,740,600)
        tree.rect.y = random.randrange(-500,-100)
 
        # -- Attributes
        # Set speed vector
        tree.change_x = 0
        tree.change_y = 5
 
    def changespeed(tree, x, y):
        """ Change the speed of the player"""
        tree.change_x += x
        tree.change_y += y
 
    def update(tree):
        """ Find a new position for the player"""
        tree.rect.x += tree.change_x
        tree.rect.y += tree.change_y

        


# Call this function so the Pygame library can initialize itself
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play(loops=-1)
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Racecar Runner')
 
# Create the player object
player = Player(370, 400)
nails = Nails(100,100)
wrench = Wrench(100,100)
glitch = Glitch(100,100)
tree = Tree(100,100)
clock = pygame.time.Clock()
done = False

#############
# Main Menu #
#############

class GameMenu():
    def __init__(menu, screen, bg_color=(0,0,0)):
 
        menu.screen = screen
        menu.bg_color = bg_color
        menu.clock = pygame.time.Clock()
 
    def run(menu):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            menu.clock.tick(50)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

 
            # Redraw the background
            menu.screen.fill(BLACK)
            background = pygame.transform.scale(img2,(800,600))
            screen.blit(background,(0,0))
            pygame.display.flip()
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(loops=-1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mainloop = False

if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Racecar Runner')
    gm = GameMenu(screen)
    gm.run()


#############
# Main Game #
#############

# Main Loop
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
 
    # --- Game logic
    # This calls update on all the sprites        
    if player.rect.x >= 100:
        player.rect.x == 100

    # Controls the line movment on the road
    for i in range(3):
        line_y1 += line_change_y1
        line_y2 += line_change_y2
        if line_y1 == 800:
            line_y1 = -300
            line_y2 = -100
            
    # All Sprites List
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)
    all_sprites_list.add(nails)
    all_sprites_list.add(wrench)
    all_sprites_list.add(tree)
    all_sprites_list.add(glitch)
    all_sprites_list.update()
    
    # All Objects List
    all_objects_list = pygame.sprite.Group()
    all_objects_list.add(nails)
    all_objects_list.add(glitch)
    all_objects_list.add(tree)
    all_objects_list.add(wrench)

    
    # Collision List
    collision_list = pygame.sprite.spritecollide(player, all_objects_list, True)

    # Effects from collision with nails
    while nails in collision_list:
        car_hitpoints -= 5
        nails.rect.y = random.randrange(-2000,-1000)
        nails.rect.x = random.randrange(200,560)
        collision_list.remove(nails)
        
    # Effects from collision with glitch    
    while glitch in collision_list:
        glitch.rect.y = random.randrange(-10000,-8000)
        glitch.rect.x = random.randrange(200,560)
        color = RED
        speed = 1000
        collision_list.remove(glitch)

    # Effects from collision with wrench
    while wrench in collision_list:
        if car_hitpoints + car_fix >= 100:
            car_hitpoints = 100
            color = GREEN
            speed = 150
        else:
            car_hitpoints += 20
        wrench.rect.y = random.randrange(-5000,-4000)
        wrench.rect.x = random.randrange(200,550)
        collision_list.remove(wrench)

    # Effects from collision with Tree
    while tree in collision_list:
        car_hitpoints -= 30
        tree.rect.x = random.randrange(0,740,600)
        tree.rect.y = random.randrange(-500,-100)
        collision_list.remove(tree)

    # Nails Reset
    if nails.rect.y >= 1000:
        nails.rect.y = random.randrange(-2000,-1000)
        nails.rect.x = random.randrange(200,560)

    # Glitch Reset
    if glitch.rect.y >= 5000:
        glitch.rect.y = random.randrange(-10000,-8000)
        glitch.rect.x = random.randrange(200,560)

    # Wrench Reset
    if wrench.rect.y >= 2000:
        wrench.rect.y = random.randrange(-2000,-1000)
        wrench.rect.x = random.randrange(200,560)

    # Tree Reset
    if tree.rect.y >= 1000:
        tree.rect.x = random.randrange(0,740,600)
        tree.rect.y = random.randrange(-500,-100)

    # Forces car to say on screen
    LBuffer = 0
    RBuffer = 725
    if player.rect.x > RBuffer:
        player.rect.x = RBuffer
    if player.rect.x < LBuffer:
        player.rect.x = LBuffer

        
    if car_hitpoints <= 0:
        done = True


    # -- Draw everything
    # Clear screen
    screen.fill(color)
    pygame.draw.rect(screen, GRAY, [200,0,400,1000])
    pygame.draw.line(screen, YELLOW, [400, line_y1], [400, line_y2], 5)
    # Car Damage Text
    font = pygame.font.SysFont('Calibri', 20, False, False)
    text = font.render(str(car_hitpoints), True,BLUE)
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [65, 10])
    font = pygame.font.SysFont('Calibri', 20, False, False)
    text = font.render("Car HP:", True,BLUE)
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [0, 10])
    # Draw sprites
    all_sprites_list.draw(screen)
    # Flip screen
    pygame.display.flip()
 
    # Pause
    clock.tick(speed)


###################
# GAMEOVER SCREEN #
###################

class GameMenu():
    def __init__(menu, screen, bg_color=(0,0,0)):
 
        menu.screen = screen
        menu.bg_color = bg_color
        menu.clock = pygame.time.Clock()
 
    def run(menu):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            menu.clock.tick(50)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

 
            # Redraw the background
            menu.screen.fill(BLACK)
            background = pygame.transform.scale(img4,(800,600))
            screen.blit(background,(0,0))
            pygame.display.flip()
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(loops=-1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mainloop = False

if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Racecar Runner')
    gm = GameMenu(screen)
    gm.run()
pygame.quit()
