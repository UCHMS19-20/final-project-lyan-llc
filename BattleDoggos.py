import sys
import pygame
import random
import time 

white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)


# Initialize pygame so it runs in the background and manages things
pygame.init()

#Load the image of the battlefield
background = pygame.image.load("img/BDField.png")
backgroundrect = background.get_rect()


#Creates a class for the two bases
class Base:
    def __init__(self, image, locx, locy): 
        self.health = 1000
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = locx
        self.rect.y = locy
"""
    def Damage(damage):

"""



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

    screen.blit(background, backgroundrect)
    screen.blit(Base1Image, Base1.rect)
    screen.blit(Base2Image, Base2.rect)

    pygame.display.flip()