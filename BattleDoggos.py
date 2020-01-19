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
        #for later in the game when the player has no health, the character disappears and is deleted
        self.visible = True

    #Make sure that the defense is the enemy player defense. Health is the enemy Health. 
    #this is activated when the player attacks (Right clicks) while colliding with the other player
    #still need to put the player collision code it
    """
    def damage(self, health, defense, attack):
        #If colliding and left click is pressed:
        if self.health > 0:
            damage = attack - defense
            health =- damage
        else: self.visible = False
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



# Create font objects
big_font = pygame.font.SysFont("Comicsansms", 75)
medium_font = pygame.font.SysFont("Comicsansms", 50)
little_font = pygame.font.SysFont("Comicsansms", 25)
 
# Create text objects
player1_text = big_font.render("PLAYER 1", True, white)
click_text = little_font.render("Click the dice to get your stats!", True, white)

# load images
dice = pygame.image.load("img/Base1.png")
abilities_BG = pygame.image.load("img/Base1.png")

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
    keys = pygame.key.get_pressed()
    
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
        #Determines the velocity for player 1


        #Have to put in the borders so that if the player tries to escape the screen they are bounced back
        if keys[pygame.K_LEFT]:
            velocity1 = -10
        else: 
            velocity1 = 0
        if keys[pygame.K_RIGHT]:
            velocity1 = 10
        else: 
            velocity1 = 0

        #Determines the velocity for player 2
        if keys[pygame.K_a]:
            velocity2 = -10
        else: 
            velocity2 = 0
        if keys[pygame.K_d]:
            velocity2 = 10
        else: 
            velocity2 = 0
        
    #Changes the players position according to the respective velocity
    Player1.rect.x += velocity1
    Player2.rect.x += velocity2
    

    #Draw the background, and bases in certain positions
    screen.blit(background, backgroundrect)
    screen.blit(Base1Image, Base1.rect)
    screen.blit(Base2Image, Base2.rect)
    

    #Player collision Code



    #Damage to other player



    #Heal?


    #Health Bars


    #Health Bar Player1
    #draws on the window, color, (x, y), width, height

    #Possible Problem: When damaged, Player 2's health bar decreases the wrong way(right to left instead of left to right)
    #Possible solution: Multiply the Player2 Health by -60, and create a different damage function in the player class where when player 2 is damaged, 
    #health is added to decrease the bar
    
    pygame.draw.rect(screen, (0, 0, 0), (10, 30, Player1.health*90, 10))
    pygame.draw.rect(screen, (0, 255, 0), (10, 30, Player1.health*90, 15))         
 

    #Player 2 Health Bar
    pygame.draw.rect(screen, (0, 0, 0), (750, 30, Player2.health*90, 10))
    pygame.draw.rect(screen, (0, 255, 0), (750, 30, Player2.health*90, 15))
    
    pygame.display.flip()


 








    












