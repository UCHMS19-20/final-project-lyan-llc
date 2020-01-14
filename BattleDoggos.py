import sys
import pygame
import random
import time 

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (1300, 560) )

#Load the image of the battlefield
background = pygame.image.load("img/BDField.png")
backgroundrect = background.get_rect()


#Creates a class for the two bases
class Base:
    def __init__(self, image, x, y): 
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
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.attack = attack
        self.defence = defense
        self.health = health


    #Make sure that the defense is the enemy player defense. Health is the enemy Health. 
    #this is activated when the player attacks (Right clicks) while colliding with the other player
    #still need to put the player collision code it
    """
    def damage(health, defense, attack):
        #If colliding and left click is pressed:
        damage = attack - defense
        health - damage
        """
        
#Images for Player 1 and 2

Player1Image = pygame.image.load("img/Player1Image.png")
Player2Image = pygame.image.load("img/Player2Image.png")


#Loads the players in their starting positions and with their stats
Player1 = Player(Player1Image, 300, 310, 6, 6, 6)
Player2 = Player(Player2Image, 700, 310, 6, 6, 6)


#Images for base 1 and 2
Base1Image = pygame.image.load("img/Base1.png")

Base2Image = pygame.image.load("img/Base2.png")


#Creates the base objects with custom location and images (Still need to put in location)
Base1 = Base(Base1Image, 2, 170)
Base2 = Base(Base2Image, 1100, 170)

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:

            # If so, exit the program
            sys.exit()
        #keydown and stuff if event.type == 


    #Draw the background, and bases in certain positions
    screen.blit(background, backgroundrect)
    screen.blit(Base1Image, Base1.rect)
    screen.blit(Base2Image, Base2.rect)
    screen.blit(Player1Image, Player1.rect)
    screen.blit(Player2Image, Player2.rect)
    pygame.display.flip()


    #Movement




    #Player collision Code



    #Damage to other player



    #Heal?





    












