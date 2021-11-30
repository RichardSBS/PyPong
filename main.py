from PyPong import*


pygame.init()

screen=pygame.display.set_mode((640, 480))

setup_ini(pygame,screen)

running = True

    # main loop

while running:


        # event handling, gets all event from the event queue
    for event in pygame.event.get():
            # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
            running = False
    pygame.display.flip()