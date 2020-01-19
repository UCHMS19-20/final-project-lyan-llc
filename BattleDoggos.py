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
Player1Image = pygame.image.load("img/Base1.png")
Player2Image = pygame.image.load("img/Base2.png")

# button images
dice = pygame.image.load("img/dice2.png")
start_battle = pygame.image.load("img/startbattle2.png")

# Create classes Player and Button
class Player:
    def __init__(self, name, image, x, y, attack, defense, health):
        '''Player is defined by its image, coordinates, and abilities'''
        self.name = name
        self.img = image
        self.rect = self.img.get_rect()
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
    
    
    # "flip" screen for this frame and then loop repeats
    pygame.display.flip()

# wait 1 second so it doesn't register the click for the next scene accidentally
pygame.time.wait(900)

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
    text("Press enter to continue.", little_font, 100, 380)
    # "flip" screen for this frame and then loop repeats
    pygame.display.flip()

# wait 1 second so it doesn't register the click for the next scene accidentally
pygame.time.wait(900)

# set value of scene_cont back to True to make the next screen
scene_cont = True

# ABILITIES SCREEN
for p in players:
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
    
        screen.blit(p.img, (100, 100))

        # display text
        text(f"Player {players.index(p)+1}", big_font, 400, 50)
        text(f"Click the dice to get your random stats!", medium_font, 200, 100)
        text(f"Attack: {p.attack}", little_font, 598, 180)
        text(f"Defense: {p.defense}", little_font, 598, 280)
        text(f"Health: {p.health}", little_font, 598, 380)

        # set the abilities to the values in the dice_values list
        p.attack, p.defense, p.health = dice_values

        # draw all three dice in the dice_list
        for d in dice_list:
            screen.blit(d.img, d.rect)

        # create the "Start Battle" button
        start_battle_button = Button(start_battle, 100, 100)

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
                        # Deactivate the button
                        dice_list[i].is_active = False
                if start_battle_button.has_mouse():
                    scene_cont = False

        # if the dice is in the process of rolling, display "Dice rolling..." and wait 3 seconds
        if dice_rolling == True:
            text("Dice rolling...", medium_font, 700, 100)
            pygame.display.flip()
            pygame.time.wait(1000)
            # set back to False so the program doesn't pause again until another die is rolled
            dice_rolling = False 

        if p == Player1 and (dice_list[0].is_active or dice_list[1].is_active or dice_list[2].is_active) == False:
            text(f"Player {players.index(p)+1} profile complete!", medium_font, 200, 200)
            text("Press enter to continue.", little_font, 200, 300)
            if keys[pygame.K_RETURN]:
                scene_cont = False

        # only runs code for "Start Battle" button if the sceen is for Player 2
        if p == Player2 and (dice_list[0].is_active or dice_list[1].is_active or dice_list[2].is_active) == False:
            # if any die is still active, the parentheses return True, which is negated and if statement will not run
             # if all dice have been clicked, the parenthese return False, which is negated and if statement runs
                # draw the "Start Battle!" buttton
            text(f"Player {players.index(p)+1} profile complete!", medium_font, 200, 200)
            screen.blit(start_battle_button.img, start_battle_button.rect)

        # "flip" screen for this frame and then loop repeats
        pygame.display.flip()
    
    pygame.time.wait(1000)
    scene_cont = True

Player1MaxHealth = Player1.health
Player2MaxHealth = Player2.health

# BATTLE SCREEN
while scene_cont == True:
    # Display battle background
    background(battle_BG)

    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    
    screen.blit(Player1Image, Player1.rect)
    screen.blit(Player2Image, Player2.rect)
    

    keys = pygame.key.get_pressed()
    
    #Movement
    #Determines the velocity for player 1

 
    #Have to put in the borders so that if the player tries to escape the screen they are bounced back
    if keys[pygame.K_LEFT]:
        velocity1 = -10
    elif keys[pygame.K_RIGHT]:
        velocity1 = 10
    else: 
        velocity1 = 0

    #Determines the velocity for player 2
    if keys[pygame.K_a]:
        velocity2 = -10
    elif keys[pygame.K_d]:
         velocity2 = 10
    else: 
        velocity2 = 0
        
    #Changes the players position according to the respective velocity
    Player1.rect.x += velocity1
    Player2.rect.x += velocity2


    #Health Bars
    pygame.draw.rect(screen, (0, 0, 0), (10, 475, Player1MaxHealth*90, 10))
    pygame.draw.rect(screen, (0, 255, 0), (10, 475, Player1.health*90, 15))     

    #Player 2 Health Bar
    pygame.draw.rect(screen, (0, 0, 0), (10, 525, Player2MaxHealth*90, 10))
    pygame.draw.rect(screen, (0, 255, 0), (10, 525, Player2.health*90, 15))


    # check if players are colliding
    if Player1.rect.colliderect(Player2.rect) == True:
       
        

         # damage to other player
    pygame.display.flip()

    
# END-OF-GAME SCREEN


#add in names?