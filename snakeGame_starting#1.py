import random
import pygame
import time

pygame.init()

violet = (200 , 15 , 196)
white = (255, 255, 255)
black = (0, 0, 0)
red = (150, 0, 0)
hotRed = (255, 0, 0)
gameRed = (220 , 0 , 0)
yellow = (200, 200, 0)
brightYellow = (255, 255, 51)
green = (0, 150, 0)
lightGreen = (0 , 255 , 0)
gameGreen = (0 , 220 , 0)
blue = (0, 0, 255)
hue = (12, 35, 67)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither.io')
icon = pygame.image.load('sprites/icon.png')
pygame.display.set_icon(icon)
img = pygame.image.load('sprites/snakeHead.png')
imgApple = pygame.image.load('sprites/Apple.png')

clock = pygame.time.Clock()

block_size = 20
FPS = 25
AppleThickness = 30

direction = "right"
smallfont = pygame.font.SysFont(None, 30)
medfont = pygame.font.SysFont(None, 65)
largefont = pygame.font.SysFont(None, 100)
titlefont = pygame.font.SysFont("Algerian" , 80)


def text_Objects(text , color, size="small"):
    if size =="small":

        textSurface = smallfont.render(text , True , color)

    if size == "medium":
        textSurface = medfont.render(text, True, color)

    if size == "large":
        textSurface = largefont.render(text, True, color)

    if size == "titlefont":
        textSurface = titlefont.render(text , True , color)
    return textSurface , textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_Objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)

def pause():

    paused = True
    message_to_screen("Paused",
                      black,
                      -100,
                      size="large")

    message_to_screen("Press C to continue or Q to QUIT",
                      black,
                      25)

    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            """
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #gameDisplay.fill(white)

        clock.tick(5)

def game_controls():
    gcont = True

    while gcont:
        for event in pygame.event.get():
            """
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    gameLoop()



        gameDisplay.fill(hue)
        message_to_screen("CONTROLS", lightGreen, -270, size="medium")
        message_to_screen("Move Snake Up & Down : Up and down arrows keys", black, -220)
        message_to_screen("Move Snake Right & Left : Left and Right arrows keys", black, -190)
        message_to_screen("Press P to Pause , C to Continue or Q to Quit", black, -160)

        message_to_screen("-------------------------------------------------------------------------------------",black,-125)



        message_to_screen("INSTRUCTIONS:",violet,-75 , size="medium")

        message_to_screen("1) Don't  crash into walls!",black,-20)

        message_to_screen("2) Runnin' backwards is counted under foul play.",black,10)

        message_to_screen("3)ShortCut Key : Press C to play , P to pause or Q to quit(works on every screen)",black,40,size="small")

        message_to_screen("-------------------------------------------------------------------------------------",black,70)

        # format = x1+y1 > cur[0] > x1 and x2 + y2 > cur[1] > y1:{
        # programing format:
        # if x1+y1 > cur[0] > x1 and x2 + y2 > cur[1] > y1:
        # else:}
        button("PLAY", 150, 500, 100, 55 , green , lightGreen , action="PLAY")
        button("Main Menu",  300, 500, 170, 55 , yellow , brightYellow , action="Main Menu")
        button("QUIT",  525, 500, 100, 55 , red , hotRed , action="QUIT")

        pygame.display.update()

        clock.tick(15)






def button(text , x , y , width , height , inactive_color , active_color  , text_color = black , action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay , active_color , (x ,y , width , height))
        if click[0] == 1 and action != None:
            if action == "QUIT":
                pygame.quit()
                quit()
            if action == "CONTROLS":
                game_controls()
            if action == "PLAY":
                gameLoop()
            if action == "Main Menu":
                game_intro()
            if action == "quit_endScreen":
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(gameDisplay , inactive_color , (x ,y , width , height))
    text_to_button(text , black , x , y , width , height)



def score(score):
    text  = medfont.render("Score: " +str(score) , True ,  black)
    gameDisplay.blit(text , [0 ,0])


def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))  # / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - AppleThickness))  # / 10.0) * 10.0
    return  randAppleX , randAppleY

def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            """
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()



        gameDisplay.fill(hue)
        message_to_screen("Welcome to Slither" ,
                          gameRed,
                          -220,
                          size="titlefont")

        message_to_screen("--------------------------------------------------------------------------------------------------------------",
                          black,
                          -185)

        message_to_screen("The objective of the game is to eat as many as Red Apples as possible ",
                          black,
                          0)

        message_to_screen(" to score highest and probably acheive rewards!",
                          black,
                          30)



        button("PLAY", 150, 500, 100, 55 , green , lightGreen , action="PLAY")
        button("CONTROLS",  300, 500, 170, 55 , yellow , brightYellow , action="CONTROLS")
        button("QUIT",  525, 500, 100, 55 , red , hotRed , action="QUIT")

        pygame.display.update()
        clock.tick(15)

def snake(block_size , snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img , 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img , 180)



    gameDisplay.blit(head, (snakeList[-1][0] , snakeList[-1][1]))
    for XnY in snakeList[:-1]:

        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])



def message_to_screen(msg, color , y_displace=0 , size = "small"):
    textSurf , textRect = text_Objects(msg,  color , size)

    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width / 5.3, display_height / 2.2])
    textRect.center = (display_width / 2) , (display_height / 2) + y_displace
    gameDisplay.blit(textSurf , textRect)
def gameLoop():
    global direction
    direction = "right"
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0
    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()
    while not gameExit:



        while gameOver == True:
            gameDisplay.fill(gameRed)

            #final_score = largeFont.render("Score: " )

            message_to_screen("  Game Over ",
                              black ,
                              y_displace=-75 ,
                              size="large")

            message_to_screen("",
                              black,
                              y_displace=120,
                              size="large")

            button("PLAY AGAIN", 200, 400, 150, 55, green, lightGreen, action="PLAY")
            button("QUIT", 525, 400, 100, 55, violet , violet, action="quit_endScreen")
            pygame.display.update()

            for _ in pygame.event.get():

                if _.type == pygame.QUIT:
                    gameOver = False               # can delete this shit if wanna cause cross-exit really doen't matters
                    gameExit = True
                    print("loser quits the game!")

                if _.type == pygame.KEYDOWN:
                    if _.key ==  pygame.K_q:
                        gameExit = True
                        gameOver = False
                        print("ha ha ha! you suck loser")
                    if _.key == pygame.K_c:
                        print(" Here we go again!")
                        gameLoop()




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change



        gameDisplay.fill((gameGreen))
        #pygame.draw.rect(gameDisplay ,red, [randAppleX ,randAppleY, AppleThickness, AppleThickness])
        gameDisplay.blit(imgApple , (randAppleX , randAppleY))
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]


        snake(block_size , snakeList)
        score(snakeLength-1)
        pygame.display.update()



        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            #print(" x crossover ")
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                print("snake ate an apple!")
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                print("snake ate an apple!")




        clock.tick(FPS)


    pygame.quit()
    quit()

game_intro()
gameLoop()