from tkinter.messagebox import askretrycancel
import pygame
import time

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 102)

dis_width = 800
dis_height = 800

clock = pygame.time.Clock()

dis = pygame.display.set_mode((dis_width, dis_height), pygame.RESIZABLE)
pygame.display.set_caption("Tic Tac Toe by Mike Wolski")

game_over = False

def circle():
    pygame.draw.circle(dis, black, pos, 180, 20)
    pygame.display.update()

areaa = pygame.Rect(dis_width*0, dis_height*0, dis_width/3, dis_height/3)
areab = pygame.Rect(dis_width/3, dis_width*0, dis_width/3, dis_height/3)
areac = pygame.Rect(dis_width*2/3, dis_width*0, dis_width/3, dis_height/3)
aread = pygame.Rect(dis_width*0, dis_height/3, dis_width/3, dis_height/3)
areae = pygame.Rect(dis_width/3, dis_height/3, dis_width/3, dis_height/3)
areaf = pygame.Rect(dis_width*2/3, dis_height/3, dis_width/3, dis_height/3)
areag = pygame.Rect(dis_width*0, dis_height*2/3, dis_width/3, dis_height/3)
areah = pygame.Rect(dis_width/3, dis_height*2/3, dis_width/3, dis_height/3)
areai = pygame.Rect(dis_width*2/3, dis_height*2/3, dis_width/3, dis_height/3)

def squarea():
    pygame.draw.line(dis, black, [dis_width*0, dis_height*0], [dis_width/3, dis_height/3], 10)
    pygame.draw.line(dis, black, [dis_width*0, dis_height/3], [dis_width/3, dis_height*0], 10)
    #pygame.draw.rect(dis, black, [dis_width*1/6, dis_height*0, 10, dis_height*1/3])
    #pygame.draw.rect(dis, black, [dis_width*0, dis_height*1/6, dis_width*1/3, 10])
    pygame.display.update()
def squareb():
    pygame.draw.rect(dis, black, [dis_width*1/2, dis_height*0, 10, dis_height*1/3])
    pygame.draw.rect(dis, black, [dis_width*1/3, dis_height*1/6, dis_width*1/3, 10])
    pygame.display.update()
def squarec():
    pygame.draw.rect(dis, black, [dis_width*5/6, dis_height*0, 10, dis_height*1/3])
    pygame.draw.rect(dis, black, [dis_width*2/3, dis_height*1/6, dis_width*1/3, 10])
    pygame.display.update()
def squared():
    pygame.draw.rect(dis, black, [dis_width/6, dis_height/3, 10, dis_height*1/3])
    pygame.draw.rect(dis, black, [dis_width*0, dis_height/2, dis_width*1/3, 10])
    pygame.display.update()
def squaree():
    pygame.draw.rect(dis, black, [dis_width/2, dis_height/3, 10, dis_height*1/3])
    pygame.draw.rect(dis, black, [dis_width/3, dis_height/2, dis_width*1/3, 10])
    pygame.display.update()
def squaref():
    pygame.draw.rect(dis, black, [dis_width*5/6, dis_height*1/3, 10, dis_height*1/3])
    pygame.draw.rect(dis, black, [dis_width*2/3, dis_height*1/2, dis_width*1/3, 10])
    pygame.display.update()
def squareg():
    pygame.draw.rect(dis, black, [dis_width*1/6, dis_height*2/3, 10, dis_height*1/3])
    pygame.draw.rect(dis, black, [dis_width*0, dis_height*5/6, dis_width*1/3, 10])
    pygame.display.update()
def squareh():
    pygame.draw.rect(dis, black, [dis_width*1/2, dis_height*2/3, 10, dis_height*1/3])
    pygame.draw.rect(dis, black, [dis_width*1/3, dis_height*5/6, dis_width*1/3, 10])
    pygame.display.update()
def squarei():
    pygame.draw.rect(dis, black, [dis_width*5/6, dis_height*2/3, 10, dis_height*1/3])
    pygame.draw.rect(dis, black, [dis_width*2/3, dis_height*5/6, dis_width*1/3, 10])
    pygame.display.update()


while not game_over:
    dis.fill(white)
    pygame.draw.rect(dis, black, [dis_width/3, 0, 10, dis_height])
    pygame.draw.rect(dis, black, [dis_width*2/3, 0, 10, dis_height])
    pygame.draw.rect(dis, black, [0, dis_height/3, dis_width, 10])
    pygame.draw.rect(dis, black, [0, dis_height*2/3, dis_width, 10])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if areaa.collidepoint(event.pos):
                    pos = pygame.mouse.get_pos()
                    print(str(pos))
                    squarea()
                elif areab.collidepoint(event.pos):
                    pos = pygame.mouse.get_pos()
                    print(str(pos))
                    squareb()
                elif areac.collidepoint(event.pos):
                    pos = pygame.mouse.get_pos()
                    print(str(pos))
                    squarec()
                elif aread.collidepoint(event.pos):
                    pos = pygame.mouse.get_pos()
                    print(str(pos))
                    squared()
                elif areae.collidepoint(event.pos):
                    pos = pygame.mouse.get_pos()
                    print(str(pos))
                    squaree()
                elif areaf.collidepoint(event.pos):
                    pos = pygame.mouse.get_pos()
                    print(str(pos))
                    squaref()
                elif areag.collidepoint(event.pos):
                    pos = pygame.mouse.get_pos()
                    print(str(pos))
                    squareg()
                elif areah.collidepoint(event.pos):
                    pos = pygame.mouse.get_pos()
                    print(str(pos))
                    squareh()
                elif areai.collidepoint(event.pos):
                    pos = pygame.mouse.get_pos()
                    print(str(pos))
                    squarei()
    clock.tick(1)

pygame.quit()
quit()