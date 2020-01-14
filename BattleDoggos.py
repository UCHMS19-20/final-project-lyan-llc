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
black = pygame.Color(0, 0, 0)

# Create font objects
big_font = pygame.font.SysFont("Comicsansms", 75)
medium_font = pygame.font.SysFont("Comicsansms", 50)
little_font = pygame.font.SysFont("Comicsansms", 25)
 
# Create text objects
player1_text = big_font.render("PLAYER 1", True, white)
click_text = little_font.render("Click the dice to get your stats!", True, white)

# load images
dice = pygame.image.load("img/red_dice.gif")
abilities_BG = pygame.image.load("img/AbilitiesBG2.png")

# Create button class
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

# create list of 3 buttons that look like the red dice
dice_list = []
for y in range(3):
    dice_list.append(Button(dice, 525, y * 200 + 160))

# create blank list of 3 aspects of the dice (later to be abilities)
dice_values = [0,0,0]

#set initial value of if the dice is being rolled to False
dice_rolling = False

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    
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
    screen.blit(player1_text, (800, 0))
    screen.blit(click_text, (800, 100))
    
    # set the abilities to the values in the dice_values list
    attack, defense, health = dice_values
   
    screen.blit((little_font.render(f"Attack: {attack}", True, black)), (598, 180))
    screen.blit((little_font.render(f"Defense: {defense}", True, black)), (598, 380))
    screen.blit((little_font.render(f"Health: {health}", True, black)), (598, 580))
   
    screen.blit((little_font.render(f"Attack: {attack}", True, white)), (600, 180))
    screen.blit((little_font.render(f"Defense: {defense}", True, white)), (600, 380))
    screen.blit((little_font.render(f"Health: {health}", True, white)), (600, 580))
    
    
    for d in dice_list:
            screen.blit(d.img, d.rect)
   
    # get position of mouse
    mouse_pos = pygame.mouse.get_pos()
    
    
    for event in pygame.event.get(): 
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
      
        # check if mouse is pressing down on a button
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(0, len(dice_list)):
                if dice_list[i-2].has_mouse() and dice_list[i].is_active:
                    dice_values[i-2] = dice_list[i].roll_die()
                    dice_rolling = True
                    print(f"Attack = {dice_values[0]}")
                    print(f"Defense = {dice_values[1]}")
                    print(f"Health = {dice_values[2]}")
                    print("________")
                    dice_list[i].is_active = False
    
    
    pygame.display.flip()