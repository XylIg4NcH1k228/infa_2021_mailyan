import pygame
from pygame.draw import *
from numpy import pi

wood = (180, 150, 0)
wood2 = (170, 130, 0)
grass = (10, 150, 70)
sky = (0, 180, 220)
dog = (80, 80, 70)
wood_line = (80, 50, 30)
white = (255, 255, 255)

scr = pygame.display.set_mode((720, 1080))

rect(scr, sky, pygame.Rect((0, 0, 720, 200)))
rect(scr, wood, pygame.Rect((0, 200, 720, 440)))
rect(scr, grass, pygame.Rect((0, 640, 720, 460)))

for i in range(0, 720, 40):
    line(scr, wood_line, (i, 200), (i, 640))
line(scr, 0, (0, 640), (720, 640))

polygon(scr, wood2, ((555,600),(600,720),(480,700)))
polygon(scr, 0, ((555,600),(600,720),(480,700)), width=1)
polygon(scr, wood2, ((555,600),(600,720),(640,700),(595,580)))
polygon(scr, 0, ((555,600),(600,720),(640,700),(595,580)), width=1)
polygon(scr, wood, ((480,700),(600,720),(600,885),(480,825)))
polygon(scr, 0, ((480,700),(600,720),(600,885),(480,825)), width=2)
polygon(scr, wood, ((600,885),(600,720),(640,700),(640,815)))
polygon(scr, 0, ((600,885),(600,720),(640,700),(640,815)),width=2)

ellipse(scr, 0, pygame.Rect(500,735,70,90))

ellipse(scr, 0, pygame.Rect(495,810,35,10), width=2)
ellipse(scr, 0, pygame.Rect(490,815,15,18), width=2)
ellipse(scr, 0, pygame.Rect(470,820,30,25), width=2)
ellipse(scr, 0, pygame.Rect(450,830,30,15), width=2)
ellipse(scr, 0, pygame.Rect(443,837,15,15), width=2)
ellipse(scr, 0, pygame.Rect(400,845,50,10), width=2)
ellipse(scr, 0, pygame.Rect(375,847,35,10), width=2)
ellipse(scr, 0, pygame.Rect(350,846,35,5), width=2)
ellipse(scr, 0, pygame.Rect(340,835,20,25), width=2)
ellipse(scr, 0, pygame.Rect(325,843,25,15), width=2)

ellipse(scr, dog, pygame.Rect(50,820,170,70)) #body
ellipse(scr, dog, pygame.Rect(180,805,90,50)) #hips
ellipse(scr, dog, pygame.Rect(175,803,60,70)) #left hip
ellipse(scr, dog, pygame.Rect(203,855,15,50)) #left back leg
ellipse(scr, dog, pygame.Rect(183,900,30,17)) #left back foot
ellipse(scr, dog, pygame.Rect(230,825,55,65)) #right hip
ellipse(scr, dog, pygame.Rect(272,878,15,50)) #right back leg
ellipse(scr, dog, pygame.Rect(252,923,30,17)) #right back foot
ellipse(scr, dog, pygame.Rect(40,840,45,100)) #left front leg
ellipse(scr, dog, pygame.Rect(30,930,48,22)) #left front foot
ellipse(scr, dog, pygame.Rect(120,850,45,100)) #right front leg
ellipse(scr, dog, pygame.Rect(110,940,48,22)) #right front foot

rect(scr, dog, pygame.Rect(55,775,100,100)) #face base
rect(scr, 0, pygame.Rect(55,775,100,100), width=3)
ellipse(scr, dog, pygame.Rect(40,775,30,40)) #ears
ellipse(scr, 0, pygame.Rect(40,775,30,40), width=2)
ellipse(scr, dog, pygame.Rect(140,775,30,40))
ellipse(scr, 0, pygame.Rect(140,775,30,40), width=2)
ellipse(scr, white, pygame.Rect(75,815,20,8)) #eyes
ellipse(scr, 0, pygame.Rect(80,815,10,8))
ellipse(scr, 0, pygame.Rect(75,815,20,8), width=1)
ellipse(scr, white, pygame.Rect(115,815,20,8))
ellipse(scr, 0, pygame.Rect(120,815,10,8))
ellipse(scr, 0, pygame.Rect(115,815,20,8), width=1)
arc(scr, 0, pygame.Rect(75,840,60,40), 2*pi/3, pi, width=2) #mouth
arc(scr, 0, pygame.Rect(75,840,60,40), 0, pi/3, width=2)
line(scr, 0, (90,842), (120,842), 2)
polygon(scr, white, ((82,847),(86,843),(84,837))) #teeth
polygon(scr, 0, ((82,847),(86,843),(84,837)), width=1)
polygon(scr, white, ((128,847),(124,843),(126,837)))
polygon(scr, 0, ((128,847),(124,843),(126,837)), width=1)

pygame.init()

pygame.display.update()
clock = pygame.time.Clock()

quit = False
while not(quit):
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

pygame.quit()
