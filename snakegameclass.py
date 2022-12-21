'''
SNAKE GAME CLASS
BY: ANDREW AND DANIEL
'''
'''
Notes:
- 20 * 20 pixels per snake unit
- 20 * 20 pixels per Consumable
- 40 * 40 units
Classes:
- 2 Classes - Snake and Consumable
Snake:
Variables -->
- Initialize
- Set Image
- Set Width 
- Set Height
- Set Dimensions
- Set X
- Set Y
- Set Location
- Get Image
- Get Width 
- Get Height
- Get Dimensions
- Get X
- Get Y
- Get Location
- Add length
- Move 
- Output

Consumable:
- Initialize
- Set Width 
- Set Height
- Set Dimensions
- Set Random X
- Set Random Y
- Get Width 
- Get Height
- Get Dimensions
- Get X
- Get Y
- Get Location
- Set Random Location (Between Boundaries) - Not on snake
'''
import pygame
import random

class Snake:

    __imgSnakeOriginal = None
    __imgSnake = None
    __width = 1
    __height = 1
    __xpos = 0
    __ypos = 0
    __listBody = [None]

    def __init__(self):

        self.__imgSnakeOriginal = pygame.image.load("Images/SnakeBodyUnit.png")
        self.__width = self.__imgSnakeOriginal.get_width()
        self.__height = self.__imgSnakeOriginal.get_height()
        self.__imgSnake = self.__imgSnakeOriginal
        self.__xpos = 0
        self.__ypos = 0

    def output(self, surface):
        surface.blit(self.__imgSnake,(self.__xpos, self.__ypos))
    
    def move(self, pixels=1, direction="MOVEDOWN"):
        if direction == "MOVEUP":
            self.__ypos = self.__ypos - pixels
        
        elif direction == "MOVELEFT":
            self.__xpos = self.__xpos - pixels

        elif direction == "MOVERIGHT":
            self.__xpos = self.__xpos + pixels
        
        elif direction == "MOVEDOWN": 
            self.__ypos = self.__ypos + pixels

        else:
            self.__xpos = self.__xpos + 0
            self.__ypos = self.__ypos + 0 

    def set_Image(self, img):
        self.__imgSnakeOriginal = img
        self.__width = self.__imgSnakeOriginal.get_width()
        self.__height = self.__imgSnakeOriginal.get_height()

    def set_Width(self, w=1):
        self.__width = w
        self.__imgSnake = pygame.transform.smoothscale(self.__imgSnakeOriginal,
        (self.__width, self.__height))

    def set_Height(self, h=1):
        self.__height = h
        self.__imgSnake = pygame.transform.smoothscale(self.__imgSnakeOriginal,
        (self.__width, self.__height))

    def set_Dimensions(self, w=1, h=1):
        self.__width = w
        self.__height = h
        self.__imgSnake = pygame.transform.smoothscale(self.__imgSnakeOriginal,
        (self.__width, self.__height))

    def set_Xpos(self, x=0):
        self.__xpos = x

    def set_Ypos(self, y=0):
        self.__ypos = y

    def set_Location(self, x=0, y=0):
        self.__xpos = x
        self.__ypos = y

    # Void
    def get_Image(self):
        return self.__imgSnake

    def get_Width(self):
        return self.__width

    def get_Height(self):
        return self.__height

    def get_Dimensions(self):
        return (self.__width, self.__height)

    def get_Xpos(self):
        return self.__xpos

    def get_Ypos(self):
        return self.__ypos

    def get_Location(self):
        return (self.__xpos, self.__ypos)


class Consumable:
    '''
    - Copy variables into init and add self. to the beginning of each
    '''
    __imgFoodOriginal = None
    __imgFood = None
    __width = 1
    __height = 1
    __xRandom = 0
    __yRandom = 0

    def __init__(self):
        self.__imgFoodOriginal = pygame.image.load("Images/ConsumableSnakeGame.png")
        self.__imgFood = self.__imgFoodOriginal
        self.__width = self.__imgFoodOriginal.get_width()
        self.__height = self.__imgFoodOriginal.get_height()
        self.__xRandom = 0
        self.__yRandom = 0

    def output(self, surface):
        surface.blit(self.__imgFood, (self.__xRandom, self.__yRandom))

    def set_Image(self, img):
        self.__imgFoodOriginal = img
        self.__width = self.__imgFoodOriginal.get_width()
        self.__height = self.__imgFoodOriginal.get_height()

    def set_Width(self, w=1):
        self.__width = w
        self.__imgFood = pygame.transform.smoothscale(self.__imgFoodOriginal,(self.__width, self.__height))

    def set_Height(self, h=1):
        self.__height = h
        self.__imgFood = pygame.transform.smoothscale(self.__imgFoodOriginal,(self.__width, self.__height))

    def set_Dimensions(self, w=1, h=1):
        self.__width = w
        self.__height = h
        self.__imgFood = pygame.transform.smoothscale(self.__imgFoodOriginal,(self.__width, self.__height))
        
    def set_Xrandom(self, max=100):
        self.__xRandom = random.randrange(0, max, 20)

    def set_Yrandom(self, max=100):
        self.__yRandom = random.randrange(0, max, 20)

    def set_locationRandom(self, maxX, maxY):
        self.__xRandom = random.randrange(0, maxX, 20)
        self.__yRandom = random.randrange(0, maxY, 20)
        
    # Getters
    def get_Image(self):
        return self.__imgFood

    def get_Width(self):
        return self.__width

    def get_Height(self):
        return self.__height

    def get_Dimensions(self):
        return (self.__width, self.__height)

    def get_Xrandom(self):
        return self.__xRandom

    def get_Yrandom(self):
        return self.__yRandom

    def get_locationRandom(self, x=0, y=0):
        return (self.__xRandom, self.__yRandom)
