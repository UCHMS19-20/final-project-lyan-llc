import sys
import pygame
import random
import time 

# Initialize pygame so it runs in the background and manages things
pygame.init()

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
    #still need to put the collision code it
    def damage(health, defense, attack):
        #If colliding and left click is pressed:
        damage = attack - defense
        health - damage
        

#Images for base 1 and 2
Base1Image = pygame.image.load("img/Base1.png")

Base2Image = pygame.image.load("img/Base2.png")



#Creates the base objects with custom location and images (Still need to put in location)
Base1 = Base(Base1Image, 30, 170)
Base2 = Base(Base2Image, 1100, 170)



# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (1300, 560) )

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:

            # If so, exit the program
            sys.exit()


    #Draw the background, and bases in certain positions
    screen.blit(background, backgroundrect)
    screen.blit(Base1Image, Base1.rect)
    screen.blit(Base2Image, Base2.rect)
    pygame.display.flip()

    #GameMechanics

    #Movement
    
    #Collision Code


    #Damage to other player

    #












