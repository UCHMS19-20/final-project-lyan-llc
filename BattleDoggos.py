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
huge_font = pygame.font.Font("Good Morning.ttf", 70)
big_font = pygame.font.Font("Doctor Soos Bold 2.1.ttf", 75)
medium_font = pygame.font.Font("Doctor Soos Bold 2.1.ttf", 45)
little_font = pygame.font.Font("Doctor Soos Bold 2.1.ttf", 25)

# LOAD ALL IMAGES
# background images and create rects
battle_BG = pygame.image.load("img/BDField3.jpg")
cloud_BG = pygame.image.load("img/CloudBG.jpg")

# player images
Player1Image = pygame.image.load("img/Heidi.png")
Player2Image = pygame.image.load("img/Remi.png")

# button images
dice = pygame.image.load("img/dice2.png")
start_battle = pygame.image.load("img/startbattle3.png")

# Create classes Player and Button
class Player:
    def __init__(self, name, image, x, y, attack, defense, health, velocity):
        '''Player is defined by its image, coordinates, and abilities'''
        self.name = name
        self.img = image
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.attack = attack
        self.defense = defense
        self.health = health
        self.velocity = velocity

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
Player1 = Player("Player 1", Player1Image, 300, 100, 0, 0, 0, 0)
Player2 = Player("Player 2", Player2Image, 700, 100, 0, 0, 0, 0)
# create a list of players
players = [Player1, Player2]

# set initial value of if the dice is being rolled to False
dice_rolling = False

def background(image):
    ''' Function fills background of screen with the indicated image'''
    screen.fill((0,0,0))
    screen.blit(image, (0,0))
    return

def text(text, size, offset, x, y):
    ''' Function displays text on the screen with the specified attributes, with a black shadow'''
    for n in color_list:
        screen.blit(size.render(text, True, n), (x+offset*color_list.index(n), y))    
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
    text("Welcome to...", medium_font, 4, 500, 100)
    text("BATTLE DOGGOS", huge_font, 6, 200, 200)
    text("Press enter to continue.", little_font, 2, 500, 400)
    
    
    # "flip" screen for this frame and then loop repeats
    pygame.display.flip()

# wait 1 second so it doesn't register the click for the next scene accidentally
pygame.time.wait(900)

#set scene_cont back to True so the next scene will run
scene_cont = True

# RULES SCREEN 1
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
    text("RULES", big_font, 5, 50, 50)
    rules_text_1 = [
        "This is a two-player game. You will both roll virtual dice to get random",
        "levels of Attack, Defense, and Health on a scale of 1-6. Then, the battle",
        "begins and you attack each other!",
        "",
        "Player 1 moves back and forth using the A and D keys, and attacks with",
        "the Left Shift key. Player 2 uses the left and right arrows,",
        "and attacks with the enter key."
    ] 
    # display text in lines that fit on the screen and are evenly spaced
    for n in rules_text_1:
        text(n, medium_font, 4, 50, rules_text_1.index(n)*40+130)
    
    text("Press enter to continue.", little_font, 2, 50, 450)
    # "flip" screen for this frame and then loop repeats
    pygame.display.flip()

# wait 1 second so it doesn't register the click for the next scene accidentally
pygame.time.wait(900)

# set value of scene_cont back to True to make the next scene
scene_cont = True

# RULES SCREEN 2
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
    
    # display second set of rules
    text("RULES", big_font, 5, 50, 50)
    rules_text_2 = [
        "You must be colliding with each other to attack. Attacking decreases",
        "your opponent's health. If their defense is strong, your attack",
        "becomes weaker.",
        "",
        "The health bar at the top will show how much health you have left. The",
        "first to 0 health loses. Good luck!"
    ]
    # display text in lines that fit on the screen and are evenly spaced
    for n in rules_text_2:
        text(n, medium_font, 4, 50, rules_text_2.index(n)*40+130)
    
    text("Press enter to continue.", little_font, 2, 50, 450)
    
    pygame.display.flip()
    
# wait 1 second so it doesn't register the click for the next scene accidentally
pygame.time.wait(900)

# set value of scene_cont back to True to make the next scene
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
        text(f"{p.name}", big_font, 5, 75, 40)
        text(f"Click the dice to get your random stats!", medium_font, 4, 75, 100)
        text(f"Attack: {p.attack}", little_font, 2, 600, 180)
        text(f"Defense: {p.defense}", little_font, 2, 600, 280)
        text(f"Health: {p.health}", little_font, 2, 600, 380)

        # set the abilities to the values in the dice_values list
        p.attack, p.defense, p.health = dice_values

        # draw all three dice in the dice_list
        for d in dice_list:
            screen.blit(d.img, d.rect)

        # create the "Start Battle" button
        start_battle_button = Button(start_battle, 1010, 400)

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
                        # set dice_rolling to True so in the next frame, the program will pause and display "Dice Rolling..."
                        dice_rolling = True
                        # Deactivate the button
                        dice_list[i].is_active = False
                        print(dice_values)
                if start_battle_button.has_mouse():
                    scene_cont = False
            
        # if the dice is in the process of rolling, display "Dice rolling..." and wait 3 seconds
        if dice_rolling == True:
            text("Dice rolling...", medium_font, 4, 1000, 130)
            pygame.display.flip()
            pygame.time.wait(1000)
            # set back to False so the program doesn't pause again until another die is rolled
            dice_rolling = False 

        if p == Player1 and (dice_list[0].is_active or dice_list[1].is_active or dice_list[2].is_active) == False:
            text(f"Player {players.index(p)+1} profile complete!", medium_font, 4, 850, 350)
            text("Press enter to continue.", little_font, 2, 1075, 400)
            if keys[pygame.K_RETURN]:
                scene_cont = False

        # only runs code for "Start Battle" button if the screen is for Player 2
        if p == Player2 and (dice_list[0].is_active or dice_list[1].is_active or dice_list[2].is_active) == False:
             # if all dice have been clicked, draw the "Start Battle!" buttton
            text(f"Player {players.index(p)+1} profile complete!", medium_font, 4, 850, 350)
            screen.blit(start_battle_button.img, start_battle_button.rect)

        # "flip" screen for this frame and then loop repeats
        pygame.display.flip()
    
    pygame.time.wait(900)
    scene_cont = True

def damage(attacker, defender):
    '''Calculate damage inflicted based on defense and attack stats of each player'''
    damage = int((attacker.attack + 6) * (1- (defender.defense / 10)))
    defender.health = defender.health - damage
    return defender.health

# scale up how many health points there are for the battle screen
for p in players:
    p.health = p.health * 20

# BATTLE SCREEN
while scene_cont == True:
    # Display battle background
    background(battle_BG)

    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    # Draw both players 
    screen.blit(Player1.img, Player1.rect)
    screen.blit(Player2.img, Player2.rect)
    
    # get state of all the keys, every frame
    keys = pygame.key.get_pressed()
    
    # MOVEMENT
   
    # determine the velocity for player 1
    # if the Player1 presses left, velocity is set to 10 (left)
    if keys[pygame.K_a]:
        Player1.velocity = -10
    # if the Player1 presses right, velocity is set to 10 (right)
    elif keys[pygame.K_d]:
        Player1.velocity = 10
    # otherwise, the velocity is set to 0
    else: 
        Player1.velocity = 0

    # determine the velocity for Player2
    # If the Player2 presses A, velocity is set to 10 (left)
    if keys[pygame.K_LEFT]:
        Player2.velocity = -10
    # If the Player2 presses D, velocity is set to 10 (right)
    elif keys[pygame.K_RIGHT]:
        Player2.velocity = 10
    # Otherwise, the velocity is set to 0
    else: 
        Player2.velocity = 0
    
    # Change player positions based on velocities and prevent players from leaving screen
    for p in players:
        if p.rect.x > 1100:
            p.velocity = -0.5
        if p.rect.x < 0:
            p.velocity = 0.5
        p.rect.x += p.velocity

    # HEALTH BARSy
    # Draws Player 1's name over their health bar
    text("Player 1", little_font, 2, 15, 435)
    # Draws a a green bar that decreases in width when the player is damaged
    pygame.draw.rect(screen, (0, 255, 0), (10, 475, Player1.health*10, 15))     

    # Draws Player 2's name over their health bar
    text("Player 2", little_font, 2, 15, 487)
    # Draws a green bar that decreases in width when the player is damaged
    pygame.draw.rect(screen, (0, 255, 0), (10, 525, Player2.health*10, 15))

    # check if players are colliding
    if Player1.rect.colliderect(Player2.rect) == True:
         # if Player 1 presses left shift, inflict damage on Player 2
        if keys[pygame.K_LSHIFT]:
            pygame.time.wait(500)
            damage(Player1, Player2)
        # if Player 2 presses Return/Enter, dddinflict damage on Player 1
        if keys[pygame.K_RETURN]:
            pygame.time.wait(500)
            damage(Player2, Player1)
    for p in players:
        if p.health <= 0:
            text(f"{players[players.index(p)-1].name} wins!", big_font, 5, 470, 100)
            pygame.display.flip()
            pygame.time.wait(3000)
            scene_cont = False

    pygame.display.flip()
    
#set scene_cont back to true to move to last scene
scene_cont = True

# END-OF-GAME SCREEN
while scene_cont == True:
    background(cloud_BG)
    text("The End!", huge_font, 6, 400, 200)
    pygame.display.flip()
    pygame.time.wait(5000)
    sys.exit()