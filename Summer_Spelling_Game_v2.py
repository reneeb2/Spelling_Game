import pygame
import random
import os
import sys


# Set variables for colors
vGray = (100, 100, 100)
vNavyBlue = (60, 60, 100)
vWhite = (255, 255, 255)
vRed = (255, 0, 0)
vGreen = (0, 255, 0)
vBlue = (0, 0, 255)
vYellow = (255, 255, 0)
vOrange = (255, 128, 0)
vPurple = (255, 0, 255)
vCyan = (0, 255, 255)
vBlack = (0, 0, 0)
vLightBlue = (204, 229, 255)

# Set the screen size
vHeight = 600
vWidth = 1000
# initiate pygame
pygame.init()
# Set variables for the screen display
vScreen = pygame.display.set_mode([vWidth,vHeight])
vBGColor = vLightBlue
vTitleFont = pygame.font.SysFont('comicsansms', 75)
vTitle = 'Summer Spelling Game'
pygame.display.set_caption(vTitle)

# Set variables for font and size
vFont = pygame.font.SysFont('comicsansms', 50)
vDirectFont = pygame.font.SysFont('comicsansms', 50)

# My attempt to build a function that would allow the user to decide on the level
# def get_level():
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_1:
#                 vLevel = 1
#             elif event.key == pygame.K_2:
#                 vLevel = 2
#             elif event.key == pygame.K_3:
#                 vLevel = 3
#             elif event.key == pygame.K_4:
#                 vLevel = 4
#
#     return vLevel

# Hard coded the level to start with. I was unable to get the user input for the level at this time
vLevel = '1'

# empty list for words
vWordList = []
# Path to the files with pictures
vDirectory = os.walk(vLevel)

# Loop through level file to get names of picutres/words in that file
for root, dir, files in vDirectory:
    for file in files:
        vWordList.append(file)

# Gets a random word from the list
vRandomWord = random.choice(vWordList)
# Removes the last 4 characters from the word .png
vWord = vRandomWord[:-4]
# Loads the image that goes with the word
vWordPic = pygame.image.load(vRandomWord)
# Changes the scale of the picture so that it fits in the screen
vWordPic = pygame.transform.scale(vWordPic, (150, 200))
# Gets the number of letters in the word
VNumber = len(vWord)
# print(vRandomWord)
# print(vWord)

# Empty letter list for later use
vLetter =[]

# This function provides how the text objects, like title, will be formated
def text_objects(text, font, fontcolor):
    vSurf = vFont.render(text, True, fontcolor)
    return vSurf, vSurf.get_rect()

# Produces the title
def title(text):
    vTitle_Surf, vTitle_Rect = text_objects(vTitle, vTitleFont, vPurple)
    vTitle_Rect.center = (500, 50)
    vScreen.blit(vTitle_Surf, vTitle_Rect)
    # pygame.display.update()

# Produces the level number so the user can see that
def level():
    vLevel_Surf, vLevel_Rect = text_objects('Level '+ vLevel + '!', vFont, vPurple)
    vLevel_Rect.center = (500, 125)
    vScreen.blit(vLevel_Surf, vLevel_Rect)

# Provides the simple instructions for the user
def directions_line_one():
    vDirect_Surf, vDirect_Rect = text_objects('Spell the word that goes with the picture', vDirectFont, vGreen)
    vDirect_Rect.center = (500, 175)
    vScreen.blit(vDirect_Surf, vDirect_Rect)

# The screen that should show when the player spells the word correctly
def display_congrats():
    vYay_Surf, vYay_Rect = text_objects('Yay! You are correct!', vDirectFont, vBlue)
    vYay_Rect.center = (450, 500)
    vScreen.blit(vYay_Surf, vYay_Rect)

# The screen that should show when the player spells the word incorrectly and has not more turns left
def display_wrong():
    vWrong_Surf, vWrong_Rect = text_objects('Oh no! Wrong answer!', vDirectFont, vBlue)
    vWrong_Rect.center = (450, 500)
    vScreen.blit(vWrong_Surf, vWrong_Rect)



# The loop to play the game
while True:

    key = pygame.key.get_pressed()

    # fills the screen with the background color
    vScreen.fill(vBGColor)

    # calls forward the title function
    title(vTitle)
    # calls forward the level function
    level()
    # calls forward the directions function
    directions_line_one()

    # shows the scaled picture for the word on the screen
    vScreen.blit(vWordPic,(400, 250))

    # Provides lines for each letter in the word and where they sit on the screen
    vWordLines = ' _ ' * len(vWord)
    vLines_Surf, vLines_Rect = text_objects(vWordLines, vDirectFont, vBlack)
    vLines_Rect.center = (450, 500)
    vScreen.blit(vLines_Surf, vLines_Rect)

    # This is my attempt to get the letters to show on the screen and determine if the word was spelled correctly
    for event in pygame.event.get():
        for vLetter in range(5):
            if event.type == pygame.KEYDOWN:
                vLetter = pygame.key.name(event.key)
                if vLetter in vWord:
                    vLetter =+ event.key
                if vLetter == vWord:
                    break
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.sys.exit()


        if vLetter == vWord:
            vScreen.fill(vBGColor)
            title(vTitle)
            level()
            display_congrats()
            # pygame.display.flip()
        else:
            vScreen.fill(vBGColor)
            title(vTitle)
            level()
            display_wrong()
            # pygame.display.flip()


    # for event in pygame.event.get():

    # print(vWord)
    pygame.display.update()

