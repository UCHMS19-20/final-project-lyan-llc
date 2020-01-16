# import sys, pygame, random, and time to use later
import sys
import pygame
import random
import time

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (1300, 560) )

# Create colors and color list
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
color_list = [black, white]

# Create font objects
big_font = pygame.font.SysFont("Comicsansms", 75)
medium_font = pygame.font.SysFont("Comicsansms", 50)
little_font = pygame.font.SysFont("Comicsansms", 25)

# LOAD ALL IMAGES
# background images and create rects
battle_BG = pygame.image.load("img/BDField.png")
backgroundrect = battle_BG.get_rect()
cloud_BG = pygame.image.load("img/AbilitiesBG2.png")

# player images
Player1Image = pygame.image.load("img/Player1Image.png")
Player2Image = pygame.image.load("img/Player2Image.png")

# # images for bases
# Base1Image = pygame.image.load("img/Base1.png")
# Base2Image = pygame.image.load("img/Base2.png")
# button images
dice = pygame.image.load("img/red_dice.gif")
start_battle_button = pygame.image.load(img/startbattle.jpg)

# Create classes Player and Button

# class Base:
#     def __init__(self, image, x, y):
#         '''Base is defined by its image and coordinates'''
#         self.health = 1000
#         self.image = image
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
# """
#     def Damage(damage):

# """

class Player:
    def __init__(self, name, image, x, y, attack, defense, health):
        '''Player is defined by its image, coordinates, and abilities'''
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.attack = attack
        self.defense = defense
        self.health = health

    # def attack(self, attack):


    #Make sure that the defense is the enemy player defense. Health is the enemy Health. 
    #this is activated when the player attacks (Right clicks) while colliding with the other player
    #still need to put the player collision code it
    """
    def damage(health, defense, attack):
        #If colliding and left click is pressed:
        damage = attack - defense
        health - damage
        """

class Button:
    def __init__(self, img, x, y):
        '''Button is defined by rect and image, as well as if it is active'''
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = x, y
        self.message = f"{x},{y}"
        self.is_active = True
    
    def has_mouse(self):
        '''Return True if mouse is in button and False otherwise'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False
    
    def roll_die(self):
        '''Return random integer between 0 and 6'''
        return random.randint(1,6)
      
# # Create 2 bases using Base class
# Base1 = Base(Base1Image, 2, 170)
# Base2 = Base(Base2Image, 1100, 170)

# Create 2 players using Player class
Player1 = Player("Player 1", Player1Image, 300, 310, 0, 0, 0)
Player2 = Player("Player 2", Player2Image, 700, 310, 0, 0, 0)
# create a list of players
players = [Player1, Player2]


# set initial value of if the dice is being rolled to False
dice_rolling = False

def background(image):
    ''' Function fills background of screen with the indicated image'''
    screen.fill((0,0,0))
    screen.blit(image, (0,0))
    return

def text(text, size, color, x, y):
    ''' Function displays text on the screen with the specified attributes'''
    screen.blit(size.render(text, True, color), (x, y))
    return

# set variable equation to get_pressed function, to get state of keys
keys = pygame.key.get_pressed()

# TITLE SCREEN
'''press enter to break and move to next screen'''
while True:
    # display cloud background
    background(cloud_BG)
   
    # display title screen text
    text("Welcome to...", medium_font, white, 100, 180)
    text("BATTLE DOGGOS", big_font, white, 100, 380)
    text("Press enter to continue.", little_font, white, 100, 580)
    
    # if return is pressed, break loop
    if keys[pygame.K_RETURN]:
        break
    
    # "flip" screen for this frame and then While True loop repeats
    pygame.display.flip()

# RULES SCREEN
while True:
    '''press enter to break and move to next screen'''
    # display cloud background
    background(cloud_BG)
    
    # display rules
    text("Rules", medium_font, white, 100, 180)
    text("Rules rules rules rules rules rules rules rules rules", medium_font, white, 100, 380)
    
    # if return is pressed, break loop
    if keys[pygame.K_RETURN]:
        break
    
    # "flip" screen for this frame and then While True loop repeats
    pygame.display.flip()

# ABILITIES SCREEN
for p in players:
    # Create list of 3 buttons that look like the red dice (using Button class)
    dice_list = []
    for y in range(3):
        dice_list.append(Button(dice, 525, y * 200 + 160))

    # Create blank list of 3 aspects of the dice (later to be abilities)
    dice_values = [0,0,0]
    
    while True:
        # if the dice is in the process of rolling, display "Dice rolling..." and wait 3 seconds
        if dice_rolling == True:
            screen.blit((medium_font.render(f"Dice rolling...", True, white)), (40, 200))
            pygame.display.flip()
            pygame.time.wait(3000)
            # set back to False so the program doesn't pause again until another die is rolled
            dice_rolling = False 

        # display text
        text(f"{p.name}", little_font, white, 800, 0)
        # display the same words twice in white and black, offset to create a shadow effect
        for n in len(color_list):
            text(f"Attack: {p.attack}", little_font, color_list[n], 598+2*n, 180)
            text(f"Defense: {p.defense}", little_font, color_list[n], 598+2*n, 380)
            text(f"Health: {p.health}", little_font, color_list[n], 598+2*n, 580)

        # set the abilities to the values in the dice_values list
        p.attack, p.defense, p.health = dice_values

        # draw all three dice in the dice_list
        for d in dice_list:
            screen.blit(d.img, d.rect)

        # create the "Start Battle" button
        start_battle = Button()

        # get position of mouse
        mouse_pos = pygame.mouse.get_pos()
    
        for event in pygame.event.get():
            # Check to see if the current event is a QUIT event
            if event.type == pygame.QUIT:
                # If so, exit the program
                sys.exit()
        
            # check if mouse is pressing down
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if the mouse is on a die (while it presses down)
                for i in range(0, len(dice_list)):
                    if dice_list[i-2].has_mouse() and dice_list[i].is_active:
                        # "roll die" and get a random number
                        dice_values[i-2] = dice_list[i].roll_die()
                        # set dice_rolling to True so in the next frame, the progrram will pause and display "Dice Rolling..."
                        dice_rolling = True
                        # just for testing purposes
                        print(f"Attack = {dice_values[0]}")
                        print(f"Defense = {dice_values[1]}")
                        print(f"Health = {dice_values[2]}")
                        print("________")
                        # Deactivate the button
                        dice_list[i].is_active = False
                # check if the mouse is on the start button (while it presses down)
                if start_battle.has_mouse():
                    pygame.time.wait(1000)
                    break
        
        # if any die is still active, the parentheses return True, which is negated and if statement will not run
        # if all dice have been clicked, the parenthese return False, which is negated and if statement runs
        if (dice_list[0].is_active or dice_list[1].is_active or dice_list[2].is_active) == False:
            # draw the "Start Battle!" buttton
            screen.blit(start_battle.img, start_battle.rect)
        
        # "flip" screen for this frame and then While True loop repeats
        pygame.display.flip()

# BATTLE SCREEN
while True:
    # Display battle background
    background(battle_BG)
    # # Draw the bases in certain positions
    # '''screen.blit(Base1Image, Base1.rect)
    # screen.blit(Base2Image, Base2.rect)'''

    screen.blit(Player1Image, Player1.rect)
    screen.blit(Player2Image, Player2.rect)
    pygame.display.flip()

    #Movement

    # check if players are colliding
    if Player1.rect.colliderect(Player2.rect) == True:
        print ("Players are colliding")
        

         # damage to other player

    #Heal?

# END-OF-GAME SCREEN