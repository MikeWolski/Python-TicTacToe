import pygame
import time

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 102)

dis_width = 1200
dis_height = 1200

clock = pygame.time.Clock()

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Tic Tac Toe by Mike Wolski")

game_over = False

def circle():
    pygame.draw.circle(dis, black, pos, 180, 20)
    pygame.display.update()

def ex():
    pygame.draw.line(dis, black, pos, (560, 560), 20)
    pygame.display.update()

while not game_over:
    dis.fill(white)
    pygame.draw.rect(dis, black, [400, 0, 10, dis_height])
    pygame.draw.rect(dis, black, [800, 0, 10, dis_height])
    pygame.draw.rect(dis, black, [0, 400, dis_width, 10])
    pygame.draw.rect(dis, black, [0, 800, dis_width, 10])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(str(pos))
            ex()
    clock.tick(1)

pygame.quit()
quit()