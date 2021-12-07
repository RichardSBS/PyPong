# import the pygame module, so you can use it
import pygame
#Farben
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (50,50,50)
GREEN = (0,255,0)
setterx=1
settery=0

posx = 200
posy = 200
clock = pygame.time.Clock()

# initialisiren des pygame modules
pygame.init()

#So soll mein Fenster heißen
pygame.display.set_caption("PyPong")

#Festlegen einer variable die meine GUI beinhaltet mit den ausmaßen die ich angegeben hab
screen = pygame.display.set_mode((800, 600))

def ballRichtung(setterx,settery,x,y):
    if setterx == 1:
        posx = x + 4

    if setterx == 0:
        posx = x - 4

    if settery == 1:
        posy = y + 4

    if settery == 0:
        posy = y - 4
    return posx,posy


def setter(posx,posy):
    if posx >= 740:
        setterx = 0
    if posx<=50:
        setterx=1
    if posy >= 500:
        settery = 0
    if posy <= 50:
        settery = 1
# define a variable to control the main loop
running = True

    # main loop

while running:


        # event handling, gets all event from the event queue
    for event in pygame.event.get():
            # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
            running = False

    pygame.draw.rect(screen, WHITE, [10, 20, 20, 200])
    pygame.draw.rect(screen, WHITE, [760, 10, 20, 200])
    pygame.draw.rect(screen, WHITE, [posx, posy, 20, 20])


    posx,posy=ballRichtung(setterx,settery,posx,posy)
    setter(posx,posy)
    pygame.display.flip()
    screen.fill(BLACK)
    clock.tick(1000)
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
