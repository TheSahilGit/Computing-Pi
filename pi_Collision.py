import pygame
import numpy as np
from fractions import Fraction

pygame.init()

display_width = 900
display_height = 650

black = [0, 0, 0]
white = [255, 255, 255]

display_surface = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Pi Collision")


def box(x, y, s):
    pygame.draw.rect(display_surface, white, [x, y - s, s, s])


def collisionVel(m1, m2, u1, u2):
    totalMass = m1 + m2
    v1 = float((m1 - m2) / totalMass) * u1 + float(2 * m2 / totalMass) * u2
    v2 = float(2 * m1 / totalMass) * u1 + float((m2 - m1) / totalMass) * u2
    return v1, v2


def collisonShow(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render(("Pi= " + str(count)), True, white)
    display_surface.blit(text, (0, 0))


digit = 1

massSmall = 1
massBig = 100 ** digit

widthSmall = 25
widthBig = 50

velocitySmall = 0
velocityBig = -5

xsm = display_width / 4.
xbg = display_height / 2.

count = 0

game_exit = False
while not game_exit:
    display_surface.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    xsm += velocitySmall
    xbg += velocityBig

    newVelBig, newVelSmall = collisionVel(massBig, massSmall, velocityBig, velocitySmall)

    if xbg <= 0:
        velocityBig *= -1
        count += 1
    if xsm <= 0:
        velocitySmall *= -1
        count += 1

    if xbg <= xsm + widthSmall or xsm + widthSmall >= xbg:
        velocityBig = newVelBig
        velocitySmall = newVelSmall
        count += 1

    box(xsm, display_height / 1.5, widthSmall)
    box(xbg, display_height / 1.5, widthBig)
    pi=count/10**digit
    collisonShow(pi)

    pygame.display.update()
    clock.tick(200)
