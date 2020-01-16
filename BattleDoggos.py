# import sys, pygame, random, and time to use later
import sys
import pygame
import random
import time

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (1300, 560) )

# Create color(s)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

# Create font objects
big_font = pygame.font.SysFont("Comicsansms", 75)
medium_font = pygame.font.SysFont("Comicsansms", 50)
little_font = pygame.font.SysFont("Comicsansms", 25)

# LOAD ALL IMAGES
# background images and create rects
background = pygame.image.load("img/BDField.png")
backgroundrect = background.get_rect()
abilities_BG = pygame.image.load("img/AbilitiesBG2.png")
abilities_BGrect = background.get_rect()
# player images
Player1Image = pygame.image.load("img/Player1Image.png")
Player2Image = pygame.image.load("img/Player2Image.png")
# images for bases
Base1Image = pygame.image.load("img/Base1.png")
Base2Image = pygame.image.load("img/Base2.png")
# button images
dice = pygame.image.load("img/red_dice.gif")
start_battle_button = pygame.image.load(img/startbattle.jpg

# Create classes Base, Player, and Button
class Base:
    def __init__(self, image, x, y):
        '''Base is defined by its image and coordinates'''
        self.health = 1000
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
"""
    def Damage(damage):

"""

class Player:
    def __init__(self, image, x, y, attack, defense, health):
        '''Player is defined by its image, coordinates, and abilities'''
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
      
# Create 2 bases using Base class
Base1 = Base(Base1Image, 2, 170)
Base2 = Base(Base2Image, 1100, 170)

# Create 2 players using Player class
Player1 = Player(Player1Image, 300, 310, 6, 6, 6)
Player2 = Player(Player2Image, 700, 310, 6, 6, 6)
# create a list of players
players = [Player1, Player2]

# Create list of 3 buttons that look like the red dice (using Button class)
dice_list = []
for y in range(3):
    dice_list.append(Button(dice, 525, y * 200 + 160))

# Create blank list of 3 aspects of the dice (later to be abilities)
dice_values = [0,0,0]

# set initial value of if the dice is being rolled to False
dice_rolling = False

# TITLE SCREEN
'''press enter to break and move to next screen'''

# RULES SCREEN
'''press enter to break and move to next screen'''

# ABILITIES SCREEN
while True:
    # if the dice is in the process of rolling, display "Dice rolling..." and wait 3 seconds
    if dice_rolling == True:
        screen.blit((medium_font.render(f"Dice rolling...", True, white)), (40, 200))
        pygame.display.flip()
        pygame.time.wait(3000)
        # set back to False so the program doesn't pause again until another die is rolled
        dice_rolling = False 

    # display colors, images and text
    screen.fill((0,0,0))
    screen.blit(abilities_BG, (0,0))
    screen.blit(big_font.render("PLAYER 1", True, white), (800, 0))
    screen.blit(little_font.render("Click the dice to get your stats!", True, white), (800, 100))
    
    # set the abilities to the values in the dice_values list
    attack, defense, health = dice_values
   
    screen.blit((little_font.render(f"Attack: {attack}", True, black)), (598, 180))
    screen.blit((little_font.render(f"Defense: {defense}", True, black)), (598, 380))
    screen.blit((little_font.render(f"Health: {health}", True, black)), (598, 580))
   
    screen.blit((little_font.render(f"Attack: {attack}", True, white)), (600, 180))
    screen.blit((little_font.render(f"Defense: {defense}", True, white)), (600, 380))
    screen.blit((little_font.render(f"Health: {health}", True, white)), (600, 580))
    
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
        # check if mouse is pressing down on a button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # check if the mouse is on a button while it is pressing down
            for i in range(0, len(dice_list)):
                if dice_list[i-2].has_mouse() and dice_list[i].is_active:
                    # "roll die" and get a random number
                    dice_values[i-2] = dice_list[i].roll_die()
                    # 
                    dice_rolling = True
                    print(f"Attack = {dice_values[0]}")
                    print(f"Defense = {dice_values[1]}")
                    print(f"Health = {dice_values[2]}")
                    print("________")
                    dice_list[i].is_active = False
       
            if start_battle.has_mouse():
                pygame.time.wait(1000)
                break

# BATTLE SCREEN
While True:

    #Draw the background, and bases in certain positions
    screen.blit(background, backgroundrect)
    screen.blit(Base1Image, Base1.rect)
    screen.blit(Base2Image, Base2.rect)
    screen.blit(Player1Image, Player1.rect)
    screen.blit(Player2Image, Player2.rect)
    pygame.display.flip()

    #Movement

    # check if players are colliding
    if Player1.rect.colliderect(Player2.rect) == True:
        print ("Players are colliding")
            if 

         # damage to other player

    #Heal?

# END-OF-GAME SCREEN