import pygame

from PyPong import*


pygame.init()

screen=pygame.display.set_mode((640, 480))

setup_ini(pygame,screen)

running = True
started=False
    # main loop

while running:


        # event handling, gets all event from the event queue
    for event in pygame.event.get():
        player_move(event)
            # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
            running = False

        if event.type==pygame.KEYDOWN:
            if pygame.key.name(event.key)=="g":
                started=True

    if started:
        #player_move(event)
        update_Game(pygame,screen)


    pygame.display.flip()
