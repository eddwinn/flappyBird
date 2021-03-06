import pygame
from random import randint


pygame.init()



white = (255,255,255)
black = (0,0,0)


red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)



smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)




display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Flappy')


pygame.init()

done = False
clock = pygame.time.Clock()


def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

def ball(x, y):
    pygame.draw.circle(gameDisplay, black, [x, y], 20)

def gameover():
    message_to_screen("Game Over", black, -30)

def obstacle(xloc, yloc, xsize, ysize):
    pygame.draw.rect(gameDisplay, green, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(gameDisplay, green, [xloc, int(yloc+ysize+space), xsize, ysize+500])

def Score(score):
    message_to_screen(("score: "+str(score)), black,  -12)





x = 350
y = 250
x_speed = 0
y_speed = 0
ground = 600
xloc = 800
yloc = 0
xsize = 80
ysize = randint(200, 550)
space = 220
obspeed = 2.5
score = 0







while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_speed = -10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_speed = 5


    gameDisplay.fill(white)
    obstacle(xloc,yloc,xsize,ysize)
    ball(x, y)
    Score(score)

    y += y_speed
    xloc -= obspeed

    if y > ground:
        gameover()
        y_speed = 0
        obspeed = 0

    if xloc < -80:
        xloc = 800
        ysize = randint(100,450)

    if x+20 > xloc and y < ysize and x-15 < xsize + xloc:
        gameover()
        obspeed = 0
        y_speed = 0

    if x+20 > xloc and y < ysize + space and x-15 < xsize + xloc:
        gameover()
        obspeed = 0
        y_speed = 0

    if x > xloc and x < xloc+3:
        score = (score+1)


    else:
        y += y_speed
        xloc -= obspeed

    if x >xloc and x < xloc+3:
        score = (score + 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()





