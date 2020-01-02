# import sys, pygame, random, and time to use later
import sys
import pygame
import random
import time

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (1350, 650) )

# Create color(s)
white = pygame.Color(255, 255, 255)
purple = pygame.Color(110, 27, 190)

# Create font object
big_font = pygame.font.SysFont("Comicsansms", 75)
medium_font = pygame.font.SysFont("Comicsansms", 50)
little_font = pygame.font.SysFont("Comicsansms", 25)

# Create text objects
player1_text = big_font.render("PLAYER 1", True, white)
click_text = little_font.render("Click the dice to get your stats!", True, white)

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    screen.fill(purple)
    screen.blit(player1_text, (800, 0))
    screen.blit(click_text, (800, 100))
    pygame.display.flip()

    
    
    
    
    
    
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()