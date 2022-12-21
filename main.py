'''
SNAKE GAME --> MAIN PROGRAM
BY: ANDREW AND DANIEL
'''
import os
import pygame
from tkinter import Tk
from tkinter import messagebox
from snakegameclass import Snake
from snakegameclass import Consumable
from pygame.locals import *



# Withdraw a new window from tkinter
root = Tk()
root.withdraw()

# Centering the screen
os.environ['SDL_VIREO_CENTERED'] = "1"

# Initialize all modules required for pygame; reset all objects
pygame.init()

# Set the caption to Snake Game to display on the top left of the surface window
pygame.display.set_caption("Snake Game")

# Set the visibility of the mouse on the program surface to True
pygame.mouse.set_visible(True)

# Set a clock
clock = pygame.time.Clock()

# Formulate a surface window whose dimensions are 900 x 900
surfaceWindow = pygame.display.set_mode((800, 800))

# Make the background color white according to RGB values
surfaceWindow.fill([0, 0, 0])


# Consumable
consumableObject = Consumable()

int_length = 1

# Variable Declarations and class usage
# Set the dimensions of the snake
scoreFont = pygame.font.SysFont("Bahnschrift", 28, True, False)
scoreOutput = scoreFont.render("{:s}{:d}".format("SCORE: ", int_length),
    True, pygame.Color("#FFFF00"))

# Initializing all variables and class functions are to be used
consumableObject.set_Width(20)
consumableObject.set_Height(20)
consumableObject.set_Xrandom(surfaceWindow.get_width() - consumableObject.get_Width())
consumableObject.set_Yrandom(surfaceWindow.get_height() - consumableObject.get_Height())
listIndex = 0
snakeBody = [None]
snakeBodyCollide = [None]
snakeBody[listIndex] = Snake()
snakeBody[listIndex].set_Xpos(surfaceWindow.get_width() // 2)
snakeBody[listIndex].set_Ypos(surfaceWindow.get_height() // 2)
snakeBody[listIndex].set_Width(20)
snakeBody[listIndex].set_Height(20)
snakeBodyCollide[listIndex] = Snake()
snakeBodyCollide[listIndex].set_Xpos(surfaceWindow.get_width() // 2)
snakeBodyCollide[listIndex].set_Ypos(surfaceWindow.get_height() // 2)
snakeBodyCollide[listIndex].set_Width(20)
snakeBodyCollide[listIndex].set_Height(20)
pygame.time.set_timer(pygame.USEREVENT, 120)
programContinuity = True
snakeDirection = "STOP"
bodyDirection = "STOP"
previousXposition = [None] 
previousYposition = [None] 
int_length = 1

while programContinuity == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programContinuity = False
        if event.type == pygame.USEREVENT:
            # Check for a collision with the boundaries of the game and then move
            
            if snakeBody[0].get_Xpos() < 0 or snakeBody[0].get_Ypos() < 0 or snakeBody[0].get_Xpos() > surfaceWindow.get_width() - snakeBody[0].get_Width() or snakeBody[0].get_Ypos() > surfaceWindow.get_height() - snakeBody[0].get_Height():
                pygame.time.set_timer(pygame.USEREVENT, 0)
                messagebox.showinfo("Snake Game", "GAMEOVER!\nScore: " + str(int_length))
                potentialTermination = messagebox.askquestion("Snake Game", "Would you like to play again?")
                if potentialTermination == "no":
                    programContinuity = False
                elif potentialTermination == "yes":
                    consumableObject.set_Width(20)
                    consumableObject.set_Height(20)
                    consumableObject.set_Xrandom(surfaceWindow.get_width() - consumableObject.get_Width())
                    consumableObject.set_Yrandom(surfaceWindow.get_height() - consumableObject.get_Height())
                    listIndex = 0
                    snakeBody = [None]
                    snakeBodyCollide = [None]
                    snakeBody[listIndex] = Snake()
                    snakeBody[listIndex].set_Xpos(surfaceWindow.get_width() // 2)
                    snakeBody[listIndex].set_Ypos(surfaceWindow.get_height() // 2)
                    snakeBody[listIndex].set_Width(20)
                    snakeBody[listIndex].set_Height(20)
                    snakeBodyCollide[listIndex] = Snake()
                    snakeBodyCollide[listIndex].set_Xpos(surfaceWindow.get_width() // 2)
                    snakeBodyCollide[listIndex].set_Ypos(surfaceWindow.get_height() // 2)
                    snakeBodyCollide[listIndex].set_Width(20)
                    snakeBodyCollide[listIndex].set_Height(20)
                    pygame.time.set_timer(pygame.USEREVENT, 125)
                    programContinuity = True
                    snakeDirection = "STOP"
                    bodyDirection = "STOP"
                    previousXposition = [None] 
                    previousYposition = [None] 
                    int_length = 1
            else:
                for index, unit in enumerate(snakeBody):
                    if index == 0:
                        previousXposition[0] = unit.get_Xpos()
                        previousYposition[0] = unit.get_Ypos()
                        unit.move(pixels=20, direction=snakeDirection)
                    else:
                        previousXposition.append(None)
                        previousYposition.append(None)
                        previousXposition[index] = unit.get_Xpos()
                        previousYposition[index] = unit.get_Ypos()
                        unit.set_Xpos(previousXposition[index - 1])
                        unit.set_Ypos(previousYposition[index - 1])

            if snakeBody[0].get_Xpos() == consumableObject.get_Xrandom():
                if snakeBody[0].get_Ypos() == consumableObject.get_Yrandom():
                    int_length = int_length + 4
                    for index, unit in enumerate(snakeBody):
                        while snakeBody[index].get_Xpos() == consumableObject.get_Xrandom() and snakeBody[index].get_Ypos() == consumableObject.get_Yrandom():
                            consumableObject.set_Xrandom(surfaceWindow.get_width() - consumableObject.get_Width())
                            consumableObject.set_Yrandom(surfaceWindow.get_height() - consumableObject.get_Height())

                    for counter in range(4):
                        listIndex = listIndex + 1
                        snakeBody.append(Snake())
                        snakeBodyCollide.append(Snake())
                        snakeBody[listIndex].set_Width(20)
                        snakeBody[listIndex].set_Height(20)
                        snakeBodyCollide[listIndex].set_Width(20)
                        snakeBodyCollide[listIndex].set_Height(20)
                        snakeBody[listIndex].set_Xpos(surfaceWindow.get_width() + 100)
                        snakeBody[listIndex].set_Ypos(surfaceWindow.get_height() + 100)
                        snakeBodyCollide[listIndex].set_Xpos(surfaceWindow.get_width() + 100)
                        snakeBodyCollide[listIndex].set_Ypos(surfaceWindow.get_height() + 100)
                        
                        
            for index, unit in enumerate(snakeBodyCollide):
                unit.set_Xpos(snakeBody[index].get_Xpos())
                unit.set_Ypos(snakeBody[index].get_Ypos())

            for index, unit in enumerate(snakeBodyCollide):
                if index != 0:
                    if snakeBody[0].get_Xpos() == unit.get_Xpos():
                        if snakeBody[0].get_Ypos() == unit.get_Ypos():
                            pygame.time.set_timer(pygame.USEREVENT, 0)
                            messagebox.showinfo("Snake Game", "GAMEOVER!\nScore: " + str(int_length))
                            potentialTermination = messagebox.askquestion("Snake Game", "Would you like to play again?")
                            if potentialTermination == "no":
                                programContinuity = False
                            elif potentialTermination == "yes":
                                consumableObject.set_Width(20)
                                consumableObject.set_Height(20)
                                consumableObject.set_Xrandom(surfaceWindow.get_width() - consumableObject.get_Width())
                                consumableObject.set_Yrandom(surfaceWindow.get_height() - consumableObject.get_Height())
                                listIndex = 0
                                snakeBody = [None]
                                snakeBodyCollide = [None]
                                snakeBody[listIndex] = Snake()
                                snakeBody[listIndex].set_Xpos(surfaceWindow.get_width() // 2)
                                snakeBody[listIndex].set_Ypos(surfaceWindow.get_height() // 2)
                                snakeBody[listIndex].set_Width(20)
                                snakeBody[listIndex].set_Height(20)
                                snakeBodyCollide[listIndex] = Snake()
                                snakeBodyCollide[listIndex].set_Xpos(surfaceWindow.get_width() // 2)
                                snakeBodyCollide[listIndex].set_Ypos(surfaceWindow.get_height() // 2)
                                snakeBodyCollide[listIndex].set_Width(20)
                                snakeBodyCollide[listIndex].set_Height(20)
                                pygame.time.set_timer(pygame.USEREVENT, 125)
                                programContinuity = True
                                snakeDirection = "STOP"
                                bodyDirection = "STOP"
                                previousXposition = [None] 
                                previousYposition = [None] 
                                int_length = 1

        if event.type == KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                if (len(snakeBody) > 1 and snakeDirection != "MOVEDOWN") or len(snakeBody) == 1:
                    snakeDirection = "MOVEUP"
        
            elif event.key == K_s or event.key == K_DOWN:
                if (len(snakeBody) > 1 and snakeDirection != "MOVEUP") or len(snakeBody) == 1:
                    snakeDirection = "MOVEDOWN"
        
            elif event.key == K_a or event.key == K_LEFT:
                if (len(snakeBody) > 1 and snakeDirection != "MOVERIGHT") or len(snakeBody) == 1:
                    snakeDirection = "MOVELEFT"
        
            elif event.key == K_d or event.key == K_RIGHT:
                if (len(snakeBody) > 1 and snakeDirection != "MOVELEFT") or len(snakeBody) == 1:
                    snakeDirection = "MOVERIGHT"

    scoreOutput = scoreFont.render("{:s}{:d}".format("SCORE: ", int_length),
        True, pygame.Color("Yellow"))
    
    for counter in range(len(snakeBody)):
        surfaceWindow.blit(snakeBody[counter].get_Image(), 
            (snakeBody[counter].get_Xpos(), snakeBody[counter].get_Ypos()))

    for counter in range(len(snakeBodyCollide)):
        surfaceWindow.blit(snakeBodyCollide[counter].get_Image(), 
            (snakeBodyCollide[counter].get_Xpos(), snakeBodyCollide[counter].get_Ypos()))

    surfaceWindow.blit(scoreOutput, (surfaceWindow.get_width() - 170, 20))

    consumableObject.output(surfaceWindow)
    pygame.display.update()
    clock.tick(240)
    surfaceWindow.fill([0, 0, 0])
'''
Snake Game Process
- Make the Snake
- Make it move
- Make a list to increase the snake length
- Make the snake able to gain points
'''
'''
NOTES:
- Display the length/ Score
- Use messageboxes to interact with user

# Create 1 square object with color and dimensions
# Create a list that continuous appends new squares to the snake as
the new 
'''

'''
Snake is composed of list of snake units that are a added according to the direction
of the last square unit in the list 
--> if the last sqaure is moving right when first square consumes the object then a square will be added to the left of the last square
For movement, the last square will always follow the square right before it

'''



# Prior Attempts


                # if index > 0:
                #     if unit.get_Xpos() == snakeBody[listIndex - 1].get_Xpos():
                #         if unit.get_Ypos() > snakeBody[listIndex - 1].get_Ypos():
                #             bodyDirection = "MOVEUP"
                #             unit.move(pixels=20, direction=bodyDirection)
                #         elif unit.get_Ypos() < snakeBody[listIndex - 1].get_Ypos():
                #             bodyDirection = "MOVEDOWN"
                #             unit.move(pixels=20, direction=bodyDirection)
                #     elif unit.get_Ypos() == snakeBody[listIndex - 1].get_Ypos():
                #         if unit.get_Xpos() > snakeBody[listIndex - 1].get_Xpos():
                #             bodyDirection = "MOVELEFT"
                #             unit.move(pixels=20, direction=bodyDirection)
                #         elif unit.get_Xpos() < snakeBody[listIndex - 1].get_Xpos():
                #             bodyDirection = "MOVERIGHT"
                #             unit.move(pixels=20, direction=bodyDirection)
                #     else:
                #         unit.move(pixels=20, direction=bodyDirection)
            
                # if snakeDirection == "MOVERIGHT" and listIndex == 1:
                #     if snakeBody[1].get_Ypos() == snakeBody[0].get_Ypos():
                        
                # elif snakeDirection == "MOVELEFT" and listIndex == 1:
                #     if snakeBody[1].get_Ypos() == snakeBody[0].get_Ypos():
                        
                # elif snakeDirection == "MOVEUP" and listIndex == 1:
                #     if snakeBody[1].get_Xpos() == snakeBody[0].get_Xpos():
                        
                # elif snakeDirection == "MOVEDOWN" and listIndex == 1:
                #     if snakeBody[1].get_Xpos() == snakeBody[0].get_Xpos():
                #        snakeBody[1].move(pixels=20, direction="MOVEDOWN")

                # if snakeDirection == "MOVERIGHT":
                #     snakeBody[listIndex].set_Xpos(snakeBody[listIndex - 1].get_Xpos() - 20)
                #     snakeBody[listIndex].set_Ypos(snakeBody[listIndex - 1].get_Ypos())
                #     snakeBody[listIndex].set_Width(20)
                #     snakeBody[listIndex].set_Height(20)

                # elif snakeDirection == "MOVELEFT":
                #     snakeBody[listIndex].set_Xpos(snakeBody[listIndex - 1].get_Xpos() + 20)
                #     snakeBody[listIndex].set_Ypos(snakeBody[listIndex - 1].get_Ypos())
                #     snakeBody[listIndex].set_Width(20)
                #     snakeBody[listIndex].set_Height(20)

                # elif snakeDirection == "MOVEUP":
                #     snakeBody[listIndex].set_Xpos(snakeBody[listIndex - 1].get_Xpos())
                #     snakeBody[listIndex].set_Ypos(snakeBody[listIndex - 1].get_Ypos() + 20)
                #     snakeBody[listIndex].set_Width(20)
                #     snakeBody[listIndex].set_Height(20)

                # elif snakeDirection == "MOVEDOWN":
                #     snakeBody[listIndex].set_Xpos(snakeBody[listIndex - 1].get_Xpos())
                #     snakeBody[listIndex].set_Ypos(snakeBody[listIndex - 1].get_Ypos() - 20)
                #     snakeBody[listIndex].set_Width(20)
                #     snakeBody[listIndex].set_Height(20)