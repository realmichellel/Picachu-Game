
import pygame


pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

clock = pygame.time.Clock()

carImg1 = pygame.image.load('mario1.jpg')
carImg2 = pygame.image.load('mario2.png')
carCurrentImage = 1
gameDisplay = pygame.display.set_mode((display_width,display_height))

gameLoop=True
while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    gameDisplay.fill(white)

    if carCurrentImage ==1:
        gameDisplay.blit(carImg1, (100,100))
    if carCurrentImage ==2:
        gameDisplay.blit(carImg2, (100,100))
    if carCurrentImage ==2:
        carCurrentImage =1
    else:
        carCurrentImage +=1
    pygame.display.update()
    clock.tick(10)
    
pygame.quit()
