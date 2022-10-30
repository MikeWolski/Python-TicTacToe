import pygame
import time

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
gray = (60, 60, 60)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 102)
dis_width = 1200
dis_height = 1200
dis = pygame.display.set_mode((dis_width, dis_height), pygame.RESIZABLE)
pygame.display.set_caption("Tic Tac Toe by Mike Wolski")

def gameloop():
    dis_width = dis.get_width()
    dis_height = dis.get_height()
    so = (dis_width + dis_height)/80
    clock = pygame.time.Clock()
    dis.fill(gray)
    font_style = pygame.font.SysFont("bahnschrift", int(so*3.5))
    game_over = False

    rad = dis_width
    if dis_width > dis_height:
        rad = dis_height

    class area():
        def __init__(self, x, y, taken):
            self.rect = pygame.Rect(dis_width*x, dis_height*y, dis_width*1/3, dis_height*1/3)
            self.taken = taken

    aa = area(0,0,0)
    ab = area(1/3,0,0)
    ac = area(2/3,0,0)
    ad = area(0,1/3,0)
    ae = area(1/3,1/3,0)
    af = area(2/3,1/3,0)
    ag = area(0,2/3,0)
    ah = area(1/3,2/3,0)
    ai = area(2/3,2/3,0)

    def board():
        pygame.draw.rect(dis, black, [(dis_width/3)-(so/2), 0, so, dis_height])
        pygame.draw.rect(dis, black, [(dis_width*2/3)-(so/2), 0, so, dis_height])
        pygame.draw.rect(dis, black, [0, (dis_height/3)-(so/2), dis_width, so])
        pygame.draw.rect(dis, black, [0, (dis_height*2/3)-(so/2), dis_width, so])
        pygame.display.update()

    def message(msg,color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width/99, dis_height/2.15])

    def end(msg):
        message(msg, green)
        pygame.display.update()

    def circle(x, y):
        pygame.draw.circle(dis, blue, [dis_width*x, dis_height*y], rad/6.5, int(so))
        pygame.display.update()

    def ex(x, y, a, b):
        pygame.draw.line(dis, red, [dis_width*x, dis_height*a], [dis_width*y, dis_height*b], int(so))
        pygame.draw.line(dis, red, [dis_width*x, dis_height*b], [dis_width*y, dis_height*a], int(so))
        pygame.display.update()

    def win(x):
        if (aa.taken == x and ab.taken == x and ac.taken == x) or (ad.taken == x and ae.taken == x and af.taken == x) or (ag.taken == x and ah.taken == x and ai.taken == x) or (aa.taken == x and ad.taken == x and ag.taken == x) or (ab.taken == x and ae.taken == x and ah.taken == x) or (ac.taken == x and af.taken == x and ai.taken == x) or (aa.taken == x and ae.taken == x and ai.taken == x) or (ac.taken == x and ae.taken == x and ag.taken == x):
            time.sleep(0.5)
            if x == 1:
                end("X's win!")
                time.sleep(3)
                gameloop()
            elif x == 2:
                end("O's win!")
                time.sleep(3)
                gameloop()
        elif aa.taken > 0 and ab.taken > 0 and ac.taken > 0 and ad.taken > 0 and ae.taken > 0 and af.taken > 0 and ag.taken > 0 and ah.taken > 0 and ai.taken > 0:
            end("It's a tie!")
            time.sleep(3)
            gameloop()

    turn = 1
    board()

    while not game_over:
        for event in pygame.event.get():
            win(1)
            win(2)
            if event.type == pygame.QUIT:
                game_over = True
            if event.type==pygame.VIDEORESIZE:
                dis_height = dis.get_height()
                dis_width = dis.get_width()
                dis.fill(gray)
                aa = area(0,0,0)
                ab = area(1/3,0,0)
                ac = area(2/3,0,0)
                ad = area(0,1/3,0)
                ae = area(1/3,1/3,0)
                af = area(2/3,1/3,0)
                ag = area(0,2/3,0)
                ah = area(1/3,2/3,0)
                ai = area(2/3,2/3,0)
                so = (dis_width + dis_height)/80
                font_style = pygame.font.SysFont("bahnschrift", int(so*3.5))
                rad = dis_width
                if dis_width > dis_height:
                    rad = dis_height
                board()
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if turn%2 != 0:
                        if aa.rect.collidepoint(event.pos):
                            if aa.taken == 0:
                                turn += 1
                                ex(0, 1/3, 0, 1/3)
                                board()
                                aa.taken = 1
                        elif ab.rect.collidepoint(event.pos):
                            if ab.taken == 0:
                                turn += 1
                                ex(1/3, 2/3, 0, 1/3)
                                board()
                                ab.taken = 1
                        elif ac.rect.collidepoint(event.pos):
                            if ac.taken == 0:
                                turn += 1
                                ex(2/3, 1, 0, 1/3)
                                board()
                                ac.taken = 1
                        elif ad.rect.collidepoint(event.pos):
                            if ad.taken == 0:
                                turn += 1
                                ex(0, 1/3, 1/3, 2/3)
                                board()
                                ad.taken = 1
                        elif ae.rect.collidepoint(event.pos):
                            if ae.taken == 0:
                                turn += 1
                                ex(1/3, 2/3, 1/3, 2/3)
                                board()
                                ae.taken = 1
                        elif af.rect.collidepoint(event.pos):
                            if af.taken == 0:
                                turn += 1
                                ex(2/3, 1, 1/3, 2/3)
                                board()
                                af.taken = 1
                        elif ag.rect.collidepoint(event.pos):
                            if ag.taken == 0:
                                turn += 1
                                ex(0, 1/3, 2/3, 1)
                                board()
                                ag.taken = 1
                        elif ah.rect.collidepoint(event.pos):
                            if ah.taken == 0:
                                turn += 1
                                ex(1/3, 2/3, 2/3, 1)
                                board()
                                ah.taken = 1
                        elif ai.rect.collidepoint(event.pos):
                            if ai.taken == 0:
                                turn += 1
                                ex(2/3, 1, 2/3, 1)
                                board()
                                ai.taken = 1
                    elif turn%2 == 0:
                        if aa.rect.collidepoint(event.pos):
                            if aa.taken == 0:
                                turn += 1
                                circle(1/6, 1/6)
                                board()
                                aa.taken = 2
                        elif ab.rect.collidepoint(event.pos):
                            if ab.taken == 0:
                                turn += 1
                                circle(1/2, 1/6)
                                board()
                                ab.taken = 2
                        elif ac.rect.collidepoint(event.pos):
                            if ac.taken == 0:
                                turn += 1
                                circle(5/6, 1/6)
                                board()
                                ac.taken = 2
                        elif ad.rect.collidepoint(event.pos):
                            if ad.taken == 0:
                                turn += 1
                                circle(1/6, 1/2)
                                board()
                                ad.taken = 2
                        elif ae.rect.collidepoint(event.pos):
                            if ae.taken == 0:
                                turn += 1
                                circle(1/2, 1/2)
                                board()
                                ae.taken = 2
                        elif af.rect.collidepoint(event.pos):
                            if af.taken == 0:
                                turn += 1
                                circle(5/6, 1/2)
                                board()
                                af.taken = 2
                        elif ag.rect.collidepoint(event.pos):
                            if ag.taken == 0:
                                turn += 1
                                circle(1/6, 5/6)
                                board()
                                ag.taken = 2
                        elif ah.rect.collidepoint(event.pos):
                            if ah.taken == 0:
                                turn += 1
                                circle(1/2, 5/6)
                                board()
                                ah.taken = 2
                        elif ai.rect.collidepoint(event.pos):
                            if ai.taken == 0:
                                turn += 1
                                circle(5/6, 5/6)
                                board()
                                ai.taken = 2
        clock.tick(60)
    pygame.quit()
    quit()
gameloop()