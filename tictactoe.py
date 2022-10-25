
import pygame
import time

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 102)

dis_width = 1600
dis_height = 1600

clock = pygame.time.Clock()

dis = pygame.display.set_mode((dis_width, dis_height), pygame.RESIZABLE)
pygame.display.set_caption("Tic Tac Toe by Mike Wolski")

game_over = False

areaa = pygame.Rect(dis_width*0, dis_height*0, dis_width/3, dis_height/3)
areab = pygame.Rect(dis_width/3, dis_width*0, dis_width/3, dis_height/3)
areac = pygame.Rect(dis_width*2/3, dis_width*0, dis_width/3, dis_height/3)
aread = pygame.Rect(dis_width*0, dis_height/3, dis_width/3, dis_height/3)
areae = pygame.Rect(dis_width/3, dis_height/3, dis_width/3, dis_height/3)
areaf = pygame.Rect(dis_width*2/3, dis_height/3, dis_width/3, dis_height/3)
areag = pygame.Rect(dis_width*0, dis_height*2/3, dis_width/3, dis_height/3)
areah = pygame.Rect(dis_width/3, dis_height*2/3, dis_width/3, dis_height/3)
areai = pygame.Rect(dis_width*2/3, dis_height*2/3, dis_width/3, dis_height/3)

def circle(x, y):
    pygame.draw.circle(dis, blue, [dis_width*x, dis_height*y], dis_width/6.5, 10)
    pygame.display.update()

def square(x, y, a, b):
    pygame.draw.line(dis, red, [dis_width*x, dis_height*a], [dis_width*y, dis_height*b], 10)
    pygame.draw.line(dis, red, [dis_width*x, dis_height*b], [dis_width*y, dis_height*a], 10)
    pygame.display.update()

dis.fill(white)
pygame.draw.rect(dis, black, [(dis_width/3)-5, 0, 10, dis_height])
pygame.draw.rect(dis, black, [(dis_width*2/3)-5, 0, 10, dis_height])
pygame.draw.rect(dis, black, [0, (dis_height/3)-5, dis_width, 10])
pygame.draw.rect(dis, black, [0, (dis_height*2/3)-5, dis_width, 10])
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if areaa.collidepoint(event.pos):
                    square(0, 1/3, 0, 1/3)
                elif areab.collidepoint(event.pos):
                    square(1/3, 2/3, 0, 1/3)
                elif areac.collidepoint(event.pos):
                    square(2/3, 1, 0, 1/3)
                elif aread.collidepoint(event.pos):
                    square(0, 1/3, 1/3, 2/3)
                elif areae.collidepoint(event.pos):
                    square(1/3, 2/3, 1/3, 2/3)
                elif areaf.collidepoint(event.pos):
                    square(2/3, 1, 1/3, 2/3)
                elif areag.collidepoint(event.pos):
                    square(0, 1/3, 2/3, 1)
                elif areah.collidepoint(event.pos):
                    square(1/3, 2/3, 2/3, 1)
                elif areai.collidepoint(event.pos):
                    square(2/3, 1, 2/3, 1)
            if event.button == 3:
                if areaa.collidepoint(event.pos):
                    circle(1/6, 1/6)
                elif areab.collidepoint(event.pos):
                    circle(1/2, 1/6)
                elif areac.collidepoint(event.pos):
                    circle(5/6, 1/6)
                elif aread.collidepoint(event.pos):
                    circle(1/6, 1/2)
                elif areae.collidepoint(event.pos):
                    circle(1/2, 1/2)
                elif areaf.collidepoint(event.pos):
                    circle(5/6, 1/2)
                elif areag.collidepoint(event.pos):
                    circle(1/6, 5/6)
                elif areah.collidepoint(event.pos):
                    circle(1/2, 5/6)
                elif areai.collidepoint(event.pos):
                    circle(5/6, 5/6)
    clock.tick(1)

pygame.quit()
quit()