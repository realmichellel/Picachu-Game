import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
brightgreen = (0,255,0)

carImg1 = pygame.image.load('Pokeman1.png')
carImg2 = pygame.image.load('Pokeman2.png')
background = pygame.image.load('Background.png')
gameover = pygame.image.load('Picachucry.png')
pikachu = 1

car_width = 80
gameDisplay = pygame.display.set_mode((display_width,display_height))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    #pygame built in function
    return textSurface, textSurface.get_rect()
def scoreboard(count):
    font = pygame.font.SysFont(None,35)
    text = font.render("Scored: " + str(count), True, black)
    gameDisplay.blit(text,(20,20))
    
def blocks(blockx, blocky, blockw, blockh, color):
    pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)
        #show stuff
    message2('Start Over')
    pygame.display.update()
    
    time.sleep(2)

    game_intro()
    
def message2(blabla):
    smallText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(blabla,smallText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def crash():
       
    gameDisplay.fill(white)
    gameDisplay.blit(pygame.transform.scale(gameover, (400, 400)), (400,300))
    message_display('Pikachu died!')
    
    pygame.display.update()

   
    

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(pygame.transform.scale(background, (800, 600)), (0,0))
        largeText = pygame.font.Font('freesansbold.ttf',95)
        TextSurf, TextRect = text_objects('Pokeman Game',largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
        button("GO!",320,300,150,80,green,brightgreen)
        
  
def button(message,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    

    if x+w> mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        # mouse[0] = mouse x position(first element of mouse), mouse[1] = mouse y position
        if click[0] == 1:
            game()
            
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    #(place to draw, color, top corner x, top corner y, width, height)
    mediumText = pygame.font.Font('freesansbold.ttf',30)
    textSurf, textRect = text_objects(message, mediumText)
    textRect.center = ((x+w/2),(y+h/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    

        
def game():

    def car(x,y):
           gameDisplay.blit(pygame.transform.scale(carImg1, (80, 100)), (x,y))
     
    x = (display_width*0.9)
    y = (display_height*0.8)

    x_change = 0
    
    block_width = 100
    block_startx = random.randrange(0,display_width - block_width - 20)
    block_starty = -200
    block_speed = 4
    block_width = 100
    block_height = 20
    score = 0


    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Pikachu Game')
    timing = pygame.time.Clock()

    gameExit = False
  
    while not gameExit:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
            
                    x_change = -10
 
                    
                if event.key == pygame.K_RIGHT:
                    #elif makes the moving not so smooth
                    x_change = 10
    
            if event.type == pygame.KEYUP:
                
                if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
        x += x_change                 
                    
        gameDisplay.fill(white)
        #background,default is black which is nothing, must put it infront of car
        #otherwise the paint will cover the car
        gameDisplay.blit(pygame.transform.scale(background, (800, 600)), (0,0))

        blocks(block_startx, block_starty, block_width, block_height, black)
        block_starty += block_speed
        #blocks(blockx, blocky, blockw, blockh, color)
        
        car(x,y)
        scoreboard(score)

        if x + car_width > display_width or x<0:
            crash()
            
        if block_starty > display_height:
            block_starty = 0 - block_height
            block_startx = random.randrange(0, display_width - block_width -20)
            score+=1
            if block_speed <15:
               block_speed+=0.5
            
        if y < block_starty + block_height -20:
            

            if x> block_startx and x < block_startx + block_width-10 or x+car_width-10 > block_startx and x+car_width <block_startx+block_width-10:

                crash()
            
            
        pygame.display.update()
      
        
        #or pygame.display.flip(), this will show all the operations we did prior
        timing.tick(60)
    
game_intro()
game()

