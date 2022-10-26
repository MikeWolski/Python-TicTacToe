import pygame

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 102)

dis_width = 1200
dis_height = 1200

clock = pygame.time.Clock()

dis = pygame.display.set_mode((dis_width, dis_height), pygame.RESIZABLE)
pygame.display.set_caption("Tic Tac Toe by Mike Wolski")
dis.fill(white)
pygame.draw.rect(dis, black, [(dis_width/3)-5, 0, 10, dis_height])
pygame.draw.rect(dis, black, [(dis_width*2/3)-5, 0, 10, dis_height])
pygame.draw.rect(dis, black, [0, (dis_height/3)-5, dis_width, 10])
pygame.draw.rect(dis, black, [0, (dis_height*2/3)-5, dis_width, 10])
pygame.display.update()

game_over = False

class area():
    def __init__(self, x, y, taken):
        self.rect = pygame.Rect(dis_width*x, dis_height*y, dis_width*1/3, dis_height*1/3)
        self.taken = taken

areaa = area(0,0,0)
areab = area(1/3,0,0)
areac = area(2/3,0,0)
aread = area(0,1/3,0)
areae = area(1/3,1/3,0)
areaf = area(2/3,1/3,0)
areag = area(0,2/3,0)
areah = area(1/3,2/3,0)
areai = area(2/3,2/3,0)

def circle(x, y):
    pygame.draw.circle(dis, blue, [dis_width*x, dis_height*y], dis_width/6.5, 10)
    pygame.display.update()

def square(x, y, a, b):
    pygame.draw.line(dis, red, [dis_width*x, dis_height*a], [dis_width*y, dis_height*b], 10)
    pygame.draw.line(dis, red, [dis_width*x, dis_height*b], [dis_width*y, dis_height*a], 10)
    pygame.display.update()

turn = 1

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if turn%2 != 0:
                    if areaa.rect.collidepoint(event.pos):
                        if areaa.taken == 0:
                            turn += 1
                            square(0, 1/3, 0, 1/3)
                            areaa.taken = 1
                    elif areab.rect.collidepoint(event.pos):
                        if areab.taken == 0:
                            turn += 1
                            square(1/3, 2/3, 0, 1/3)
                            areab.taken = 1
                    elif areac.rect.collidepoint(event.pos):
                        if areac.taken == 0:
                            turn += 1
                            square(2/3, 1, 0, 1/3)
                            areac.taken = 1
                    elif aread.rect.collidepoint(event.pos):
                        if aread.taken == 0:
                            turn += 1
                            square(0, 1/3, 1/3, 2/3)
                            aread.taken = 1
                    elif areae.rect.collidepoint(event.pos):
                        if areae.taken == 0:
                            turn += 1
                            square(1/3, 2/3, 1/3, 2/3)
                            areae.taken = 1
                    elif areaf.rect.collidepoint(event.pos):
                        if areaf.taken == 0:
                            turn += 1
                            square(2/3, 1, 1/3, 2/3)
                            areaf.taken = 1
                    elif areag.rect.collidepoint(event.pos):
                        if areag.taken == 0:
                            turn += 1
                            square(0, 1/3, 2/3, 1)
                            areag.taken = 1
                    elif areah.rect.collidepoint(event.pos):
                        if areah.taken == 0:
                            turn += 1
                            square(1/3, 2/3, 2/3, 1)
                            areah.taken = 1
                    elif areai.rect.collidepoint(event.pos):
                        if areai.taken == 0:
                            turn += 1
                            square(2/3, 1, 2/3, 1)
                            areai.taken = 1
                elif turn%2 == 0:
                    if areaa.rect.collidepoint(event.pos):
                        if areaa.taken == 0:
                            turn += 1
                            circle(1/6, 1/6)
                            areaa.taken = 1
                    elif areab.rect.collidepoint(event.pos):
                        if areab.taken == 0:
                            turn += 1
                            circle(1/2, 1/6)
                            areab.taken = 1
                    elif areac.rect.collidepoint(event.pos):
                        if areac.taken == 0:
                            turn += 1
                            circle(5/6, 1/6)
                            areac.taken = 1
                    elif aread.rect.collidepoint(event.pos):
                        if aread.taken == 0:
                            turn += 1
                            circle(1/6, 1/2)
                            aread.taken = 1
                    elif areae.rect.collidepoint(event.pos):
                        if areae.taken == 0:
                            turn += 1
                            circle(1/2, 1/2)
                            areae.taken = 1
                    elif areaf.rect.collidepoint(event.pos):
                        if areaf.taken == 0:
                            turn += 1
                            circle(5/6, 1/2)
                            areaf.taken = 1
                    elif areag.rect.collidepoint(event.pos):
                        if areag.taken == 0:
                            turn += 1
                            circle(1/6, 5/6)
                            areag.taken = 1
                    elif areah.rect.collidepoint(event.pos):
                        if areah.taken == 0:
                            turn += 1
                            circle(1/2, 5/6)
                            areah.taken = 1
                    elif areai.rect.collidepoint(event.pos):
                        if areai.taken == 0:
                            turn += 1
                            circle(5/6, 5/6)
                            areai.taken = 1
    clock.tick(30)

pygame.quit()
quit()