# import sys, pygame, random, and time to use later
import sys
import pygame
import random
import time

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (1300, 560) )

def background(image):
    ''' Function fills background of screen with the indicated image'''
    screen.fill((0,0,0))
    screen.blit(image, (0,0))
    return

battle_BG = pygame.image.load("img/BDField3.jpg")
cloud_BG = pygame.image.load("img/AbilitiesBG2.png")
scene_cont = True

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
color_list = [black, white]

def text(text, size, color, x, y):
    ''' Function displays text on the screen with the specified attributes'''
    screen.blit(size.render(text, True, color), (x, y))
    return

big_font = pygame.font.SysFont("Comicsansms", 75)
medium_font = pygame.font.SysFont("Comicsansms", 50)
little_font = pygame.font.SysFont("Comicsansms", 25)


while scene_cont == True:
    background(battle_BG)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
        if keys[pygame.K_RETURN]:
            scene_cont = False
    
    pygame.display.flip()

pygame.time.wait(500)
scene_cont = True

while scene_cont == True:
    background(cloud_BG)
    keys = pygame.key.get_pressed()

    for n in color_list:
        text(f"Attack:", little_font, n, 598+2*color_list.index(n), 180)
        text(f"Defense:", little_font, n, 598+2*color_list.index(n), 280)
        text(f"Health:", little_font, n, 598+2*color_list.index(n), 380)
        



    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
        if keys[pygame.K_RETURN]:
            scene_cont = False
    
    pygame.display.flip()

pygame.time.wait(500)
scene_cont = True

while scene_cont == True:
    background(battle_BG)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
        if keys[pygame.K_RETURN]:
            scene_cont = False
    
    pygame.display.flip()

