import pygame
(width, height) = (600, 200)
screen = pygame.display.set_mode((width, height))
pygame.draw.rect(screen,(0,255,0),[10, 20, 100, 100], 0)
game=True
while game:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (0, 255, 0), [10, 20, 100, 100], 0)
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            game = False

#pygame.draw.rect(screen, [10, 20, 100, 100], 1)

