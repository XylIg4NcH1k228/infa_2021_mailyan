import pygame
from pygame.draw import *
import keyboard
from random import randint
import numpy as np
pygame.init()

FPS = 30
# screen size
X = 1200
Y = 700
screen = pygame.display.set_mode((X, Y))

#start button
start_font_size = 150

#enter name screen
enter_name_size = 100
ok_x_cor, ok_y_cor = (90/100*X, 60/100*Y)
ok_size = 50

#for name
alphabet = []
with open('words.txt') as g:
    for element in g.read():
        alphabet.append('K_'+element)
        
#game_over
game_over_size = 180
menu_button_size = 100
restart_button_size = 100
Points_size = 100

#enter name screen

enter_button_size = 100
#coordinates of the center of buttons
start_x_cor = X/2
start_y_cor = Y/2

menu_y_cor = 80/100*Y
#play-field
RECT = left_wall, up_wall, right_wall, down_wall = (250/1200*X, 10/700*Y, 1190/1200*X, 690/700*Y)
# colors
WHITE = (255, 255, 255)
GOLD = (255,215,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, WHITE, GREEN, MAGENTA, CYAN]

#counter constants
counter_font_size = 32
counter_top_left_corner_x, counter_top_left_corner_y = counter_top_left_corner = (10/1200*X,10/700*Y)

#game pars
Number_of_balls = 2
Number_of_small_balls = 3
Supa_ball_radius = 70
Small_ball_radius = 15

Small_ball_time = 2000

def new_ball_pars():
    '''gives parameters of a new ball
return: x, y, r, Vx, Vy, color
x - 1 cor of a ball
y - 2 cor of a ball
r - radius
Vx - velocity in x direction
Vy - velocity in y direction
color - color of a ball
'''
    x = randint(round(340/1200*X), round(1100/1200*X))
    y = randint(round(140/700*Y), round(600/700*Y))
    r = randint(15, 50)
    Vx = randint(-10, 10)
    Vy = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    return x, y, r, Vx, Vy, color 

def counter(screen, points, misses, x_cor, y_cor, font_size):
    """
    displays counter of points and misses on the screen
    :par points: number of points
    :par misses: number of points
    :par x_cor: 1 coordinate of top left corner of counter
    :par y_cor: 2 coordinate of top left corner of counter
    :par font_size: font size
    """
    rect(screen, BLUE, (0, 0, left_wall, down_wall), 0)
    points_counter(screen, points, x_cor, y_cor, font_size)
    misses_counter(screen, misses, x_cor, y_cor+40, font_size)
    
def points_counter(screen, points, x_cor, y_cor, font_size):
    """
    displays counter of points at the right top corner of the screen
    :par points: number of points
    :par x_cor: 1 coordinate of top left corner of counter
    :par y_cor: 2 coordinate of top left corner of counter
    :par font_size: font size
    """
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render('Bucks: '+str(points)+'$', True, GREEN, BLUE)
    textRect = text.get_rect()
    textRect.topleft = (x_cor, y_cor)
    screen.blit(text, textRect)
    
def misses_counter(screen, misses, x_cor, y_cor, font_size):
    """
    displays counter of points at the right top corner of the screen
    :par misses: number of points
    :par x_cor: 1 coordinate of top left corner of counter
    :par y_cor: 2 coordinate of top left corner of counter
    :par font_size: font size
    """
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render('misses: '+str(misses), True, GREEN, BLUE)
    textRect = text.get_rect()
    textRect.topleft = (x_cor, y_cor)
    screen.blit(text, textRect)
    
def move_ball(screen, Color, x_cor, y_cor, r, vx, vy, rect):
    """ moves ball from position x_cor, y_cor to position x_cor+vx, y_cor+vy
        checks if ball hitted an edge of the play-field and changes its velocity
       :par screen: where you want to draw it
       :par x_cor: initial x coordinate of a ball
       :par y_cor: initial y coordinate of a ball
       :par vx: x - shift
       :par vy: y - shift
       :par color: color of a ball
        returns: x_cor, y_cor, vx, vy
        new coordinates and velocity
    """
    if (x_cor < rect[0]+r) or x_cor > rect[2]-r:
        vx = -vx
    if y_cor < rect[1]+r or y_cor > rect[3]-r:
        vy = -vy
    
    
    circle(screen, BLACK,(x_cor, y_cor), r) 
    circle(screen, Color, (x_cor+vx, y_cor+vy), r)

    x_cor += vx
    y_cor += vy
    return x_cor, y_cor, vx, vy
        
def supa_ball(screen):
    """ draws supa ball on the screen
    gives parameters of a new supa_ball
    :par screen: display
    return: color, x, y, r, Vx, Vy
    x - 1 cor of a ball
    y - 2 cor of a ball
    r - radius
    Vx - velocity in x direction
    Vy - velocity in y direction
    color - color of a ball
    """
    x = randint(round(340/1200*X), round(1100/1200*X))
    y = randint(round(140/700*Y), round(600/700*Y))
    r = Supa_ball_radius
    Vx = randint(-10, 10)
    Vy = randint(-10, 10)
    circle(screen, GOLD, (x, y), r)
    return [GOLD, x, y, r, Vx, Vy]
def small_ball(screen, x_cor, y_cor, r):
    """draws small_ball of the screen
    gives parameters of a new small_ball
    :par screen: display
    :par x_cor: 1 coordinate of supa_ball which produced this small ball
    :par y_cor: 2 coordinate of supa_ball which produced this small ball
    :par r: radius of supa_ball which produced this small ball
    return: color, x, y, r, Vx, Vy
    x - 1 cor of a ball
    y - 2 cor of a ball
    r - radius
    Vx - velocity in x direction
    Vy - velocity in y direction
    color - color of a ball
    """
    r = Small_ball_radius
    Vx = randint(-10, 10)
    Vy = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x_cor, y_cor), r)
    return [color, x_cor, y_cor, r, Vx, Vy]    

def menu_screen(screen):
    """
    draws menu screen
    :par screen: display
    """
    global Start_button_width, Start_button_length, Score_button_width, Score_button_length  
    Start_button_width, Start_button_length = button('Start', GREEN, BLUE, start_x_cor, start_y_cor, start_font_size)
    button('Menu', RED, WHITE, X/2, Y/5, 100)
    Score_button_width, Score_button_length = button('Score board', GREEN, BLUE, start_x_cor, start_y_cor + Start_button_length + 5, 100)
    

def button(name, name_color, background_color, x, y, font_size):
    """
    draws button 'name' with center in (x,y) cor
    returns: width and length of button
    """

    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(name, True, name_color, background_color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
    return font.size(name)

def button_hit(x_tap, y_tap, x_button, y_button, button_width, button_length):
    """
    checks if (x_tap, y_tap) is in rect (x_button, y_button, button_width, button_length) tapped on button
    :par x_tap: x cor of tap
    :par y_tap: y cor of tap
    :par x_button: x cor of the center of button
    :par y_button: y cor of the center of button
    returs: True or False
    """
    if abs(x_tap - x_button) < button_width/2 and abs(y_tap - y_button) < button_length/2:
        return True
    else: return False

def game_over(screen, Points):
    """
    draws game_over screen
    :par screen: display
    """
    global menu_button_width, menu_button_length, restart_button_width, restart_button_length
    screen.fill(BLACK)
    game_over_width, game_over_length = button('Game over', RED, WHITE, X/2, Y/5, game_over_size)
    if Points != 1:
        button('score: '+str(Points)+'$', RED, WHITE, X/2, Y*45/100, Points_size)
    else: button('You scored: '+str(Points)+' Point', RED, WHITE, X/2, Y*45/100, Points_size)
    menu_button_width, menu_button_length = button('Menu', GREEN, BLUE, X/2, menu_y_cor, menu_button_size)
    restart_button_width, restart_button_length = button('Restart', GREEN, BLUE, X/2, menu_y_cor - menu_button_length - 5, restart_button_size)
    pygame.display.update()

def enter_name(screen, name):
    """
    draws enter your name screen with your name
    """
    global ok_length, ok_width
    screen.fill(BLACK)
    button('Enter your name', RED, WHITE, X/2, Y/5, enter_name_size)
    ok_width, ok_length = button('OK', GREEN, BLUE, ok_x_cor, ok_y_cor, ok_size)
    button(name, GREEN, BLUE, X/2, Y/2, 50)

def score_board(names, last, best, first_place):
    global G1, G2
    rect(screen, BLUE, (X/40,0, 38/40*X, Y), 0)
    o = button('Score board', RED, WHITE, X/2, Y/5, 100)
    G1, G2 = button('menu', GOLD, WHITE, X/40+100/1200*X, 100/700*Y, 50)
    i = first_place - 1
    while i < len(names) and i <= 5+first_place:
        F = button(str(i+1)+') ' + names[i]+':Last - $'+str(last[i])+'|Best - $'+str(best[i]), RED, WHITE, X/2, Y/5+o[1]+100*(i - first_place+1), 50)
        rect(screen, BLUE, (X/2 - F[0]/2, Y/5+o[1]+100*(i - first_place+1) - F[1]/2, F[0]+5, F[1]+5))
        button(str(i+1)+') ' + names[i]+':Last - $'+str(last[i])+'|Best - $'+str(best[i]), RED, WHITE, X/40 + F[0]/2, Y/5+o[1]+100*(i - first_place+1), 50)    
        i += 1
Game_start = True   
finished = False
Enter_name = False

pygame.display.update()
while not finished:
    clock = pygame.time.Clock()

    names = []
    best = []
    last = []
    with open('score_board.txt', 'r') as g:
        for line in g.readlines():
            if line != '\n':
                a = line.split(':')
                names.append(a[0])
                b = a[1].split('|')
                last.append(int(b[0][8:len(b[0])]))
                best.append(int(b[1][8:len(b[1])]))
                
    with open('score_board.txt', 'w') as g:
        u = 0
    for j in range(len(names)-1):
        for i in range(0, len(names)-1-j):
            if best[i] < best[i+1]:
                m = best[i]
                best[i] = best[i+1]
                best[i+1] = m

            
                m = names[i]
                names[i] = names[i+1]
                names[i+1] = m

            
                m = last[i]
                last[i] = last[i+1]
                last[i+1] = m
            
    #lists for parameters of balls
    x = [1 for i in range(Number_of_balls)]
    y = [1 for i in range(Number_of_balls)]
    r = [1 for i in range(Number_of_balls)]
    Vx = [1 for i in range(Number_of_balls)]
    Vy = [1 for i in range(Number_of_balls)]
    color = [1 for i in range(Number_of_balls)]

    #super ball list of parameters
    supa_ball_pars = []
    #small ball list of parameters
    small_balls_pars = []

    #timers for smallballs
    events = []
    #initial balls
    for i in range(Number_of_balls):
        x[i], y[i], r[i], Vx[i], Vy[i], color[i] = new_ball_pars()
    # displaying menu screen
    screen.fill(BLACK)
    menu_screen(screen)



    Points = 0
    Misses = 0


    pygame.display.update()
    supa_chance = randint(0,1)


    #game menu
    while Game_start:
        clock.tick(FPS)

        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if button_hit(x_mouse, y_mouse, start_x_cor, start_y_cor, Start_button_width, Start_button_length) == True:
            button('Start', BLUE, GREEN, X/2, Y/2, start_font_size)

            
        if button_hit(x_mouse, y_mouse, start_x_cor, start_y_cor + Start_button_length + 5, Score_button_width, Score_button_length) == True:
            button('Score board', BLUE, GREEN, start_x_cor, start_y_cor + Start_button_length + 5, 100)

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                Game_start = False
                Game_play = False
                Game_over = False
                Score_board = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #checking if player tapped on start button
                
                if button_hit(event.pos[0], event.pos[1], start_x_cor, start_y_cor, Start_button_width, Start_button_length) == True:
                    Game_start = False
                    Game_play = True
                    Enter_name = True
                    Score_board = False
                #checking if player tapped on score board button
                    
                if button_hit(event.pos[0], event.pos[1],start_x_cor, start_y_cor + Start_button_length + 5, Score_button_width, Score_button_length) == True:
                    Game_start = False
                    Game_play = False
                    Enter_name = False
                    Score_board = True
                    
        
        pygame.display.update()
        button('Start', GREEN, BLUE, X/2, Y/2, start_font_size)
        button('Score board', GREEN, BLUE, start_x_cor, start_y_cor + Start_button_length + 5, 100)
    screen.fill(BLACK)
    first_place = 1

    score_board(names, last, best, first_place)
    while Score_board == True:
        score_board(names, last, best, first_place)
        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if button_hit(x_mouse, y_mouse, X/40+100/1200*X, 100/700*Y, G1, G2) == True:
            button('menu', WHITE, GOLD, X/40+100/1200*X, 100/700*Y, 50)

            
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                Game_start = False
                Game_play = False
                Game_over = False
                Score_board = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if first_place != 1:
                        first_place -= 1
                if event.key == pygame.K_DOWN:
                    if first_place < len(names):
                        first_place += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_hit(event.pos[0], event.pos[1], X/40+100/1200*X, 100/700*Y, G1, G2) == True:
                    Game_start = True
                    Game_play = False
                    Game_over = False
                    Score_board = False
        button('menu', GOLD, WHITE, X/40+100/1200*X, 100/700*Y, 50)
        screen.fill(BLACK)
                
    screen.fill(BLACK)
    #entering name
    Name = ''
    enter_name(screen, Name)

    
    while Enter_name:
        clock.tick(FPS)
            
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if button_hit(x_mouse, y_mouse, ok_x_cor, ok_y_cor, ok_width, ok_length) == True:
            button('OK', BLUE, GREEN, ok_x_cor, ok_y_cor, ok_size)
            
        
        pygame.display.update()
        enter_name(screen, Name)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                finished = True
                Enter_name = False
                Game_play = False
                Game_over = False
            elif event.type == pygame.KEYDOWN:
                for i in alphabet:
                    if eval('pygame.'+i) == event.key:
                        Name += i[2]
                if event.key == pygame.K_BACKSPACE:
                    Name = Name[:len(Name)-1]
                if event.key == pygame.K_SPACE:
                    Name += ' '
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_hit(event.pos[0], event.pos[1], ok_x_cor, ok_y_cor, ok_width, ok_length) == True:
                    Enter_name = False
                    Game_play = True
        

                    
                
                        
    screen.fill(BLACK)

    
    #game-play
    while Game_play:
        clock.tick(FPS)

            
        for event in pygame.event.get():
     
            if event.type == pygame.QUIT:
                finished = True
                Game_play = False
                Game_over = False

                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # condition of game over
                if Misses >= 3:
                    Game_play = False
                    Game_over = True
                Misses += 1
                
                #cheking simple balls
                for i in range(Number_of_balls):
                    if (event.pos[0] - x[i])**2 + (event.pos[1] - y[i])**2 <= r[i]**2: #checking if we've hitted the ball
                        pygame.mixer.music.load('11817-gachi-woo.mp3')
                        pygame.mixer.music.play()
                        Points += 30
                        Misses -= 1
                        screen.fill(BLACK)
                        #changing the ball we've hitted
                        x[i], y[i], r[i], Vx[i], Vy[i], color[i] = new_ball_pars()
                        #chance of getting new supa ball (33%)
                        supa_chance = randint(0,2)
                        
                        if supa_chance == 1:
                            supa_ball_pars.append(supa_ball(screen)) #adding new supa ball in list


                i = 0            
                while i < len(supa_ball_pars):
                    if (event.pos[0] - supa_ball_pars[i][1])**2 + (event.pos[1] - supa_ball_pars[i][2])**2 <= supa_ball_pars[i][3]**2:      #Cheking if we've hitted supa ball number i
                        
                        pygame.mixer.music.load('41077-gachi-billy-spank.mp3')
                        pygame.mixer.music.play()
                        Misses -= 1
                        #adding Number_of_small_balls in small_balls_pars
                        small_balls_pars.append([small_ball(screen, supa_ball_pars[i][1], supa_ball_pars[i][2], supa_ball_pars[i][3]) for k in range(Number_of_small_balls)] )

                        #making timer for this small balls
                        events.append(pygame.USEREVENT+len(events))
                        pygame.time.set_timer(events[len(events)-1], Small_ball_time, 1)

                        #deleting supa ball
                        circle(screen, BLACK, (supa_ball_pars[i][1], supa_ball_pars[i][2]), supa_ball_pars[i][3])
                        supa_ball_pars.pop(i)
                        i -= 1
                    i += 1
                    
                    #Checking about hitting small balls
                k = 0
                while k < len(small_balls_pars):

                    j = 0   
                    while j < len(small_balls_pars[k]):
                        #Cheking if we've hitted small ball number j, if so, delete this ball
                        if (event.pos[0] - small_balls_pars[k][j][1])**2 + (event.pos[1] - small_balls_pars[k][j][2])**2 <= small_balls_pars[k][j][3]**2:
                            Misses -= 1
                            circle(screen, BLACK, (small_balls_pars[k][j][1], small_balls_pars[k][j][2]), small_balls_pars[k][j][3])
                            small_balls_pars[k].pop(j)
                            j -= 1
                        j += 1

                    # adding points if player hitted all small balls from one supa ball
                    if len(small_balls_pars[k]) == 0:
                        pygame.mixer.music.load('15835-300.mp3')
                        pygame.mixer.music.play()
                        Points += 300
                        small_balls_pars.pop(k)
                        events.pop(k)
                        k -= 1

                    k += 1
            
            i = 0
            #checking timer_events
            while i < len(events):       
                if event.type == events[i]:
                    # erasing each ball associated with this event
                    for j in range(len(small_balls_pars[i])):
                        circle(screen, BLACK, (small_balls_pars[i][j][1], small_balls_pars[i][j][2]), small_balls_pars[i][j][3])
                    # adding points if player hitted all small balls from one supa ball
                    small_balls_pars.pop(i)
                    events.pop(i)
                    i -= 1
                i += 1
                         
        # shifting each ball
        for i in range(Number_of_balls):
            x[i] ,y[i], Vx[i], Vy[i] =  move_ball(screen, color[i], x[i], y[i], r[i], Vx[i], Vy[i], RECT)
                           
        # shifting supa balls and small balls

        #moving each supa ball                       
        for i in range(len(supa_ball_pars)):

            supa_ball_pars[i][1], supa_ball_pars[i][2], supa_ball_pars[i][4], supa_ball_pars[i][5] =  move_ball(screen, supa_ball_pars[i][0], supa_ball_pars[i][1], supa_ball_pars[i][2], supa_ball_pars[i][3], supa_ball_pars[i][4], supa_ball_pars[i][5], RECT)

        #moving each small ball        
        for i in range(len(small_balls_pars)):
            for j in range(len(small_balls_pars[i])):

                small_balls_pars[i][j][1], small_balls_pars[i][j][2], small_balls_pars[i][j][4], small_balls_pars[i][j][5] =  move_ball(screen, COLORS[randint(0, 5)], small_balls_pars[i][j][1], small_balls_pars[i][j][2], small_balls_pars[i][j][3], small_balls_pars[i][j][4], small_balls_pars[i][j][5], RECT)


        #  highlighting play-field
        rect(screen, WHITE, (left_wall, up_wall, right_wall-left_wall, down_wall-up_wall), width = 5)
            
        #Refreshing screen with new points
        
        counter(screen, Points, Misses, counter_top_left_corner_x, counter_top_left_corner_y, counter_font_size)
        pygame.display.update()


    k = 0
    #displaying game_over screen
    game_over(screen, Points)
    #game-over
    while Game_over:
        clock.tick(FPS)
        #writing score in scoreboard
        if k == 0:
            l = 1
            for i in range(len(names)):
                if Name == names[i]:
                    l = 0
                    last[i] = Points
                    if Points > best[i]:
                        best[i] = Points

            if l == 1:
                names.append(Name)
                best.append(Points)
                last.append(Points)

            k = 1
        
        #changing buttons if mouse pos is located on them
        x_mouse, y_mouse = pygame.mouse.get_pos()

        if button_hit(x_mouse, y_mouse, X/2, menu_y_cor, menu_button_width, menu_button_length) == True:
            button('Menu', BLUE, GREEN, X/2, menu_y_cor, menu_button_size)
        elif button_hit(x_mouse, y_mouse, X/2, menu_y_cor - menu_button_length - 5, restart_button_width, restart_button_length) == True:
            button('Restart', BLUE, GREEN, X/2, menu_y_cor - menu_button_length - 5, restart_button_size)

        pygame.display.update()
        button('Restart', GREEN, BLUE, X/2, menu_y_cor - menu_button_length - 5, restart_button_size)
        button('Menu', GREEN, BLUE, X/2, menu_y_cor, menu_button_size)

        
        for event in pygame.event.get():

                
            if event.type == pygame.QUIT:
                Game_over = False
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #checking if player tapped on menu button
                if button_hit(event.pos[0], event.pos[1], X/2, menu_y_cor, menu_button_width, menu_button_length) == True:
                    Game_over = False
                    Game_play = False
                    Game_start = True
                    # checking if player tapped on restart button
                elif button_hit(event.pos[0], event.pos[1], X/2, menu_y_cor - menu_button_length - 5, restart_button_width, restart_button_length) == True:
                    Game_over = False
                    Game_play = True
                    Game_start = False
    with open('score_board.txt', 'a') as g:
        for i in range(len(names)):
            g.write(names[i]+':Last - $'+str(last[i])+'|Best - $'+str(best[i])+ '\n')    
                
               
pygame.quit()
