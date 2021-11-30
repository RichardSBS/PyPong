# import the pygame module, so you can use it
import pygame
green=(0,255,0)
white=(255,255,255)
balck=(0,0,0)
color=green
setterx=1
settery=0
clock = pygame.time.Clock()
# define a main function

# initialize the pygame module
pygame.init()
# load and set the logo
#logo = pygame.image.load("python.png")
#pygame.display.set_icon(logo)

pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
screen = pygame.display.set_mode((800, 600))


    # define a variable to control the main loop
running = True

    # main loop
posx = 200
posy = 200
while running:


        # event handling, gets all event from the event queue
    for event in pygame.event.get():
            # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
            running = False

    pygame.draw.rect(screen, (255, 255, 255), [10, 20, 20, 200])
    pygame.draw.rect(screen, (255, 255, 255), [760, 10, 20, 200])
    pygame.draw.rect(screen, color, [posx, posy, 20, 20])

    #posy = posy+4
    if setterx == 1:
        posx = posx + 4

    if setterx==0:
        posx= posx - 4

    if settery == 1:
        posy = posy + 4

    if settery == 0:
        posy = posy - 4

    if posx >= 740:
        setterx = 0
        color = (0, 255, 0)
    if posx<=50:
        setterx=1
        color = (255, 0, 0)
    if posy >= 500:
        settery = 0
        color = (255, 255, 255)
    if posy <= 50:
        settery = 1
        color = (0, 0, 255)

    pygame.display.flip()
    screen.fill(balck)
    clock.tick(1000)
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
