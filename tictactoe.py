import pygame
import pygame_gui
import time

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
gray = (60, 60, 60)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255,255,0)
purple = (138,43,226)
orange = (255,165,0)
pink = (255,105,180)
dis_width = 800
dis_height = 800
dis = pygame.display.set_mode((dis_width, dis_height), pygame.RESIZABLE)
pygame.display.set_caption("Tic Tac Toe by Mike Wolski")
clock = pygame.time.Clock()

manager = pygame_gui.UIManager((dis_width, dis_height))

xc = red
cc = blue

def startscreen(xc, cc):
    dis_width = dis.get_width()
    dis_height = dis.get_height()
    manager.clear_and_reset()
    manager.set_window_resolution((dis_width, dis_height))
    so = (dis_width + dis_height)/80
    title_font = pygame.font.SysFont("bahnschrift", int(so*4))
    font_style = pygame.font.SysFont("bahnschrift", int(so*2))
    dis.fill(gray)
    rad = dis_width
    if dis_width > dis_height:
        rad = dis_height

    def message(msg,color, x, y):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [(dis_width-mesg.get_rect().width)/2, y])
    
    def title(msg,color, y):
        mesg = title_font.render(msg, True, color)
        dis.blit(mesg, [(dis_width-mesg.get_rect().width)/2, y])

    def circle(color):
        pygame.draw.circle(dis, color, [dis_width*3/4, dis_height*1/3], rad/9, int(so))
        pygame.display.update()

    def ex(color):
        pygame.draw.line(dis, color, [dis_width*1/6, dis_height*1/4], [dis_width*1/3, dis_height*7/16], int(so))
        pygame.draw.line(dis, color, [dis_width*1/6, dis_height*7/16], [dis_width*1/3, dis_height*1/4], int(so))
        pygame.display.update()

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/2-so*5, dis_height*1/3), (so*10, so*2)), text="Start", manager=manager)

    ex(xc)
    red_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2), (so*10, so*2)), text="Red", manager=manager)
    green_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*2), (so*10, so*2)), text="Green", manager=manager)
    blue_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*4), (so*10, so*2)), text="Blue", manager=manager)
    yellow_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*6), (so*10, so*2)), text="Yellow", manager=manager)
    purple_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*8), (so*10, so*2)), text="Purple", manager=manager)
    orange_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*10), (so*10, so*2)), text="Orange", manager=manager)
    pink_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*12), (so*10, so*2)), text="Pink", manager=manager)

    circle(cc)
    red_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2), (so*10, so*2)), text="Red", manager=manager)
    green_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*2), (so*10, so*2)), text="Green", manager=manager)
    blue_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*4), (so*10, so*2)), text="Blue", manager=manager)
    yellow_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*6), (so*10, so*2)), text="Yellow", manager=manager)
    purple_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*8), (so*10, so*2)), text="Purple", manager=manager)
    orange_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*10), (so*10, so*2)), text="Orange", manager=manager)
    pink_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*12), (so*10, so*2)), text="Pink", manager=manager)
    
    while True:
        time_delta = clock.tick(60)/1000.0
        title("TicTacToe", white, 0)
        manager.draw_ui(dis)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.VIDEORESIZE:
                dis_height = dis.get_height()
                dis_width = dis.get_width()
                rad = dis_width
                if dis_width > dis_height:
                    rad = dis_height
                so = (dis_width + dis_height)/80
                title_font = pygame.font.SysFont("bahnschrift", int(so*4))
                font_style = pygame.font.SysFont("bahnschrift", int(so*2))
                dis.fill(gray)
                manager.clear_and_reset()
                manager.set_window_resolution((dis_width, dis_height))
                title("TicTacToe", white, 0)
                start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/2-so*5, dis_height*1/3), (so*10, so*2)), text="Start", manager=manager)
                so = (dis_width + dis_height)/80
                ex(xc)
                red_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2), (so*10, so*2)), text="Red", manager=manager)
                green_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*2), (so*10, so*2)), text="Green", manager=manager)
                blue_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*4), (so*10, so*2)), text="Blue", manager=manager)
                yellow_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*6), (so*10, so*2)), text="Yellow", manager=manager)
                purple_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*8), (so*10, so*2)), text="Purple", manager=manager)
                orange_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*10), (so*10, so*2)), text="Orange", manager=manager)
                pink_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*12), (so*10, so*2)), text="Pink", manager=manager)

                circle(cc)
                red_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2), (so*10, so*2)), text="Red", manager=manager)
                green_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*2), (so*10, so*2)), text="Green", manager=manager)
                blue_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*4), (so*10, so*2)), text="Blue", manager=manager)
                yellow_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*6), (so*10, so*2)), text="Yellow", manager=manager)
                purple_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*8), (so*10, so*2)), text="Purple", manager=manager)
                orange_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*10), (so*10, so*2)), text="Orange", manager=manager)
                pink_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*12), (so*10, so*2)), text="Pink", manager=manager)

                pygame.display.update()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    gameloop(cc, xc)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == red_button:
                    xc = red
                    ex(red)
                    pygame.display.update()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == green_button:
                    xc = green
                    ex(green)
                    pygame.display.update()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == blue_button:
                    xc = blue
                    ex(blue)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == yellow_button:
                    xc = yellow
                    ex(yellow)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == purple_button:
                    xc = purple
                    ex(purple)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == orange_button:
                    xc = orange
                    ex(orange)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == pink_button:
                    xc = pink
                    ex(pink)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == red_buttono:
                    cc = red
                    circle(red)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == green_buttono:
                    cc = green
                    circle(green)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == blue_buttono:
                    cc = blue
                    circle(blue)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == yellow_buttono:
                    cc = yellow
                    circle(yellow)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == purple_buttono:
                    cc = purple
                    circle(purple)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == orange_buttono:
                    cc = orange
                    circle(orange)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == pink_buttono:
                    cc = pink
                    circle(pink)
            manager.process_events(event)
        manager.update(time_delta)
def gameloop(cc, xc):
    dis_width = dis.get_width()
    dis_height = dis.get_height()
    so = (dis_width + dis_height)/80
    dis.fill(gray)
    font_style = pygame.font.SysFont("bahnschrift", int(so*8))
    game_over = False
    xcolor = xc
    ocolor = cc
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
        dis.blit(mesg, [(dis_width-mesg.get_rect().width)/2, (dis_height-mesg.get_rect().height)/2])

    def end(msg):
        message(msg, green)
        pygame.display.update()

    def circle(x, y):
        pygame.draw.circle(dis, ocolor, [dis_width*x, dis_height*y], rad/6.5, int(so))
        pygame.display.update()

    def ex(x, y, a, b):
        pygame.draw.line(dis, xcolor, [dis_width*x, dis_height*a], [dis_width*y, dis_height*b], int(so))
        pygame.draw.line(dis, xcolor, [dis_width*x, dis_height*b], [dis_width*y, dis_height*a], int(so))
        board()
        pygame.display.update()

    def win(x):
        if (aa.taken == x and ab.taken == x and ac.taken == x) or (ad.taken == x and ae.taken == x and af.taken == x) or (ag.taken == x and ah.taken == x and ai.taken == x) or (aa.taken == x and ad.taken == x and ag.taken == x) or (ab.taken == x and ae.taken == x and ah.taken == x) or (ac.taken == x and af.taken == x and ai.taken == x) or (aa.taken == x and ae.taken == x and ai.taken == x) or (ac.taken == x and ae.taken == x and ag.taken == x):
            time.sleep(0.5)
            if x == 1:
                end("X's win!")
                time.sleep(3)
                startscreen(xc, cc)
            elif x == 2:
                end("O's win!")
                time.sleep(3)
                startscreen(xc, cc)
        elif aa.taken > 0 and ab.taken > 0 and ac.taken > 0 and ad.taken > 0 and ae.taken > 0 and af.taken > 0 and ag.taken > 0 and ah.taken > 0 and ai.taken > 0:
            end("It's a tie!")
            time.sleep(3)
            startscreen(xc, cc)

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
                font_style = pygame.font.SysFont("bahnschrift", int(so*8))
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

startscreen(xc, cc)