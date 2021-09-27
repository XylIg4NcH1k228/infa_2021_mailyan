import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

polygon(screen, (150, 150, 150), [(0, 0), (400, 0), (400, 400), (0, 400)])
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
polygon(screen, (0, 0, 0), [(150, 270), (150, 250), (250, 250), (250, 270)])
circle(screen, (255, 0, 0), (250, 180), 17)
circle(screen, (0, 0, 0), (250, 180), 17, 1)
circle(screen, (0, 0, 0), (250, 180), 9)
polygon(screen, (0, 0, 0), [(220, 175), (215, 165),(287, 130),(290, 140)])
circle(screen, (255, 0, 0), (150, 180), 20)
circle(screen, (0, 0, 0), (150, 180), 20, 1)
circle(screen, (0, 0, 0), (150, 180), 9)
polygon(screen, (0, 0, 0), [(180, 175), (185, 165), (100, 120), (95, 130)]) 
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
