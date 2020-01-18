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
battle_BG = pygame.image.load("img/BDField3.jpg")
cloud_BG = pygame.image.load("img/AbilitiesBG2.png")

# player images
Player1Image = pygame.image.load("img/Player1Image.png")
Player2Image = pygame.image.load("img/Player2Image.png")

# button images
dice = pygame.image.load("img/dice2.png")
start_battle_button = pygame.image.load("img/startbattle.png")

# Create classes Player and Button
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

def text(text, size, x, y):
    ''' Function displays text on the screen with the specified attributes, with a black shadow'''
    for n in color_list:
        screen.blit(size.render(text, True, n), (x+3*color_list.index(n), y))
    return

# for n in color_list:
#             text(f"Attack: {p.attack}", little_font, n, 598+2*color_list.index(n), 180)
#             text(f"Defense: {p.defense}", little_font, n, 598+2*color_list.index(n), 280)
#             text(f"Health: {p.health}", little_font, n, 598+2*color_list.index(n), 380)

# set the continuation of the scene to True
scene_cont = True


# TITLE SCREEN
while scene_cont == True:
    # display cloud background
    background(cloud_BG)

    # get state of all the keys, every frame
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
        # if return is pressed, break loop
        if keys[pygame.K_RETURN]:
                scene_cont = False

    # display title screen text
    text("Welcome to...", medium_font, 100, 100)
    text("BATTLE DOGGOS", big_font, 100, 180)
    text("Press enter to continue.", little_font, 100, 280)
    
    
    # "flip" screen for this frame and then While True loop repeats
    pygame.display.flip()

# wait 1 second so it doesn't register the click for the next scene accidentally
pygame.time.wait(1000)

#set scene_cont back to True so the next scene will run
scene_cont = True

# RULES SCREEN
while scene_cont == True:
    # display cloud background
    background(cloud_BG)

    # get state of all the keys, every frame
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
         # if return is pressed, break loop
        if keys[pygame.K_RETURN]:
            scene_cont = False
    
    # display rules
    text("Rules", medium_font, 100, 180)
    text("Rules rules rules rules rules rules rules rules rules", medium_font, 100, 280)
    
    # "flip" screen for this frame and then While True loop repeats
    pygame.display.flip()

# wait 1 second so it doesn't register the click for the next scene accidentally
pygame.time.wait(1000)

# set value of scene_cont back to True to make the next screen
scene_cont = True

# ABILITIES SCREEN
for p in players:
    # # set value of scene_cont back to True to make the next screen
    # scene_cont = True
    # # wait 1 second so it doesn't register the click for the next scene accidentally
    # pygame.time.wait(1000)

    # Create list of 3 buttons that look like the red dice (using Button class)
    dice_list = []
    for y in range(3):
        dice_list.append(Button(dice, 525, y * 100 + 160))

    for event in pygame.event.get():
                # Check to see if the current event is a QUIT event
                if event.type == pygame.QUIT:
                    # If so, exit the program
                    sys.exit()
    
    # Create blank list of 3 aspects of the dice (later to be abilities)
    dice_values = [0,0,0]
    
    # start scene loop (breaks when scene ends)
    while scene_cont == True:
        background(cloud_BG)
        # get state of all the keys, every frame
        keys = pygame.key.get_pressed()
    
        
        # display text
        text(f"{p.name}", big_font, 400, 50)
        text(f"Attack: {p.attack}", little_font, 598, 180)
        text(f"Defense: {p.defense}", little_font, 598, 280)
        text(f"Health: {p.health}", little_font, 598, 380)

        # set the abilities to the values in the dice_values list
        p.attack, p.defense, p.health = dice_values

        # draw all three dice in the dice_list
        for d in dice_list:
            screen.blit(d.img, d.rect)

        # create the "Start Battle" button
        start_battle = Button(pygame.image.load("img/BDField.png"), 100, 100)

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

        # if the dice is in the process of rolling, display "Dice rolling..." and wait 3 seconds
        if dice_rolling == True:
            text("Dice rolling...", medium_font, 700, 100)
            pygame.display.flip()
            pygame.time.wait(2000)
            # set back to False so the program doesn't pause again until another die is rolled
            dice_rolling = False 

                # check if the mouse is on the start button (while it presses down)
                # if start_battle.has_mouse():
                #     pygame.time.wait(1000)
                #     scene_cont = False
        if p == Player1:
            if (dice_list[0].is_active or dice_list[1].is_active or dice_list[2].is_active) == False:
                scene_cont = False
        # only runs code for "Start Battle" button if the sceen is for Player 2
        if p == Player2:
            # if any die is still active, the parentheses return True, which is negated and if statement will not run
             # if all dice have been clicked, the parenthese return False, which is negated and if statement runs
            if (dice_list[0].is_active or dice_list[1].is_active or dice_list[2].is_active) == False:
                # draw the "Start Battle!" buttton
                screen.blit(start_battle.img, start_battle.rect)

    
        # "flip" screen for this frame and then While True loop repeats
        pygame.display.flip()

    scene_cont = True
    pygame.time.wait(1000)

# BATTLE SCREEN
while True:
    # Display battle background
    background(battle_BG)

    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    
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