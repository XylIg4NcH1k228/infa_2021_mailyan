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

def draw_dog(scr, x, y, t=1):
    ellipse(scr, dog, pygame.Rect(x + 20*t,y + 45*t,170*t,70*t)) #body
    ellipse(scr, dog, pygame.Rect(x + 150*t,y + 30*t,90*t,50*t)) #hips
    ellipse(scr, dog, pygame.Rect(x + 145*t,y + 28*t,60*t,70*t)) #left hip
    ellipse(scr, dog, pygame.Rect(x + 173*t,y + 80*t,15*t,50*t)) #left back leg
    ellipse(scr, dog, pygame.Rect(x + 153*t,y + 125*t,30*t,17*t)) #left back foot
    ellipse(scr, dog, pygame.Rect(x + 200*t,y + 50*t,55*t,65*t)) #right hip
    ellipse(scr, dog, pygame.Rect(x + 242*t,y + 103*t,15*t,50*t)) #right back leg
    ellipse(scr, dog, pygame.Rect(x + 222*t,y + 148*t,30*t,17*t)) #right back foot
    ellipse(scr, dog, pygame.Rect(x + 10*t,y + 65*t,45*t,100*t)) #left front leg
    ellipse(scr, dog, pygame.Rect(x,y + 155*t,48*t,22*t)) #left front foot
    ellipse(scr, dog, pygame.Rect(x + 90*t,y + 75*t,45*t,100*t)) #right front leg
    ellipse(scr, dog, pygame.Rect(x + 80*t,y + 165*t,48*t,22*t)) #right front foot

    rect(scr, dog, pygame.Rect(x + 25*t,y,100*t,100*t)) #face base
    rect(scr, 0, pygame.Rect(x + 25*t,y,100*t,100*t), width=3)
    ellipse(scr, dog, pygame.Rect(x + 10*t,y,30*t,40*t)) #ears
    ellipse(scr, 0, pygame.Rect(x + 10*t,y,30*t,40*t), width=2)
    ellipse(scr, dog, pygame.Rect(x + 110*t,y,30*t,40*t))
    ellipse(scr, 0, pygame.Rect(x + 110*t,y,30*t,40*t), width=2)
    ellipse(scr, white, pygame.Rect(x + 45*t,y + 40*t,20*t,8*t)) #eyes
    ellipse(scr, 0, pygame.Rect(x + 50*t,y + 40*t,10*t,8*t))
    ellipse(scr, 0, pygame.Rect(x + 45*t,y + 40*t,20*t,8*t), width=1)
    ellipse(scr, white, pygame.Rect(x + 85*t,y + 40*t,20*t,8*t))
    ellipse(scr, 0, pygame.Rect(x + 90*t,y + 40*t,10*t,8*t))
    ellipse(scr, 0, pygame.Rect(x + 85*t,y + 40*t,20*t,8*t), width=1)
    arc(scr, 0, pygame.Rect(x + 45*t,y + 65*t,60*t,40*t), 2*pi/3, pi, width=2) #mouth
    arc(scr, 0, pygame.Rect(x + 45*t,y + 65*t,60*t,40*t), 0, pi/3, width=2)
    line(scr, 0, (x + 60*t,y + 67*t), (x + 90*t,y + 67*t), 2)
    polygon(scr, white, ((x + 52*t,y + 72*t),(x + 56*t,y + 68*t),(x + 54*t,y + 62*t))) #teeth
    polygon(scr, 0, ((x + 52*t,y + 72*t),(x + 56*t,y + 68*t),(x + 54*t,y + 62*t)), width=1)
    polygon(scr, white, ((x + 98*t,y + 72*t),(x + 94*t,y + 68*t),(x + 96*t,y + 62*t)))
    polygon(scr, 0, ((x + 98*t,y + 72*t),(x + 94*t,y + 68*t),(x + 96*t,y + 62*t)), width=1) 
    
def draw_fence(scr, x, y, t=1):
    rect(scr, wood, pygame.Rect(x, y, 720*t, 440*t))
    for i in range(19):
        line(scr, wood_line, (x + i*40*t, y), (x + i*40*t, y + 440*t))
    line(scr, 0, (x, y), (x + 720*t, y))
    line(scr, 0, (x, y + 440*t), (x+ 720*t, y + 440*t))

scr = pygame.display.set_mode((720, 1080))

rect(scr, sky, pygame.Rect((0, 0, 720, 540)))
rect(scr, grass, pygame.Rect((0, 540, 720, 540)))

draw_fence(scr, 100, 20, .9)
draw_fence(scr, 0, 300, .6)
draw_fence(scr, 400, 350, .7)
draw_fence(scr, 0, 450, .5)

dog1 = pygame.Surface((300, 200))
dog1.set_colorkey((0, 255, 0))
dog1.fill((0, 255, 0))
draw_dog(dog1, 0, 0, t=.75)

scr.blit(pygame.transform.flip(dog1, True, False), (450, 600))

draw_dog(scr, 30, 600)

dog2 = pygame.Surface((300, 200))
dog2.set_colorkey((0, 255, 0))
dog2.fill((0, 255, 0))
draw_dog(dog2, 0, 0, t=.9)

scr.blit(pygame.transform.flip(dog2, True, False), (40, 820))

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

draw_dog(scr, 430, 700, 3)

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
