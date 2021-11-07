import math
from random import choice, randint

import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 1200
HEIGHT = 800
game_over_size = 180
menu_button_size = 100
restart_button_size = 100
Points_size = 100
menu_y_cor = 80 / 100 * HEIGHT


class Ball:

    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(BLACK)
        self.live = 1
        self.g = 1
        self.time = 0

    def move(self, obj, gun):
        """Переместить мяч по прошествии единицы времени.
        учитывая столкновения с боссом и пушкой
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.time += 1
        self.vy -= self.g
        if self.y + self.r >= HEIGHT - 50 and self.vy < 0:
            self.vy = -0.8 * self.vy
            self.vy -= self.g
            self.vx = 0.5 * self.vx
        if self.x + self.r >= WIDTH:
            self.vx = -self.vx
        if type(obj) == Boss and obj.hittest(self):
            self.vx = -40 * math.cos(math.atan2(self.y - gun.y, self.x - gun.x))
            self.vy = 40 * math.sin(math.atan2(self.y - gun.y, self.y - gun.x))
            self.g = 0

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= self.r + obj.r:
            if type(obj) != Gun:
                return True
            elif self.time > 3:
                return True
        else:
            return False


class Shot:
    def __init__(self, screen, x, y):
        self.b = [Ball(screen, x, y) for i in range(10)]
        self.live = 1
        for i in range(len(self.b)):
            self.b[i].r = 10
            self.b[i].g = 0

    def move(self, obj, gun):
        """ moves each ball in shot
        """
        for ball in self.b:
            ball.move(obj, gun)

    def hittest(self, obj):
        """checks if shot hit a target"""
        k = 0
        for ball in self.b:
            if ball.hittest(obj):
                k += 1
        if k == 0:
            return False
        else:
            return True

    def draw(self):
        """draws shot"""
        for ball in self.b:
            ball.draw()


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 30
        self.f2_on = 0
        self.an = 0
        self.color = GREY
        self.x = 20
        self.y = 450
        self.pointing = 0
        self.live = 1
        self.r = 15
        self.shot_type = 1

    def fire2_start(self):
        self.f2_on = 1
        self.f2_power = 30

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet, shots
        self.an = -math.atan2((event.pos[1] - self.y), (event.pos[0] - self.x))
        bullet += 1
        if self.shot_type == 1:

            new_ball = Ball(self.screen, self.x, self.y)
            new_ball.r += 5

            new_ball.vx = 0.5 * self.f2_power * math.cos(- self.an)
            new_ball.vy = - 0.5 * self.f2_power * math.sin(- self.an)
            balls.append(new_ball)
        else:
            new_shot = Shot(self.screen, self.x, self.y)
            for i in range(10):
                new_shot.b[i].vx = 0.5 * self.f2_power * math.cos(- self.an + (i - 5) * math.pi / 180 * 9)
                new_shot.b[i].vy = - 0.5 * self.f2_power * math.sin(- self.an + (i - 5) * math.pi / 180 * 9)
            shots.append(new_shot)
        self.f2_on = 0
        self.f2_power = 30

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = - math.atan2((event.pos[1] - self.y), (event.pos[0] - self.x))

        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # Draws a gun-tank pointing self.pointing angle direction

        body = [(self.x - 20, self.y - 20),
                (self.x + 20, self.y - 20),
                (self.x + 20, self.y + 20),
                (self.x - 20, self.y + 20),
                (self.x - 20, self.y - 20)
                ]
        track1 = [(self.x - 25, self.y - 25),
                  (self.x + 25, self.y - 25),
                  (self.x + 25, self.y - 15),
                  (self.x - 25, self.y - 15)]

        track2 = [(self.x - 25, self.y + 25),
                  (self.x + 25, self.y + 25),
                  (self.x + 25, self.y + 15),
                  (self.x - 25, self.y + 15)]
        pygame.draw.polygon(self.screen, BLUE, rotate(body, self.x, self.y, self.pointing), 0)
        pygame.draw.polygon(self.screen, BLACK, rotate(track1, self.x, self.y, self.pointing))
        pygame.draw.polygon(self.screen, BLACK, rotate(track2, self.x, self.y, self.pointing))

        pygame.draw.circle(self.screen, GREEN, (self.x, self.y), 10, 0)
        pygame.draw.polygon(self.screen, self.color,
                            [(self.x - 5 * math.sin(self.an), self.y - 5 * math.cos(self.an)),
                             (self.x + 5 * math.sin(self.an), self.y + 5 * math.cos(self.an)),
                             (self.x + 5 * math.sin(self.an) + self.f2_power * math.cos(self.an),
                              self.y + 5 * math.cos(self.an) -
                              self.f2_power * math.sin(self.an)),
                             (self.x - 5 * math.sin(self.an) + self.f2_power * math.cos(self.an),
                              self.y - 5 * math.cos(self.an) -
                              self.f2_power * math.sin(self.an))]
                            )

    def shift(self, direction):
        """moves a gun position to the right if direction == 'right'
            to the left if direction == 'left'
            up if == 'up'
            down if == 'down'"""
        if direction == 'right':
            if self.pointing != math.pi / 4 and self.pointing != -math.pi / 4:
                self.x += 5
            else:
                self.x += 5 / math.sqrt(2)
        elif direction == 'left':
            if self.pointing != math.pi / 4 and self.pointing != -math.pi / 4:
                self.x -= 5
            else:
                self.x -= 5 / math.sqrt(2)
        elif direction == 'up':
            if self.pointing != math.pi / 4 and self.pointing != -math.pi / 4:
                self.y -= 5
            else:
                self.y -= 5 / math.sqrt(2)
        elif direction == 'down':
            if self.pointing != math.pi / 4 and self.pointing != -math.pi / 4:
                self.y += 5
            else:
                self.y += 5 / math.sqrt(2)

    def move(self, pressed):
        """checks if moving is needed and changes wheels direction,
        pressed: array of pressed keys"""
        # horizontal
        k = 0
        if pressed[pygame.K_d]:
            self.shift('right')
            k += 5
        elif pressed[pygame.K_a]:
            self.shift('left')
            k += 11
        # vertical
        if pressed[pygame.K_w]:
            self.shift('up')
            k += 16
        elif pressed[pygame.K_s]:
            self.shift('down')
            k += 20
        if k == 5 or k == 11:
            self.pointing = 0
        elif k == 16 or k == 20:
            self.pointing = math.pi / 2
        elif k == 21 or k == 31:
            self.pointing = math.pi / 4
        elif k == 27 or k == 25:
            self.pointing = -math.pi / 4

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 70:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def hit(self):
        self.live = 0


class Target:

    def __init__(self, screen):
        self.points = 0
        self.live = 1
        self.screen = screen
        self.new_target()
        self.vy = randint(-7, 7)
        self.vx = randint(-7, 7)

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(2, 50)
        self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r, 0)

    def move(self):
        self.y += self.vy
        self.x += self.vx
        if self.y + self.r > HEIGHT or self.y - self.r < 0:
            self.vy = -self.vy

        if self.x + self.r > WIDTH or self.x - self.r < 0:
            self.vx = -self.vx

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= self.r + obj.r:
            return True
        else:
            return False

class Boss:
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.r = 0
        self.color = YELLOW
        self.angle = 0
        self.points = 0
        self.live = 0
        # coordinates of 2 edges of the shield
        self.shield = [0, 0, 0, 0]

    def hit(self, points=5):
        """Попадание шарика в цель."""
        self.points += points

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(100, 780)
        self.y = randint(100, 550)
        self.r = randint(30, 80)
        self.live = 1

    def draw(self, obj):
        """draws target2 with shield pointing :par: obj: coordinates """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r, 0)
        self.angle = -math.atan2(self.y - obj.y, self.x - obj.x)
        self.shield[0] = self.x - self.r * math.cos(self.angle) - (self.r + 5) * math.sin(self.angle)
        self.shield[1] = self.y + self.r * math.sin(self.angle) - (self.r + 5) * math.cos(self.angle)
        self.shield[2] = self.x - self.r * math.cos(self.angle) + (self.r + 5) * math.sin(self.angle)
        self.shield[3] = self.y + self.r * math.sin(self.angle) + (self.r + 5) * math.cos(self.angle)
        pygame.draw.line(self.screen, BLACK, self.shield[0:2], self.shield[2:5], 5)

    def hittest(self, obj):
        """checks if obj hit shield"""

        f = math.sqrt((self.shield[3] - self.shield[1]) ** 2 + (self.shield[2] - self.shield[0]) ** 2)
        dist = ((obj.y - self.shield[1]) * (self.shield[2] - self.shield[0]) - (obj.x - self.shield[0]) * (
                self.shield[3] - self.shield[1])) / f

        if 0 <= dist <= 50:
            if (obj.x - (self.shield[0] + self.shield[2]) / 2) ** 2 + (
                    obj.y - (self.shield[1] + self.shield[3]) / 2) ** 2 <= obj.r ** 2 + (self.r + 5) ** 2:
                return True
            else:
                return False
        else:
            return False


def button(screen, name, name_color, background_color, x, y, font_size):
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


def endscreen(screen, Points, Bullets):
    """
    draws game_over screen
    :par screen: display
    """
    global restart_button_width, restart_button_length
    screen.fill(WHITE)
    button(screen, 'Game over', RED, GREEN, WIDTH / 2, HEIGHT / 5, game_over_size)
    if Points != 1:
        z = button(screen, 'score: ' + str(Points) + ' Points', RED, GREEN, WIDTH / 2, HEIGHT * 45 / 100 - 5,
                   Points_size)
    else:
        z = button(screen, 'score: ' + str(Points) + ' Point', RED, GREEN, WIDTH / 2, HEIGHT * 45 / 100 - 5,
                   Points_size)
    button(screen, 'Bullets: ' + str(Bullets), RED, GREEN, WIDTH / 2, HEIGHT * 45 / 100 + z[1] + 5, Points_size)
    restart_button_width, restart_button_length = button(screen, 'Restart', GREEN, BLUE, WIDTH / 2,
                                                         menu_y_cor - 5, restart_button_size)
    pygame.display.update()


def rotate(points, x, y, angle):
    """Rotates points in :par points: around point (x,y) on angle = angle
    returns: new set of points"""
    z = [((points[i][0] - x) * math.cos(angle) - (points[i][1] - y) * math.sin(-angle) + x,
          (points[i][1] - y) * math.cos(angle) + (points[i][0] - x) * math.sin(-angle) + y)
         for i in range(len(points))
         ]
    return z


def game_move(screen, balls, gun, target_set, boss):
    global finished, game_over, game_live, boss_live
    """moves each ball in balls array on screen, while checking every collision"""
    i = 0
    while i < len(balls):
        balls[i].move(boss, gun)
        for target in target_set:
            if balls[i].hittest(target) and target.live:
                target.hit()
                target.new_target()
                if randint(0, 2) == 0:
                    if boss.live == 0:
                        boss.new_target()
        if balls[i].hittest(boss):
            boss_live = 0
        if balls[i].hittest(gun):
            game_live = 0
        # checking if ball is low and slow enough to be deleted
        if abs(balls[i].vy) <= 3 and balls[i].y > HEIGHT - 70:
            balls.pop(i)
            i -= 1
        i += 1

    for target in target_set:
        if target.hittest(gun):
            game_live = 0

def button_hit(x_tap, y_tap, x_button, y_button, button_width, button_length):
    """
    checks if (x_tap, y_tap) is in rect (x_button, y_button, button_width, button_length) tapped on button
    :par x_tap: x cor of tap
    :par y_tap: y cor of tap
    :par x_button: x cor of the center of button
    :par y_button: y cor of the center of button
    returs: True or False
    """
    if abs(x_tap - x_button) < button_width / 2 and abs(y_tap - y_button) < button_length / 2:
        return True
    else:
        return False


def counter(screen, points, Bullets, x_cor, y_cor, font_size):
    """
    displays counter of points and misses on the screen
    :par points: number of points
    :par misses: number of points
    :par x_cor: 1 coordinate of top left corner of counter
    :par y_cor: 2 coordinate of top left corner of counter
    :par font_size: font size
    """
    points_counter(screen, points, x_cor, y_cor, font_size)
    misses_counter(screen, Bullets, x_cor, y_cor + 40, font_size)
def points_counter(screen, points, x_cor, y_cor, font_size):
    """
    displays counter of points at the right top corner of the screen
    :par points: number of points
    :par x_cor: 1 coordinate of top left corner of counter
    :par y_cor: 2 coordinate of top left corner of counter
    :par font_size: font size
    """
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render('Points: ' + str(points), True, GREEN, BLUE)
    textRect = text.get_rect()
    textRect.topleft = (x_cor, y_cor)
    screen.blit(text, textRect)
def misses_counter(screen, Bullets, x_cor, y_cor, font_size):
    """
    displays counter of points at the right top corner of the screen
    :par misses: number of points
    :par x_cor: 1 coordinate of top left corner of counter
    :par y_cor: 2 coordinate of top left corner of counter
    :par font_size: font size
    """
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render('Bullets: ' + str(Bullets), True, GREEN, BLUE)
    textRect = text.get_rect()
    textRect.topleft = (x_cor, y_cor)
    screen.blit(text, textRect)


def game():
    global bullet, balls, shots, game_over, restart_button_width, restart_button_length, game_live, boss_live
    pygame.init()
    main = True
    finished = False
    while main:
        game_live = 1
        boss_live = 1
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        bullet = 0
        p = 0
        balls = []
        shots = []
        clock = pygame.time.Clock()
        gun = Gun(screen)
        target_set = [Target(screen) for i in range(10)]
        boss = Boss(screen)

        while not finished:

            screen.fill(WHITE)
            gun.draw()
            boss.draw(gun)
            counter(screen, p, bullet, 0, 0, 50)
            for target in target_set:
                target.draw()
            for b in balls:
                b.draw()
            for shot in shots:
                shot.draw()
            pygame.display.update()

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    main = False
                    game_over = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    gun.fire2_start()
                elif event.type == pygame.MOUSEBUTTONUP:
                    gun.fire2_end(event)
                elif event.type == pygame.MOUSEMOTION:
                    gun.targetting(event)
            # moving gun
            pressed = pygame.key.get_pressed()
            gun.move(pressed)
            if pressed[pygame.K_1]:
                gun.shot_type = 1
            if pressed[pygame.K_2]:
                gun.shot_type = 2

            # moving each ball and checking if a ball hit a target
            game_move(screen, balls, gun, target_set, boss)
            # moving shots
            i = 0
            while i < len(shots):
                game_move(screen, shots[i].b, gun, target_set, boss)
                if shots[i].b[0].time > 30:
                    shots.pop(i)
                    i -= 1
                i += 1
            # checking if boss was hit
            if boss_live == 0:
                k = boss.points
                boss = Boss(screen)
                boss.points += k
                boss.hit()
                boss_live = 1

            # checking if gun was hit
            if game_live == 0:
                gun.hit()
                endscreen(screen, p, bullet)
                finished = True
                game_over = True
            # moving targets
            for target in target_set:
                target.move()
            gun.power_up()
            # counting points
            p = 0
            for target in target_set:
                p += target.points
            p += boss.points

        while game_over:
            # changing buttons if mouse pos is located on them
            x_mouse, y_mouse = pygame.mouse.get_pos()

            if button_hit(x_mouse, y_mouse, WIDTH / 2, menu_y_cor - 5, restart_button_width,
                          restart_button_length):
                button(screen, 'Restart', BLUE, GREEN, WIDTH / 2, menu_y_cor - 5, restart_button_size)
            pygame.display.update()
            button(screen, 'Restart', GREEN, BLUE, WIDTH / 2, menu_y_cor - 5, restart_button_size)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_over = False
                    finished = True
                    main = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    # checking if player tapped on restart button
                    if button_hit(event.pos[0], event.pos[1], WIDTH / 2, menu_y_cor - 5,
                                  restart_button_width, restart_button_length):
                        game_over = False
                        finished = False
    pygame.quit()


game()
