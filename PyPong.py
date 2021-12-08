import pygame



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
GREEN = (0, 255, 0)

X_PLAYER=600
X_MASCHINE=30

rect_player = None
rect_maschien = None

score_player=1
score_maschine=1

ball=[]
player_Y=0
def setup_ini(pyg, scr):

    global rect_player, rect_maschien, score_player, score_maschine, ball,player_Y

    #Mitteilung
    x,y = scr.get_size()
    player_Y=y/2-35
    pyg.draw.rect(scr, GRAY, (x/2-5, 0, 10, y))
    #Maschiene und Player

    rect_player = pygame.Rect(X_PLAYER, y/2-35, 10, 70)
    rect_maschien = pyg.Rect(X_MASCHINE, y/2-35, 10, 70)


    pyg.draw.rect(scr, WHITE, rect_player)
    pyg.draw.rect(scr, WHITE, rect_maschien)

    #Ball in bildmitte
    pyg.draw.circle(scr,WHITE,(x/2,y/2),7)

    font_score1 = pygame.font.SysFont(None, 200)
    font_score2 = pygame.font.SysFont(None, 200)

    text_score1 = font_score1.render(str(score_player), score_maschine, GRAY)
    text_score2 = font_score2.render(str(score_maschine), score_player, GRAY)

    scr.blit(text_score1, (120,50))
    scr.blit(text_score2,(440, 50))

    ball = [1, 1, int(x/2), int(y/2)]

def update_Game(pyg, scr):

    global rect_player, rect_maschien, score_player, score_maschine,ball,player_Y
    scr.fill(BLACK)
    # Mitteilung
    x, y = scr.get_size()

    pyg.draw.rect(scr, GRAY, (x / 2 - 5, 0, 10, y))
    # Maschiene und Player

    #rect_player = pygame.Rect(X_PLAYER, player_Y, 10, 70)
    #rect_maschien = pyg.Rect(X_MASCHINE, y / 2 - 35, 10, 70)

    rect_player.move_ip(0,player_Y)

    pyg.draw.rect(scr, WHITE, rect_player)
    pyg.draw.rect(scr, WHITE, rect_maschien)

    ball[2]=ball[2]+ball[0]
    ball[3]=ball[3]+ball[1]

    if ball[2]>x-10 or ball[2]<10:
        ball[0]=ball[0]*-1
    if ball[3]>y-10 or ball[3]<10:
        ball[1]=ball[1]*-1


    font_score1 = pygame.font.SysFont(None, 200)
    font_score2 = pygame.font.SysFont(None, 200)

    text_score1 = font_score1.render(str(score_player), score_maschine, GRAY)
    text_score2 = font_score2.render(str(score_maschine), score_player, GRAY)

    scr.blit(text_score1, (120, 50))
    scr.blit(text_score2, (440, 50))
    # Ball in bildmitte
    pyg.draw.circle(scr, WHITE, (ball[2],ball[3]), 7)


def player_move(ev):
    global player_Y
    setter1=0
    setter2=0
    if ev.type == pygame.KEYDOWN or setter1==1:
        if pygame.key.name(ev.key)=="s":
            player_Y=player_Y+3
            setter1=1
    if  ev.type == pygame.KEYDOWN or setter2==1:
        if pygame.key.name(ev.key)=="w":
            player_Y=player_Y-3
            setter2=1
    elif ev.type== pygame.KEYUP:
        player_Y=player_Y
        setter1=0
        setter2=0