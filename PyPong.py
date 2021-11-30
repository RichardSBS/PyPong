import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
GREEN = (0, 255, 0)

X_PLAYER=600
X_MASCHINE=30
rect_player = None
rect_maschien = None
score_player=0
score_maschine=0


def setup_ini(pyg, scr):

    #Mitteilung
    x,y = scr.get_size()
    pyg.draw.rect(scr, GRAY, (x/2-5, 0, 10, y))
    #Maschiene und Player

    rect_player = pygame.Rect(X_PLAYER, y/2-35, 10, 70)
    rect_maschien = pyg.Rect(X_MASCHINE, y/2-35, 10, 70)


    pyg.draw.rect(scr, WHITE, rect_player)
    pyg.draw.rect(scr, WHITE, rect_maschien)

    #Ball in bildmitte
    pyg.draw.circle(scr,WHITE,(x/2, y/2),7)

    font_score1 = pygame.font.SysFont(None, 200)
    font_score2 = pygame.font.SysFont(None, 200)

    text_score1 = font_score1.render(str(score_player), None, GRAY)
    text_score2 = font_score2.render(str(score_maschine), None, GRAY)

    scr.blit(text_score1, (120,50))
    scr.blit(text_score2,(440, 50))